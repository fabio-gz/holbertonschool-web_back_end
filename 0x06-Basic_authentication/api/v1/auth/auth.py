#!/usr/bin/env python3
"""API authentication."""
from flask import request


class Auth:
    """auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """paths function"""
        pass

    def authorization_header(self, request=None) -> str:
        """authorization header"""
        pass

    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        pass
