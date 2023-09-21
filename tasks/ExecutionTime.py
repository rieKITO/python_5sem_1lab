import time

def execution_time(function):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        function(*args, **kwargs)
        endTime = time.time()
        executionTime = format((endTime - startTime), '.100f')
        return executionTime
    
    return wrapper

def calc_execution_time(function) -> None:
    execution_time_func_decorated = execution_time(function)
    print(f"{function.__name__} was completed in {execution_time_func_decorated()}s\n")