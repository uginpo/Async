# Защита задачи от снятия
import asyncio
from util.delay_functions import delay


async def main() -> None:
    task = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(asyncio.shield(task), timeout=5)
        print(result)
    except TimeoutError:
        print("It's taking more than 5 seconds. Wait for not so long")
        result = await task
        print(result)

asyncio.run(main())
