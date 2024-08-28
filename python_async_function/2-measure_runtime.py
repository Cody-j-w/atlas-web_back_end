#!/usr/bin/env python3
"""
Module containing function that times the execution time of wait_n()
"""
import random
import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    accept two ints, and call wait_n() with those ints
    int n is the number of processes for wait_n to begin
    int max_delay is the maximum delay on those processes
    return the time it takes to execute those processes
    """
    start_point: float = time.process_time()
    await wait_n(n, max_delay)
    stop_point: float = time.process_time()
    return stop_point - start_point
