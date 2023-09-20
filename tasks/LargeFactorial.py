import threading

# TASKS
from tasks.factorial import factorial
from tasks.InputHandling import correct_input_int
 
def large_factorial(number):
    if number <= 0:
        return 0
    
    elif number == 1:
        return 1

    results = []
    threadsCount = 0

    def calculate_factorial(num):
        result = factorial(num)
        results.append(result)

    threads = []
    for i in range(1, number + 1):
        thread = threading.Thread(target=calculate_factorial, args=(i,))
        threads.append(thread)
        thread.start()
        threadsCount += 1

        if threadsCount >= threadsNum:
            for thread in threads:
                thread.join()
            threads = []
            threadsCount = 0

    for thread in threads:
        thread.join()

    return results[len(results) - 1]

def large_factorial_func() -> None:
    number = correct_input_int("Enter the number:")

    print(f"Factorial: {large_factorial(number)}\n")