#!/usr/bin/env python3
"""Module for element_length function."""
from typing import List, Sequence, Iterable, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples with the sequence and its length."""
    return [(i, len(i)) for i in lst]
