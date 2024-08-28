#!/usr/bin/env python3
"""
Module containing asyncronous number generator
"""
import random
import asyncio


async def async_generator() -> float:
    """
    async function that generates 10 numbers between 0 and 10
    """

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
