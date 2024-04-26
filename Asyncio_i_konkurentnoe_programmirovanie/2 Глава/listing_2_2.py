async def coroutine_add_one(number: int) -> int:
    return number + 1


def add_one(number: int) -> int:
    return number + 1


function_result = add_one(5)
coroutine_result = coroutine_add_one(5)

print(f'Result of function is equal to {function_result}\nand type is {type(function_result)}')
print(f'Result of function is equal to {coroutine_result}\nand type is {type(coroutine_result)}')
