import asyncio
from Asyncio_i_konkurentnoe_programmirovanie.util.delay_functions import delay


async def hello_every_second():
    for i in range(2):
        await asyncio.sleep(1)
        print("When I'm waiting for, it's running another code")


async def main() -> None:
    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(3))

    await hello_every_second()
    await first_delay
    await second_delay



asyncio.run(main())
