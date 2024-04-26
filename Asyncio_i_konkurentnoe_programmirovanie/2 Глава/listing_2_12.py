# Снятие задачи
import asyncio
from util.delay_functions import delay


async def main() -> None:
    delay_task = asyncio.create_task(delay(2))

    try:
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Time-out!')
        print(f'Was the task cancelled? {delay_task.cancelled()}')

asyncio.run(main())
