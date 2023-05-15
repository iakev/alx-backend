#!/usr/bin/env python3
"""
Contains a class simulating the simple pagination with
sample data
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    takes in pagination params i.e page and page_size
    computes the starting nd index and returns them as a tuple
    of index range format (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """
    Server class to paginate a database of popular baby names.
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
        """
        Takes in pagination params, aaerts the arguments are integers
        greater than 0, returns a list of pagination entries
        """
        baby_names = self.dataset()
        assert(type(page) == int and page > 0), \
            f"page shoul be an integer greater than 0"
        assert(type(page_size) == int and page_size > 0), \
            f"page_size shoul be an integer greater than 0"
        start, end = index_range(page, page_size)
        selected_baby_names = []
        if start < len(baby_names) and end <= len(baby_names):
            for i in range(start, end):
                selected_baby_names.append(baby_names[i])
        return selected_baby_names
