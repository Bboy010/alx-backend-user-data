#!/usr/bin/env python3
"""
Route module for the API
"""

from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth

app = Flask(__name__)
app.register_blueprint(app_views)

# Enable Cross-Origin Resource Sharing (CORS) for your API
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Initialize the authentication system
auth = None
auth_type = getenv("AUTH_TYPE")
if auth_type:
    if auth_type == "basic_auth":
        auth = BasicAuth()
    else:
        auth = Auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler

    :param error: The error object.
    :type error: Exception
    :return: JSON response for a 404 error.
    :rtype: str
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized handler

    :param error: The error object.
    :type error: Exception
    :return: JSON response for a 401 error.
    :rtype: str
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden handler

    :param error: The error object.
    :type error: Exception
    :return: JSON response for a 403 error.
    :rtype: str
    """
    return jsonify({"error": "Forbidden"}), 403


# Add a method to handle before_request
@app.before_request
def before_request():
    """
    Handle authentication before processing the request.

    If authentication is required for the requested path,
    this function checks for the presence of
    the 'Authorization' header and the current user.
    It aborts the request with a 401 Unauthorized
    or 403 Forbidden response if authentication fails.

    :return: None
    """
    if auth is None:
        return

    # List of paths that do not require authentication
    excluded_paths = [
        '/api/v1/status/',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden/'
    ]

    if request.path not in excluded_paths:
        if auth.authorization_header(request) is None:
            abort(401)

        if auth.current_user(request) is None:
            abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
