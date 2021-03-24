#!/usr/bin/env python3
"""Hypermedia pagination"""
import csv
import math
from typing import List


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

    @staticmethod
    def index_range(page: int, page_size: int) -> tuple:
        """start - end index"""
        return ((page - 1) * page_size, page * page_size)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get page function"""
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        idx = self.index_range(page, page_size)
        baby_names = self.dataset()
        page = baby_names[idx[0]: idx[1]]

        return page

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """hyper method that returns dict"""
        d = {}
        baby_names = len(self.dataset()) / page_size

        d['page_size'] = page_size if self.get_page(page, page_size) else 0
        d['page'] = page
        d['data'] = self.get_page(page, page_size)

        next_page = None
        if baby_names > page:
            next_page = page + 1
        else:
            None
        d['next_page'] = next_page

        prev_page = None
        if page != 1:
            prev_page = page - 1
        else:
            None
        d['prev_page'] = prev_page

        d['total_pages'] = math.ceil(baby_names)

        return d
