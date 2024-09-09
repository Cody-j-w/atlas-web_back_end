#!/usr/bin/env python3
"""
logger filtering module
"""

import re
from typing import List
import logging


PII_FIELDS = ('phone', 'name', 'ssn', 'password', 'email')


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """ filter personal information out of provided string
    """
    for field in fields:
        pattern = r"" + re.escape(field) + r"=.*?"+re.escape(separator)
        message = re.sub(pattern, f"{field}={redaction}{separator}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.FIELDS = fields

    def format(self, record: logging.LogRecord) -> str:
        """ format log record with redactions
        """
        log = record.msg
        log = filter_datum(self.FIELDS, self.REDACTION, log, self.SEPARATOR)
        record.msg = log
        return logging.Formatter(self.FORMAT).format(record)


def get_logger() -> logging.Logger:
    redaction_hdlr = RedactingFormatter(PII_FIELDS)
    user_data = logging.Logger()
    user_data.setLevel(20)
    user_data.addHandler(redaction_hdlr)
    user_data.propagate = False
    return user_data
