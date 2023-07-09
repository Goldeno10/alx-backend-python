#!/usr/bin/env python3
'''
task: Given the parameters and the return values, add type annotations
to the function
Hint: look into TypeVar
'''
from typing import TypeVar, Dict, Any, Optional


T = TypeVar('T')


def safely_get_value(dct: Dict, key: T, default: Optional[T] = None) -> T:
    '''
    Function with added type annotations
    '''
    if key in dct:
        return dct[key]
    else:
        return default
