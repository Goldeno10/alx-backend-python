#!/usr/bin/env python3
"""
Task:
    Import async_comprehension from the previous file and write a
    measure_runtime coroutine that will execute async_comprehension four
    times in parallel using asyncio.gather.

    measure_runtime should measure the total runtime and return it.
    Notice that the total runtime is roughly 10 seconds, explain it
    to yourself.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() ->  float:
    """
    coroutine that will execute async_comprehension four times in
    parallel using asyncio.gather.
    It measures the total runtime and returns it.
    """
    s: float = time.perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension()
                         )
    s: float = time.perf_counter() - s
    return s
