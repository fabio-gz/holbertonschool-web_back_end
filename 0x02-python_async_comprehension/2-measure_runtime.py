#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
from asyncio import gather
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure the total runtime """
    performance = perf_counter()
    await gather(async_comprehension())
    t = perf_counter() - performance
    return t
