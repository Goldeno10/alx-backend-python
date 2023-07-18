#!/usr/bin/env python3
"""
Task:
    Write a coroutine called async_generator that takes no arguments.
    The coroutine will loop 10 times, each time asynchronously wait 1
    second, then yield a random number between 0 and 10. Use the random
    module.
"""

import asyncio
from collections.abc import AsyncGenerator
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """
    This coroutine will loop 10 times, each time asynchronously
    wait 1 second, then yield a random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)  # Yield a random number between 0 and 10
