#!/usr/bin/env python3
"""Regex-ing"""
from typing import List
import re
import logging


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """ log message obfuscated"""
    for i in fields:
        message = re.sub(i + '=.+?' + separator, i + '=' + redaction +
                         separator, message)
    return message


def get_logger() -> logging.Logger:
    """logger object"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    sthanlder = logging.StreamHandler()
    sthanlder.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(sthanlder)
    return logger


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """init method"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)
