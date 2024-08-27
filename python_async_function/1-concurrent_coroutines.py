#!/usr/bin/env python3
"""
Module containing asyncronous sleep function
"""
import random
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n:int, max_delay:int) -> List[float]:
    times: List[float] = []
    for task in asyncio.as_completed([wait_random(max_delay) for _ in range(n)]):
        res = await task
        times.append(res)
    return times

print(asyncio.run(wait_n(5,5)))