# Повторно используемая сопрограмма delay
import asyncio


async def delay(delay_seconds: int) -> int:
    print(f"I'm sleeping for {delay_seconds} s.")
    await asyncio.sleep(delay_seconds)
    print(f"I'm waked up after {delay_seconds}s.")
    return delay_seconds





