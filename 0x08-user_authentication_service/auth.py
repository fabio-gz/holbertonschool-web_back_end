#!/usr/bin/env python3
"""Hash password"""
import bcrypt


def _hash_password(password: str) -> str:
    """hash a password"""
    enc = password.encode('utf-8')
    hashed = bcrypt.hashpw(enc, bcrypt.gensalt())
    return hashed
