# Client. Write a client program Permutation.java that takes an integer k as a command-line argument; reads in a sequence
# of strings from standard input using StdIn.readString(); and prints exactly k of them, uniformly at random. Print each
# item from the sequence at most once.

from RandomizedQueue import RandomizedQueue
import sys


def main():
    if len(sys.argv) <= 1:
        print("Usage Permutation.py <number>")
        exit(0)

    num = int(sys.argv[1])

    r = RandomizedQueue()

    for line in sys.stdin:
        for item in line.split():
            r.enqueue(item)

    for el in range(num):
        print(r.dequeue())


if __name__ == "__main__":
    main()
