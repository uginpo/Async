import threading


def hello_from_thread():
    print(f'Hello from thread {threading.current_thread()}!')


hello_thread = threading.Thread(target=hello_from_thread)
hello_thread.start()

total_threads = threading.active_count()
threads_name = threading.current_thread().name

print(f'В данный момент Python выполняет {total_threads} потоков')
print(f'Имя текущего потока {threads_name}')
hello_thread.join()


