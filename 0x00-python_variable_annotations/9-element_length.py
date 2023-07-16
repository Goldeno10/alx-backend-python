#!/usr/bin/env python3
'''
Contain a type-annotated function element_length
'''
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Return a list of tuple of int
    '''
    return [(i, len(i)) for i in lst]
