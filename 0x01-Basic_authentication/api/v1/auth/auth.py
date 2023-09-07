#!/usr/bin/env python3
"""Auth class"""

from flask import request
from typing import List, TypeVar


User = TypeVar('User')


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        always returns False for demonstration purposes.
        """
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
