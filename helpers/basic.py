import time
from functools import wraps


def test(name, actual, expected):
    if actual != expected:
        print("Test {} FAILED get {} Expected {} ".format(name, actual, expected))
    else:
        print("Test {} OK".format(name))


def timer(func):
    @wraps(func)
    def decor(*args, **kargs):
        start = time.time()
        res = func(*args, **kargs)
        print('{} execution time is {}'.format(func.__name__.title(), time.time() - start))
        return res
    return decor
