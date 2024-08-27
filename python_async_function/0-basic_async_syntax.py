#!/usr/bin/env python3
"""
Module containing asyncronous sleep function
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Accept an integer, wait a number of seconds between 0 and max_delay
    Return the time waited as a float
    """
    rand: float = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
