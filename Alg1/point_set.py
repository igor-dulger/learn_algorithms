# public class PointSET {
#    public         PointSET()                               // construct an empty set of points
#    public           boolean isEmpty()                      // is the set empty?
#    public               int size()                         // number of points in the set
#    public              void insert(Point2D p)              // add the point to the set
# (if it is not already in the set)
#    public           boolean contains(Point2D p)            // does the set contain point p?
#    public              void draw()                         // draw all points to standard draw
#    public Iterable<Point2D> range(RectHV rect)             // all points that are inside the rectangle
# (or on the boundary)
#    public           Point2D nearest(Point2D p)             // a nearest neighbor in the set to point p;
# null if the set is empty
#
#    public static void main(String[] args)                  // unit testing of the methods (optional)
# }
#
# Implementation requirements.  You must use either SET or java.util.TreeSet; do not implement your own red–black BST.
#
# Corner cases.  Throw a java.lang.IllegalArgumentException if any argument is null. Performance requirements.
# Your implementation should support insert() and contains() in time proportional to the logarithm of the number
# of points in the set in the worst case; it should support nearest() and range() in time proportional to the number
# of points in the set.

from point2d import Point2D
from recthv import RectHV
from red_black_tree import RedBlackTree
from helpers import timer
import math


class PointSET(object):
    def __init__(self):
        self.__set = RedBlackTree()

    def is_empty(self):
        return self.__set.is_empty()

    def size(self):
        return self.__set.size()

    def insert(self, point):
        self.__set.add(point)

    add = insert

    @timer
    def contains(self, point):
        return self.__contains__(point)

    def __contains__(self, point):
        return bool(self.__set.search(point))

    def range(self, rect):
        for p in self.__set.inorder_walk():
            if rect.contains(p):
                yield p
    @timer
    def nearest(self, point):
        min_distance = math.inf
        result = None
        for p in self.__set.inorder_walk():
            distance = point.distance_squared_to(p)
            if distance < min_distance:
                min_distance = distance
                result = p
        return result

    def __len__(self):
        return len(self.__set)

    def __str__(self):
        return str(self.__set)

@timer
def main():
    def test(name, actual, expected):
        if actual != expected:
            print("Test {} FAILED get {} Expected {} ".format(name, actual, expected))
        else:
            print("Test {} OK".format(name))


if __name__ == "__main__":
    main()

