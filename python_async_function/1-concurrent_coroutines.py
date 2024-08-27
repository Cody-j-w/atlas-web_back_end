#!/usr/bin/env python3
"""
Module containing asyncronous sleep function
"""
import random
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n:int, max_delay:int) -> List[float]:
    tasks = []
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    wait_times = await asyncio.gather(*tasks)
    return wait_times
