#!/usr/bin/env python3
"""
Module containing function that times the execution time of 4 instances of
the async_comprehension function
"""
import random
from asyncio import gather
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    compare runtimes of four parallel async functions
    """
    start = time.time()
    await gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension())
    stop = time.time()
    return stop - start
