# TASKS
from tasks.InputHandling import correct_input_int

def factorial(number) -> int:
    if number == 1:
        return number
    
    else:
        return number * factorial(number - 1)

def factorial_func() -> None:
    factorialNum = correct_input_int("Enter the number:")
    print(f"Number: {factorialNum}\n" +
          f"Factorial: {factorial(factorialNum)}\n"
    )