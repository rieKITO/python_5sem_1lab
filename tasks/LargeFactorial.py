import threading
import sys
import time

# TASKS
from tasks.factorial import factorial
from tasks.InputHandling import correct_input_int

def execution_time(function):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        result = function(*args, **kwargs)
        endTime = time.time()
        executionTime = format((endTime - startTime) * 1000, '.100f')
        print(f"{function.__name__} was completed in {executionTime}ms\n")
        return result
    return wrapper

@execution_time
def calculate_factorial(number, threadsCount):

    def partial_factorial(start, end):
        thread.result = factorial(start, end)

    result = 1
    threads = []
    
    # Разделение вычислений на потоки
    for i in range(threadsCount):
        start = (number // threadsCount) * i + 1
        end = (number // threadsCount) * (i + 1)
        
        if i == threadsCount - 1:
            end = number
        
        thread = threading.Thread(target=partial_factorial, args=(start, end))
        threads.append(thread)
        thread.start()
    
    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()
    
    # Вычисление итогового результата
    for thread in threads:
        result *= thread.result
    
    return result

def large_factorial_func() -> None:
    sys.set_int_max_str_digits(100000)
    number = correct_input_int("Enter the number:")
    threadsCount = correct_input_int("Enter the count of threads:")

    print(f"Factorial: {calculate_factorial(number, threadsCount)}\n")