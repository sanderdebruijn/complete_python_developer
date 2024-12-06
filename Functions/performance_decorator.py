# Decorator practice
from time import time


def relative_performance(func):
    def wrapper_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print({f"It took {t2-t1} s"})
        return result
    return wrapper_func


@relative_performance
def long_time():
    for i in range(100000000):
        i*5


long_time()
