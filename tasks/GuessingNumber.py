import random

#LOGS
from config import logger

# TASKS
from tasks.InputHandling import correct_input_int

def correct_input_boundaries(leftBorder: int, rightBorder: int, type: str) -> int:
    isCorrect = False

    while isCorrect == False:

        try:
            number = int(input(f"\n{type}\n-> "))

            if number >= leftBorder and number <= rightBorder: 
                isCorrect = True
            else:
                logger.warning("Inaccessible value entered!")
        except:
            logger.warning("Inaccessible value entered!")

    return number

def guessing_number() -> None:
    print("Enter the range boundaries:")
    leftBorder = correct_input_int("Left border:")
    rightBorder = correct_input_int("Right border:")

    if (rightBorder < leftBorder):
        #swapping
        leftBorder, rightBorder = rightBorder, leftBorder

    randNum = random.randint(leftBorder, rightBorder)
    userNum = correct_input_boundaries(leftBorder, rightBorder, "Enter the number:")
    iterationsCount = 1
    
    while userNum != randNum:
        print("\nYou didn't guessed the number(((")
        userNum = correct_input_boundaries(leftBorder, rightBorder, "Try again:")
        iterationsCount += 1

    print("\nYou guessed the number!!!\n" +
          f"Iterations count: {iterationsCount}\n"
    )