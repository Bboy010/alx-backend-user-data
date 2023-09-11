#!/usr/bin/env python3
"""Auth class"""

from flask import request
from typing import List, TypeVar

User = TypeVar('User')


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Check if authentication is required for the given path. """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        # Make the path slash tolerant
        slash_path = path if path.endswith("/") else path + "/"

        for excluded_path in excluded_paths:
            # Make the excluded paths slash tolerant as well
            excluded_slash = (
                excluded_path
                if excluded_path.endswith("/")
                else excluded_path + "/"
            )
            if slash_path.startswith(excluded_slash):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Get the 'Authorization' header value from the request. """
        if request is None:
            return None

        # Check if 'Authorization' header is present in the request
        authorization_header = request.headers.get('Authorization')

        return authorization_header

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get the current user """
        return None
