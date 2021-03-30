#!/usr/bin/env python3
"""Encrypting passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """salted, hashed password"""
    encodedp = str.encode(password)
    hashed = bcrypt.hashpw(encodedp, bcrypt.gensalt())
    return hashed
