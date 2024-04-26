import time
import threading


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


def fibs_with_threads():
    fortieth_thread = threading.Thread(target=print_fib, args=(40,))
    forty_first_thread = threading.Thread(target=print_fib, args=(41,))

    fortieth_thread.start()
    forty_first_thread.start()

    fortieth_thread.join()
    forty_first_thread.join()


start_threads = time.time()
fibs_with_threads()
end_threads = time.time()

print(f'It took {end_threads - start_threads} s')
