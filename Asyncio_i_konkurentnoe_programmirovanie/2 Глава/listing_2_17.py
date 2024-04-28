# Хронометраж двух конкурентных задач с помощью
# декоратора
import asyncio
from Asyncio_i_konkurentnoe_programmirovanie.util.async_timer import async_timed


@async_timed()
async def delay(delay_seconds: int) -> int:
    print(f"I'm gonna sleep for {delay_seconds}s.")
    await asyncio.sleep(delay_seconds)
    print(f"I'm awake up after {delay_seconds}s.")
    return delay_seconds


@async_timed()
async def main():
    task_one = asyncio.create_task(delay(2))
    task_two = asyncio.create_task(delay(3))

    await task_one
    await task_two


asyncio.run(main())
