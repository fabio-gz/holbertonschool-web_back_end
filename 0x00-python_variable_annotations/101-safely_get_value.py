#!/usr/bin/env python3
"""More involved type annotations"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Given the parameters and the return value"""
    if key in dct:
        return dct[key]
    else:
        return default
