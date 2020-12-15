import math


class PriorityQueue(object):
    def __init__(self):
        self.__heap = []
        self.__size = 0

    def __sink(self, k):
        while 2*k <= self.__size:
            j = 2*k
            # find larger child
            if j < self.__size and self.less(j, j+1):
                j += 1
            if self.less(j, k):
                break

            self.__exchange(k, j)
            k = j

    def __swim(self, k):
        while k > 1:
            j = k // 2
            if self.less(k, j):
                break
            self.__exchange(k, j)
            k = j

    def __exchange(self, i, j):
        t = self._heap[i-1]
        self._heap[i-1] = self._heap[j-1]
        self._heap[j-1] = t

    @property
    def _heap(self):
        return self.__heap

    @_heap.setter
    def _heap(self, heap):
        self.__heap = heap

    def is_empty(self):
        return self.__size == 0

    def pop(self):
        if self.is_empty():
            raise BaseException("Priority queue is empty")

        self.__exchange(1, self.__size)
        result = self._heap.pop()
        self.__size -= 1
        self.__sink(1)
        return result

    def push(self, item):
        self._heap.append(item)
        self.__size += 1
        self.__swim(self.__size)

    def less(self, i, j):
        pass

    def __repr__(self):
        return ", ".join(str(i)for i in self._heap)

    def __str__(self):
        depth = int(math.ceil(math.log(self.__size, 2)))+1
        result = [""]*depth
        size = 1
        level = 0
        level_size = 0
        for i in range(self.__size):
            result[level] += " "*int((math.pow(2, depth)-math.pow(2, level)) / (math.pow(2, level)+1)) + str(self._heap[i])
            level_size += 1
            if level_size >= size:
                size *= 2
                level += 1
                level_size = 0
        return "\n".join(result)


class IndexPriorityQueue(object):
    def __init__(self):
        self.__mapping = {}
        self.__index_position = {}
        self.__heap = []
        self.__size = 0

    def _sink(self, k):
        while 2*k <= self.__size:
            j = 2*k
            # find larger child
            if j < self.__size and self.less(j, j+1):
                j += 1
            if self.less(j, k):
                break

            self.__exchange(k, j)
            k = j

    def _swim(self, k):
        while k > 1:
            j = k // 2
            if self.less(k, j):
                break
            self.__exchange(k, j)
            k = j

    def __exchange(self, i, j):
        t = self._heap[i-1]

        self.__index_position[t] = j
        self.__index_position[self._heap[j-1]] = i

        self._heap[i-1] = self._heap[j-1]
        self._heap[j-1] = t

    @property
    def _mapping(self):
        return self.__mapping

    @_mapping.setter
    def _mapping(self, mapping):
        self.__mapping = mapping

    @property
    def _index_position(self):
        return self.__index_position

    @_index_position.setter
    def _index_position(self, position):
        self.__index_position = position

    @property
    def _heap(self):
        return self.__heap

    @_heap.setter
    def _heap(self, heap):
        self.__heap = heap

    def is_empty(self):
        return self.__size == 0

    def __contains__(self, item):
        return item in self.__mapping

    def pop(self):
        if self.is_empty():
            raise BaseException("Priority queue is empty")

        self.__exchange(1, self.__size)
        result = self._heap.pop()
        del(self.__mapping[result])
        del(self.__index_position[result])
        self.__size -= 1
        self._sink(1)
        return result

    def push(self, index, weight):
        self.__size += 1
        self.__mapping[index] = weight
        self._heap.append(index)
        self.__index_position[index] = self.__size
        self._swim(self.__size)

    def less(self, i, j):
        pass

    def __repr__(self):
        return ", ".join(str(i) for i in self._heap)

    def __str__(self):
        depth = int(math.ceil(math.log(self.__size, 2)))+1
        result = [""]*depth
        size = 1
        level = 0
        level_size = 0
        for i in range(self.__size):
            result[level] += " "*int((math.pow(2, depth)-math.pow(2, level)) / (math.pow(2, level)+1)) + str(self._heap[i])
            level_size += 1
            if level_size >= size:
                size *= 2
                level += 1
                level_size = 0
        return "\n".join(result) + " \nMapping: "+str(self.__mapping) + " \nIndexes: "+str(self.__index_position)


class MinPriorityQueue(PriorityQueue):
    def less(self, i, j):
        return self._heap[i-1] > self._heap[j-1]


class MaxPriorityQueue(PriorityQueue):
    def less(self, i, j):
        return self._heap[i-1] < self._heap[j-1]


class MinIndexPriorityQueue(IndexPriorityQueue):
    def less(self, i, j):
        return self._mapping[self._heap[i-1]] > self._mapping[self._heap[j-1]]

    def decrease_key(self, key, value):
        self._mapping[key] = value
        self._swim(self._index_position[key])


class MaxIndexPriorityQueue(IndexPriorityQueue):
    def less(self, i, j):
        return self._mapping[self._heap[i-1]] > self._mapping[self._heap[j-1]]

    def increase_key(self, key, value):
        self._mapping[key] = value
        self._swim(self._index_position[key])


def main():
    pq = MaxPriorityQueue()
    # pq = MinPriorityQueue()

    for i in range(42):
        pq.push(i)
    print(pq)

    for i in range(21):
        pq.pop()
    print(pq)

    print(repr(pq))


if __name__ == "__main__":
    main()


