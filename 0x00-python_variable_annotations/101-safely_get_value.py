#!/usr/bin/env python3
'''
task: Given the parameters and the return values, add type annotations
to the function
Hint: look into TypeVar
'''
from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    '''
    Function with added type annotations
    '''
    if key in dct:
        return dct[key]
    else:
        return default
