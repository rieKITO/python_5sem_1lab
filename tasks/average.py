# TASKS
from tasks.InputHandling import correct_input_float
from tasks.InputHandling import correct_input_int

def average(*args) -> float:
    if len(args) != 0:
        average = sum(args) / len(args)

    else:
        average = 0

    return average

def average_func() -> None:
    count = correct_input_int("Enter the count of arguments:")
    args = []

    for i in range(0, count):
        number = correct_input_float(f"Enter the {i + 1} argument:")
        args.append(number)

    print(f"Average: {average(*args)}\n")