#!/usr/bin/env python3

"""
module containing make_multiplier function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Accept a float, pass it into an internal function, and multiply it
    Return a float
    """
    def multiply(multi: float) -> float:
        return multi * multiplier
    return multiply
