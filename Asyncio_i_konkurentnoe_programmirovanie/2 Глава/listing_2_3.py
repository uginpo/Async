import asyncio


async def coroutine_add_one(number: int) -> int:
    return number + 1

coroutine_result = asyncio.run(coroutine_add_one(5))

print(f'Result of function is equal to {coroutine_result}\nand type is {type(coroutine_result)}')
