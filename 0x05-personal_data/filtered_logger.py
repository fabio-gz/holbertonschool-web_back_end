#!/usr/bin/env python3
"""filtered logger personal data"""
from typing import List
import re
import logging
import os
import mysql.connector


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


def get_db() -> mysql.connector.connection.MySQLConnection:
    """connect to database"""
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', "root")
    psw = os.getenv('PERSONAL_DATA_DB_PASSWORD', "")
    host = os.getenv('PERSONAL_DATA_DB_HOST', "localhost")
    database = os.getenv('PERSONAL_DATA_DB_NAME')

    connect = mysql.connector.connect(host=host, database=database,
                                      user=username, password=psw)

    return connect


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """init method"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """formatter function"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)
