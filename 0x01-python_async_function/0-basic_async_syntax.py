#!/usr/bin/env python3

import asyncio, random

async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay seconds"""
    max_delay = random.uniform(0, max_delay)
    await asyncio.sleep(max_delay)
    return max_delay

