#!/usr/bin/env python3
"""
Module containing asyncronous number generator comprehension function
"""

import random
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    lst: List[float] = []
    async for i in async_generator():
        lst.append(i)
    return lst
