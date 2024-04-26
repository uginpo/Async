import time


def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        match n:
            case 1:
                return 0
            case 2:
                return 1
            case _:
                return fib(n - 1) + fib(n - 2)

    print(f'fib(number)= {fib(number)}')


def fibs_no_threading():
    print_fib(40)
    print_fib(41)


start = time.time()
fibs_no_threading()
end = time.time()

print(f'It took {end - start} s')
