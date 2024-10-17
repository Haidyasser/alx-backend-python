#!/usr/bin/env python3
'''
3. Tasks
'''
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Take the function wait_random and return a asyncio.Task"""
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
