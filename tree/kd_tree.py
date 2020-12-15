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
from helpers import timer
from red_black_tree import RedBlackTree
from red_black_tree import Node
from red_black_tree import NilNode


class KdTree(RedBlackTree):

    def contains(self, point):
        return self.__contains__(point)

    def __contains__(self, point):
        return self.search(point) is not None

    def range(self, rect):
        for p in self.inorder_walk():
            if rect.contains(p):
                yield p
    @timer
    def nearest(self, point):
        min_distance = math.inf
        result = None
        for p in self.inorder_walk():
            distance = point.distance_squared_to(p)
            if distance < min_distance:
                min_distance = distance
                result = p
        return result

    def add(self, key):
        self.insert(Node(key))

    def search(self, key, x=None):
        if x is None: x = self.root
        while x and x.key != key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def _insert_helper(self, z):
        y = NilNode.instance()
        x = self.root
        level = 0
        while x:
            y = x
            if level % 2 != 0: name = 'x'
            else: name = 'y'

            if getattr(z.key, name) < getattr(x.key, name):
                x = x.left
            else:
                x = x.right
            level += 1

        z.parent = y
        if not y:
            self.root = z
        else:
            if level % 2 == 0: name = 'x'
            else: name = 'y'

            if getattr(z.key, name) < getattr(y.key, name):
                y.left = z
            else:
                y.right = z

        self.size += 1
        print(self)

@timer
def main():
    def test(name, actual, expected):
        if actual != expected:
            print("Test {} FAILED get {} Expected {} ".format(name, actual, expected))
        else:
            print("Test {} OK".format(name))


if __name__ == "__main__":
    main()

