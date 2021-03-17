#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async
"""
import random
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """corutine"""
    ran, sort = [], []
    for _ in range(n):
        ran.append(wait_random(max_delay))

    for i in asyncio.as_completed(ran):
        sort.append(await i)

    return sort