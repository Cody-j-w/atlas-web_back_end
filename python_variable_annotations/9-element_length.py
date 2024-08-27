#!/usr/bin/env python3

"""
module containing make_multiplier function
"""

from typing import Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> Tuple[Sequence, int]:
    return [(i, len(i)) for i in lst]
