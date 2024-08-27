#!/usr/bin/env python3
import random
import asyncio


async def wait_random(max_delay: float=10) -> float:
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
