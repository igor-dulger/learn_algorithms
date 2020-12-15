from Percolation import Percolation
import sys
import random
import time
from functools import wraps


def timer(func):
    @wraps(func)
    def decor(*args, **kargs):
        start = time.time()
        res = func(*args, **kargs)
        print('{}: {} execution time {}'.format(str, func.__name__, time.time() - start))
        return res
    return decor

@timer
def main():
    @timer
    def check_leaks(p):
        return p.percolates()

    args = sys.argv[1:]

    if not args:
        print('usage: [-T] n')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    t = 1
    if args[0] == '-T':
        t = int(args[1])
        del args[0:2]

    if not args[0]:
        print('usage: [-T] n')
        sys.exit(1)
    else:
        n = int(args[0])

    my_sum = 0.0
    success = 0
    extra_steps = 0
    for i in range(t):
        p = Percolation(n)
        steps = 0
        while not p.percolates():
            p.open(random.randint(1, n), random.randint(1, n))
            steps += 1
        my_sum += p.number_of_open_sites / float(n * n)
        success += 1
        extra_steps += steps - p.number_of_open_sites
        print(p)

    print(check_leaks(p))

    print("Avarage p={}, extra steps {}".format(my_sum/success, extra_steps))

if __name__ == "__main__":
    main()

