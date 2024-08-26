#!/usr/bin/env python3

"""
module containing sum_list function
"""


def sum_list(input: list[float]) -> float:
    """
    accept a list of floats, and return the sum of that list
    """

    res: float = 0
    for x in input:
        res += x
    return res
