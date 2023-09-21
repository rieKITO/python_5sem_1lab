import threading
import sys

# TASKS
from tasks.factorial import factorial
from tasks.InputHandling import correct_input_natural

def calculate_factorial(number, threadsCount):

    def partial_factorial(start, end):
        thread.result = factorial(start, end)

    result = 1
    threads = []
    
    for i in range(threadsCount):
        start = (number // threadsCount) * i + 1
        end = (number // threadsCount) * (i + 1)
        
        if i == threadsCount - 1:
            end = number
        
        thread = threading.Thread(target=partial_factorial, args=(start, end))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    for thread in threads:
        result *= thread.result
    
    return result

def large_factorial_func() -> None:
    sys.set_int_max_str_digits(100000)
    number = correct_input_natural("Enter the number:")
    threadsCount = correct_input_natural("Enter the count of threads:")

    print(f"Factorial: {calculate_factorial(number, threadsCount)}\n")