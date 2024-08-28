#!/usr/bin/env python3
"""
Module containing function that creates a wait_random() task
"""
import random
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    accepts an int
    max_delay is the maximum delay time of the generated wait_random Task
    returns the wait_random Task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
