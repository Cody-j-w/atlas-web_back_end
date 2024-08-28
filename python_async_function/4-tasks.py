#!/usr/bin/env python3
"""
Module containing function that calls multiple task_wait_random()s
"""
import random
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    accepts two ints:
    int n is the number of processes to start
    int max_delay is the max wait time of those processes
    returns a list of the wait times
    """
    times: List[float] = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        res = await task
        times.append(res)
    return times
