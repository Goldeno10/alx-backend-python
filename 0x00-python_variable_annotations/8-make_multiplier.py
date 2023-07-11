#!/usr/bin/env python3
'''
Contain a type-annotated function make_multiplier that takes a
float multiplieras argument and returns a function that multiplies
a float by multiplier.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    type-annotated function make_multiplier
    '''
    def multiply(x: float) -> float:
        '''
        function that multiplies a float by multiplier.
        '''
        return x * multiplier
    return multiply
