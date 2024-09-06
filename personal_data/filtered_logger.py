#!/usr/bin/env python3
"""
logger filtering module
"""

import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """ filter personal information out of provided string
    """
    for field in fields:
        pattern = r"" + re.escape(field) + r"=.*?"+re.escape(separator)
        message = re.sub(pattern, field + '=' + redaction + ';', message)
    return message
