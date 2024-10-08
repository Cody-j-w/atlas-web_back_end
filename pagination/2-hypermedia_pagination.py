#!/usr/bin/env python3
"""
pagination module
"""
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a section of data from the dataset
        based on the provided page and page_size numbers
        """
        assert type(page) is int
        assert type(page_size) is int
        assert page > 0
        assert page_size > 0
        data = []
        idx = index_range(page, page_size)
        if idx[1] < len(self.dataset()):
            for i in range(idx[0], idx[1]):
                data.append(self.dataset()[i])
        elif idx[0] < len(self.dataset()):
            for i in range(idx[0], len(self.dataset())):
                data.append(self.dataset()[i])
        return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ Compile the information for a page into a dict
        Accept two params:
            int page - the current page
            int page_size - the number of entries in the page
        Return a dict with the following keys:
            page_size - the page_size param
            page - the page param
            data - the return fvalue of the get_page() method
            next_page - the number of the next page, if it exists
            prev_page - the number of the previous page, if it exists
            total_pages - the total number of pages
        """
        info = {}
        total_pages = math.ceil(len(self.dataset()) / page_size)
        assert type(page_size) is int
        assert page_size > 0
        info['page_size'] = page_size
        assert type(page) is int
        assert page > 0
        info['page'] = page
        if page <= total_pages:
            info['data'] = self.get_page(page, page_size)
        else:
            info['data'] = []
        if page < total_pages:
            info['next_page'] = page + 1
        else:
            info['next_page'] = None
        if page - 1 > 0:
            info['prev_page'] = page - 1
        else:
            info['prev_page'] = None
        info['total_pages'] = total_pages

        return info
