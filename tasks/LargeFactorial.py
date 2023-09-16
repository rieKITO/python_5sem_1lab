from multiprocessing import Pool

# TASKS
from tasks.factorial import factorial
from tasks.InputHandling import correct_input_int
 
def large_factorial(num, threadsNum):
    pool = Pool(processes = threadsNum)
    chunkSize = num // threadsNum
    results = pool.map(factorial, range(1, num + 1, chunkSize))

    pool.close()
    pool.join()

    result = 1

    for res in results:
        result *= res

    return result

def large_factorial_func() -> None:
    number = correct_input_int("Enter the number:")
    threadsCount = correct_input_int("Threads count:")

    print(f"Factorial: {large_factorial(number, threadsCount)}\n")