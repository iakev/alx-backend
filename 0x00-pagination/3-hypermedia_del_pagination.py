#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a hyper-media like response that is deletion resilient
        """
        index_data = self.indexed_dataset()
        hyper_index = {}
        hyper_index['page_size'] = page_size
        if index or index == 0:
            assert(type(index) == int and 0 <= index <= len(index_data)), \
                f"index should be less than len of dataset"
            hyper_index['index'] = index
            curr_index = index
            while index_data.get(curr_index) is None:
                curr_index += 1
            next_index = curr_index + page_size
            hyper_index['next_index'] = next_index
            data = []
            for i in range(curr_index, next_index):
                data.append(index_data.get(i))
            hyper_index['data'] = data
        return hyper_index
