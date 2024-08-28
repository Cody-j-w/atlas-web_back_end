#!/usr/bin/env python3
"""
Module containing function that calls multiple wait_random()s
"""
import random
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, delay: int) -> List[float]:
    """
    accepts two ints:
    int n is the number of processes to start
    int delay is the max wait time of those processes
    returns a list of the wait times
    """
    times: List[float] = []
    for task in asyncio.as_completed([wait_random(delay) for _ in range(n)]):
        res = await task
        times.append(res)
    return times
