#!/usr/bin/env python3
""" appropriate types"""
from typing import List, Sequence, Iterable, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """iterable func"""
    return [(i, len(i)) for i in lst]
