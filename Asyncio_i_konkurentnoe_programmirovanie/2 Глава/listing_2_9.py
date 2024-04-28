import asyncio
from Asyncio_i_konkurentnoe_programmirovanie.util.delay_functions import delay


async def main() -> None:
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_ones_more = asyncio.create_task(delay(3))

    await sleep_for_three
    await sleep_again
    await sleep_ones_more


asyncio.run(main())
