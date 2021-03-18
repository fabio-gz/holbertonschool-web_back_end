#!/usr/bin/env python3
"""Async Generator"""
from asyncio import sleep
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """The coroutine will loop 10 times"""
    for _ in range(10):
        await sleep(1)
        yield random.uniform(0, 10)
