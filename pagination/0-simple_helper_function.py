#!/usr/bin/env python3
"""
index_range module
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    page indexing helper function
    page: the current page
    page_size: the size of the pages
    Return: a tuple containing the beginning and ending indices of the current page
    """

    start = 0
    start += (page-1) * (page_size)
    index_tuple = (start, start+page_size)
    return index_tuple
