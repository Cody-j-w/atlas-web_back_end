#!/usr/bin/env python3

"""
module containing to_kv function
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    accepts a str and either an int or a float, and returns a tuple with the str and the square of the int/float
    """

    sq: float = v*v
    new_tuple: Tuple[str, float] = (k, sq)
    return new_tuple
