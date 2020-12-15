# Dequeue. A double-ended queue or deque (pronounced “deck”) is a generalization of a stack and a queue that supports adding
# and removing items from either the front or the back of the data structure. Create a generic data type Deque that implements the following API:
#
# public class Deque<Item> implements Iterable<Item> {
#    public Deque()                           // construct an empty deque
#    public boolean isEmpty()                 // is the deque empty?
#    public int size()                        // return the number of items on the deque
#    public void addFirst(Item item)          // add the item to the front
#    public void addLast(Item item)           // add the item to the end
#    public Item removeFirst()                // remove and return the item from the front
#    public Item removeLast()                 // remove and return the item from the end
#    public Iterator<Item> iterator()         // return an iterator over items in order from front to end
#    public static void main(String[] args)   // unit testing (optional)
# }
# Corner cases.  Throw the specified exception for the following corner cases:
#
# Throw a java.lang.IllegalArgumentException if the client calls either addFirst() or addLast() with a null argument.
# Throw a java.util.NoSuchElementException if the client calls either removeFirst() or removeLast when the deque is empty.
# Throw a java.util.NoSuchElementException if the client calls the next() method in the iterator when there are no more items to return.
# Throw a java.lang.UnsupportedOperationException if the client calls the remove() method in the iterator.
# Performance requirements.  Your deque implementation must support each deque operation (including construction) in
# constant worst-case time. A deque containing n items must use at most 48n + 192 bytes of memory and use space proportional
# to the number of items currently in the deque. Additionally, your iterator implementation must support each
# operation (including construction) in constant worst-case time.


class Deque(object):

    class Node:
        def __init__(self, val, prev=None, next_node=None):
            self.val = val
            self.next = next_node
            self.prev = prev

        def __str__(self):
            return str(self.val)

    def __init__(self):
        self.__first = self.Node(None)
        self.__last = self.Node(None)
        self.__first.next = self.__last
        self.__last.prev = self.__first

        self.__size = 0
        self.__current = None

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self.__size

    def add_first(self, item):
        item = self.Node(item, prev=self.__first, next_node=self.__first.next)
        self.__first.next = item
        item.next.prev = item
        self.__size += 1

    def add_last(self, item):
        item = self.Node(item, prev=self.__last.prev, next_node=self.__last)
        self.__last.prev = item
        item.prev.next = item
        self.__size += 1

    def remove_first(self):
        if self.__size == 0:
            raise BaseException("No Such Element")

        temp = self.__first.next
        self.__first.next.next.prev = self.__first
        self.__first.next = self.__first.next.next
        self.__size -= 1
        return temp.val

    def remove_last(self):
        if self.__size == 0:
            raise BaseException("No Such Element")

        temp = self.__last.prev
        self.__last.prev.prev.next = self.__last
        self.__last.prev = self.__last.prev.prev
        self.__size -= 1

        return temp.val

    def __len__(self):
        return self.size()

    def __iter__(self):
        self.__current = self.__first.next
        return self

    def __next__(self):
        if self.__current is self.__last:
            raise StopIteration
        else:
            temp = self.__current
            self.__current = self.__current.next
            return temp.val

    def __str__(self):
        if self.__size == 0:
            return "Empty list"

        result_list = []
        for item in self:
            result_list.append(str(item))

        return ",".join(result_list)

    def __repr__(self):
        if self.__size == 0:
            return "\nEmpty list"

        current = self.__first
        result_list = []
        while True:
            result_list.append(str(current))
            if current.next is None:
                break
            else:
                current = current.next
        return "\nSize: {}\nList: {}\nFirst: {}\nLast: {}".format(self.__size, ",".join(result_list), self.__first, self.__last)


def main():
    def test(name, actual, expected):
        if actual != expected:
            print("Test {} FAILED get {} Expected {} ".format(name, actual, expected))
        else:
            print("Test {} OK".format(name))

    d = Deque()
    print(d)

    d.add_last('2')
    d.add_last('3')
    d.add_last('5')
    d.add_last('7')
    print(repr(d))
    print(d.remove_last())
    print(d.remove_first())
    print(d.remove_first())
    print(d.remove_first())

    # print(d)
    #
    # for i in d:
    #     print(i)

if __name__ == "__main__":
    main()
