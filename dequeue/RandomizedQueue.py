# Randomized queue. A randomized queue is similar to a stack or queue, except that the item removed is chosen uniformly
# at random from items in the data structure. Create a generic data type RandomizedQueue that implements the following API:
#
# public class RandomizedQueue<Item> implements Iterable<Item> {
#    public RandomizedQueue()                 // construct an empty randomized queue
#    public boolean isEmpty()                 // is the randomized queue empty?
#    public int size()                        // return the number of items on the randomized queue
#    public void enqueue(Item item)           // add the item
#    public Item dequeue()                    // remove and return a random item
#    public Item sample()                     // return a random item (but do not remove it)
#    public Iterator<Item> iterator()         // return an independent iterator over items in random order
#    public static void main(String[] args)   // unit testing (optional)
# }
# Iterator.  Each iterator must return the items in uniformly random order. The order of two or more iterators to the
# same randomized queue must be mutually independent; each iterator must maintain its own random order.
#
# Corner cases.  Throw the specified exception for the following corner cases:
#
# Throw a java.lang.IllegalArgumentException if the client calls enqueue() with a null argument.
# Throw a java.util.NoSuchElementException if the client calls either sample() or dequeue() when the randomized queue is empty.
# Throw a java.util.NoSuchElementException if the client calls the next() method in the iterator when there are no more items to return.
# Throw a java.lang.UnsupportedOperationException if the client calls the remove() method in the iterator.
# Performance requirements.  Your randomized queue implementation must support each randomized queue operation (besides
# creating an iterator) in constant amortized time. That is, any sequence of m randomized queue operations (starting
# from an empty queue) must take at most cm steps in the worst case, for some constant c. A randomized queue containing
# n items must use at most 48n + 192 bytes of memory. Additionally, your iterator implementation must support operations
# next() and hasNext() in constant worst-case time; and construction in linear time; you may (and will need to)
# use a linear amount of extra memory per iterator.
#
import random


class RandomizedQueue(object):

    def __init__(self):
        self.__size = 0
        self.__list = [None]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self.__size

    def __double(self):
        self.__list = self.__list + [None]*len(self.__list)

    def __cut(self):
        self.__list = self.__list[:len(self.__list)//2]

    def enqueue(self, item):
        if len(self.__list) == self.size():
            self.__double()
        self.__list[self.size()] = item
        self.__size += 1

    def dequeue(self):
        if self.size() == 0:
            raise BaseException("No Such Element")

        sample = self.sample()
        self.__list[self.size()-1] = None
        self.__size -= 1
        if self.size()*4 <= len(self.__list):
            self.__cut()
        return sample

    def sample(self):
        index = random.randrange(0, stop=self.size())
        a = self.__list[index]
        self.__list[index] = self.__list[self.size()-1]
        self.__list[self.size()-1] = a
        return a

    def __iter__(self):
        self.__current = 0
        return self

    def __next__(self):
        if self.is_empty():
            raise StopIteration
        else:
            temp = self.dequeue()
            return temp

    def __str__(self):
        if self.is_empty():
            return "Empty list"
        return ",".join(self.__list[:self.size()])

    def __repr__(self):
        result = []
        for i in self.__list:
            if i is None:
                result.append('None')
            else:
                result.append(i)

        return "{}\n{}\nSize: {}\nList: {}\n".format(self.__class__.__name__, '-'*20, self.__size, ",".join(result))


def main():
    d = RandomizedQueue()
    print(repr(d))
    d.enqueue('q')
    d.enqueue('w')
    d.enqueue('e')
    d.enqueue('r')
    d.enqueue('t')
    print(repr(d))
    # print(d)
    #
    for i in d:
        print(i)
    # print(repr(d))


if __name__ == "__main__":
    main()
