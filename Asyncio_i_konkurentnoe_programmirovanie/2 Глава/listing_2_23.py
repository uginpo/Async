# Выполнение счетного кода в отладочном режиме
import asyncio
from Asyncio_i_konkurentnoe_programmirovanie.util.async_timer import async_timed


@async_timed()
async def cpu_bond_work() -> int:
    counter = 0
    for i in range(100000000):
        counter += 1
    return counter


async def main() -> None:
    task_one = asyncio.create_task(cpu_bond_work())
    await task_one


asyncio.run(main(), debug=True)
