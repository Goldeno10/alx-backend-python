#!/usr/bin/env python3
'''
Contain a type-annotated function element_length
'''
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    '''
    Return a list of tuple of int
    '''
    return [(i, len(i)) for i in lst]
