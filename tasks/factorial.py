# TASKS
from tasks.InputHandling import correct_input_int

def factorial(start, end) -> int:
    result = 1
    
    for i in range(start, end + 1):
        result *= i

    return result

def factorial_func() -> None:
    factorialNum = correct_input_int("Enter the number:")
    print(f"Number: {factorialNum}\n" +
          f"Factorial: {factorial(1, factorialNum)}\n"
    )