#!/usr/bin/env python3
"""API authentication."""
from flask import request
from typing import List, TypeVar


class Auth:
    """auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """paths function"""
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """authorization header"""
        pass

    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        pass
