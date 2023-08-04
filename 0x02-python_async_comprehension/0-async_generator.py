#!/usr/bin/env python3
"""
Task:
    Write a coroutine called async_generator that takes no arguments.
    The coroutine will loop 10 times, each time asynchronously wait 1
    second, then yield a random number between 0 and 10. Use the random
    module.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    This coroutine will loop 10 times, each time asynchronously
    wait 1 second, then yield a random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield Generator[float, None, None]random.uniform(0, 10)  # Yield a random number between 0 and 10
