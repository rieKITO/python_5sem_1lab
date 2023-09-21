# TASKS
from tasks.InputHandling import correct_input_float
from tasks.InputHandling import correct_input_natural

def average(*args) -> float:
    if len(args) != 0:
        average = sum(args) / len(args)

    else:
        average = 0

    return average

def average_func() -> None:
    count = correct_input_natural("Enter the count of arguments:")
    args = []

    if count != 0:
        for i in range(0, count):
            number = correct_input_float(f"Enter the {i + 1} argument:")
            args.append(number)

        print(f"Average: {average(*args)}\n")
    else: print(f"Average: 0\n")