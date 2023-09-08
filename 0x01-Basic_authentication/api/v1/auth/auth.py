#!/usr/bin/env python3
"""Auth class"""

from flask import request
from typing import List, TypeVar


User = TypeVar('User')


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if authentication is required for the given path.
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        # slash tolerant path
        slash_path = path if path.endswith("/") else path + "/"

        for excluded_path in excluded_paths:
            # excluded paths are slash tolerant as well
            excluded_slash = (
                    excluded_path
                    if excluded_path.endswith("/")
                    else excluded_path + "/"
                    )
            if slash_path.startswith(excluded_slash):
                return False

        return True

        return False

    def authorization_header(self, request=None) -> str:
        """
        returns always None for demonstration purposes.
        """
        return None

    def current_user(self, request=None) -> User:
        """
        method that always returns None for demonstration purposes.
        """
        return None
