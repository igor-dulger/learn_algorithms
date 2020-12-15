# public class Point2D implements Comparable<Point2D> {
#    public Point2D(double x, double y)              // construct the point (x, y)
#    public  double x()                              // x-coordinate
#    public  double y()                              // y-coordinate
#    public  double distanceTo(Point2D that)         // Euclidean distance between two points
#    public  double distanceSquaredTo(Point2D that)  // square of Euclidean distance between two points
#    public     int compareTo(Point2D that)          // for use in an ordered symbol table
#    public boolean equals(Object that)              // does this point equal that object?
#    public    void draw()                           // draw to standard draw
#    public  String toString()                       // string representation
import math
from basicpoint import BasicPoint


class Point2D(BasicPoint):
    def distance_to(self, point):
        if isinstance(point, Point2D):
            return math.sqrt(self.distance_squared_to(point))

    def distance_squared_to(self, point):
        if isinstance(point, Point2D):
            return pow(self.x - point.x, 2) + pow(self.y - point.y, 2)
        else:
            return False

    def equals(self, that):
        return self is that

    # def compare_to(self, point):
    #     if type(self) == type(point):
    #         if self.y < point.y:
    #             return -1
    #         elif self.y > point.y:
    #             return 1
    #         elif self.x < point.x:
    #             return -1
    #         elif self.x > point.x:
    #             return 1
    #         else:
    #             return 0
    #     else:
    #         raise ValueError("Can't compare {} and {}".format(self.__class__.__name__, point.__class__.__name__))

    def compare_to(self, point, axes=None):
        if type(self) != type(point):
            raise ValueError("Can't compare {} and {}".format(self.__class__.__name__, point.__class__.__name__))

        if axes == 'x':
            axes_a, axes_b = 'x', 'y'
        else:
            axes_a, axes_b = 'y', 'x'

        if getattr(self, axes_a) < getattr(point, axes_a):
            return -1
        elif getattr(self, axes_a) > getattr(point, axes_a):
            return 1
        if getattr(self, axes_b) < getattr(point, axes_b):
            return -1
        elif getattr(self, axes_b) > getattr(point, axes_b):
            return 1
        else:
            return 0


def main():
    def test(name, actual, expected):
        if actual != expected:
            print("Test {} FAILED get {} Expected {} ".format(name, actual, expected))
        else:
            print("Test {} OK".format(name))

    p = Point2D(1, 2)
    p1 = Point2D(1, 3)
    p2 = Point2D(1, 1)
    p4 = Point2D(0, 2)
    p5 = Point2D(2, 2)
    p3 = Point2D(1, 2)
    p6 = Point2D(3, 3)
    p7 = Point2D(0, 0)
    p8 = Point2D(1, 4)
    p9 = Point2D(1, 0)
    p10 = Point2D(0, 0)
    p11 = Point2D(3, 4)

    print(p)
    test("{} < {}".format(p, p1), p < p1, True)
    test("{} > {}".format(p, p2), p > p2, True)
    test("{} = {}".format(p, p3), p == p3, True)
    test("{} > {}".format(p, p4), p > p4, True)
    test("{} < {}".format(p, p5), p < p5, True)
    test("{} <= {}".format(p, p3), p <= p3, True)
    test("{} <= {}".format(p, p1), p <= p1, True)
    test("{} >= {}".format(p, p3), p >= p3, True)
    test("{} >= {}".format(p, p2), p >= p2, True)
    test("{} != {}".format(p, p1), p != p1, True)
    test("{} < {}".format(p, p6), p < p6, True)
    test("{} > {}".format(p, p7), p > p7, True)

    test("Distance {} {}".format(p10, p11), p10.distance_to(p11), 5)
    test("Squared distance {} {}".format(p10, p11), p10.distance_squared_to(p11), 25)

    test("Equals {} {}".format(p, p), p.equals(p), True)

if __name__ == "__main__":
    main()