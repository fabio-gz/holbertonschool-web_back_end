#!/usr/bin/env python3
"""Encrypting passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """salted, hashed password"""
    encodedp = str.encode(password)
    hashed = bcrypt.hashpw(encodedp, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """validate the password"""
    encodedp = str.encode(password)
    if bcrypt.checkpw(encodedp, hashed_password):
        return True
    else:
        return False
