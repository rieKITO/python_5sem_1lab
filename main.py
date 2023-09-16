from multiprocessing import Pool

#LOGS
from config import logger

# TASKS
from tasks.GuessingNumber import guessing_number       # 1-1
from tasks.factorial import factorial_func             # 1-2
from tasks.average import average_func                 # 1-3
from tasks.add import add_func                         # 1-4/1-5
from tasks.LargeFactorial import large_factorial_func  # 1-6

def main_menu() -> None:
    print("Choose an action:\n" +
          "1) - (1-1) - Guess the number.\n" +
          "2) - (1-2) - Calculate the factorial.\n" +
          "3) - (1-3) - Calculate the average.\n" +
          "4) - (1-4) - Add two numbers.\n" +
          "5) - (1-5) - Calculate the execution time of the function.\n" +
          "6) - (1-6) - Calculate the large factorial (with threads).\n" +
          "7) - EXIT -"
)

def main():
    isExit = False

    while isExit == False:
        main_menu()
        isCorrect = False

        while isCorrect == False:
            try:
                choice = int(input("-> "))

                if choice < 1 or choice > 7:
                    logger.warning("Unavailable action selected!")

                else:
                    isCorrect = True
            except:
                logger.warning("Unavailable action selected!")

        match choice:
            case 1:
                guessing_number()
            case 2:
                factorial_func()
            case 3:
                average_func()
            case 4:
                add_func()
            case 5:
                add_func()
            case 6:
                large_factorial_func()
            case 7:
                isExit = True
    

if __name__ == '__main__':
    main()

