#!/usr/bin/env python3
"""Hash password"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from bcrypt import hashpw, gensalt, checkpw
from uuid import uuid4


def _hash_password(password: str) -> str:
    """hash a password"""
    enc = password.encode('utf-8')
    hashed = bcrypt.hashpw(enc, bcrypt.gensalt())
    return hashed


def _generate_uuid() -> str:
    """rep of a new uuid"""
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """init method"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register new User"""
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError('User {} already exists'.format(user.email))
        except NoResultFound:
            hashed = _hash_password(password)
            new_user = self._db.add_user(email, hashed)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """Checks if login is valid"""
        try:
            user_f = self._db.find_user_by(email=email)
            return checkpw(str.encode(password), user_f.hashed_password)
        except NoResultFound:
            return False
