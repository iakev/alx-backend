#!/usr/bin/env python3
"""
Contains a helper function that returns starting and ending
indices for particluar pagination parameters
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    takes in pagination params i.e page and page_size
    computes the starting nd index and returns them as a tuple
    of index range format (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
