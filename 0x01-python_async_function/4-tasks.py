#!/usr/bin/env python3
"""more Tasks"""
from asyncio import as_completed
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """coroutine Tasks"""
    sort_delays, tasks = [], []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for i in as_completed(tasks):
        result = await i
        sort_delays.append(result)

    return sort_delays
