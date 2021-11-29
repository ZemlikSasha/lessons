"""
Написать функцию, которая будет вызывать задержку выполнения программы случайным образом от 1-й до 5-ти секунд.
Написать декоратор, который будет выводить на печать время выполнения этой функции (end_time - start_time).
"""
import datetime
import random
import time




def exec_time_decorator(func):
    def print_exec_tims():
        start_time = datetime.datetime.now()
        result = func()
        end_time = datetime.datetime.now()
        print(end_time - start_time)

        return result
    return print_exec_tims

@exec_time_decorator
def random_delay():
    time.sleep(random.randint(1, 5))


if __name__ == "__main__":
    random_delay()




