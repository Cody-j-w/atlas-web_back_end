#!/usr/bin/env python3

"""
module containing annotated element_length function
"""

from typing import Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> Tuple[Sequence, int]:
    """
    Accepts an iterable of some kind
    Returns a tuple
    """

    return [(i, len(i)) for i in lst]
