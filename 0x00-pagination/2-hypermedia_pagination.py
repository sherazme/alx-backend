#!/usr/bin/env python3
"""Hypermedia pagination """

import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Retrieves the index range from given page and page size """

    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)


class Server:
    """ paginate database of popular baby names """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset
