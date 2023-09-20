import time

# TASKS
from tasks.InputHandling import correct_input_float

def add(x):
    def inner(y):
        return x + y
    return inner

def add_func() -> None:
    x = correct_input_float("Enter X:")
    y = correct_input_float("Enter Y:")

    print(f"X: {x}\n" +
          f"Y: {y}\n" +
          f"X + Y = {add(x)(y)}\n"
    )