# Снятие задачи
import asyncio
from asyncio import CancelledError
from Asyncio_i_konkurentnoe_programmirovanie.util.delay_functions import delay


async def main() -> None:
    long_task = asyncio.create_task(delay(10))

    second_elapses = 0

    while not long_task.done():
        print('Our task is not finished. Check please...')
        print(f'{second_elapses = }')
        await asyncio.sleep(1)
        second_elapses += 1

        if second_elapses == 5:
            long_task.cancel()

    try:
        await long_task
    except CancelledError:
        print('Our task is cancelled')

asyncio.run(main())
