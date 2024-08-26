#!/usr/bin/env python3

"""
module containing sum_mixed_list function
"""

from typing import List, Union


def sum_mixed_list(input: List[Union[int, float]]) -> float:
    """
    accepts a mixed type list and returns the sum of its elements as a float
    """

    sum: float = 0

    for x in input:
        sum += x
    return sum
