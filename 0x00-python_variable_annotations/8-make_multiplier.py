#!/usr/bin/env python3
"""takes a float multiplier as argument and returns a function that multiplies a float by multiplier. """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return func that multiplies"""
    def f(n: float) -> float:
        return (n * multiplier)
    return f
