# Основы будущих объектов
from asyncio import Future

my_future = Future()
print(f'Is my future ready? {my_future.done()}')

my_future.set_result(42)
print(f'Is my future ready? {my_future.done()}')

print(f'What is my result in future? {my_future.result()}')



