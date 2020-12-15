# Point data type. Create an immutable data type Point that represents a point in the plane by implementing the
# following API:
#
# public class Point implements Comparable<Point> {
#    public Point(int x, int y)                         // constructs the point (x, y)
#
#    public   void draw()                               // draws this point
#    public   void drawTo(Point that)                   // draws the line segment from this point to that point
#    public String toString()                           // string representation
#
#    public               int compareTo(Point that)     // compare two points by y-coordinates, breaking ties by x-
# coordinates
#    public            double slopeTo(Point that)       // the slope between this point and that point
#    public Comparator<Point> slopeOrder()              // compare two points by slopes they make with this point
# }
# To get started, use the data type Point.java, which implements the constructor and the draw(), drawTo(), and
# toString() methods. Your job is to add the following components.
# The compareTo() method should compare points by their y-coordinates, breaking ties by their x-coordinates. Formally,
# the invoking point (x0, y0) is less than the argument point (x1, y1) if and only if either y0 < y1 or if y0 = y1
# and x0 < x1.
# The slopeTo() method should return the slope between the invoking point (x0, y0) and the argument point
# (x1, y1), which is given by the formula (y1 − y0) / (x1 − x0). Treat the slope of a horizontal line segment as
# positive zero; treat the slope of a vertical line segment as positive infinity; treat the slope of a degenerate line
# segment (between a point and itself) as negative infinity.
# The slopeOrder() method should return a comparator that compares its two argument points by the slopes they make with
# the invoking point (x0, y0). Formally, the point (x1, y1) is less than the point (x2, y2) if and only if the slope
# (y1 − y0) / (x1 − x0) is less than the slope (y2 − y0) / (x2 − x0). Treat horizontal, vertical, and degenerate
# line segments as in the slopeTo() method.

import math
from basicpoint import BasicPoint


class Point(BasicPoint):

    def slope_to(self, point):
        if point.y == self.y:
            return 0
        elif point.x == self.x and point.y > self.y:
            return math.inf
        elif point.x == self.x and point.y < self.y:
            return -math.inf
        else:
            return (point.y - self.y) / (point.x - self.x)

    def slope_order(self):
        def comparator(point1, point2):
            a = self.slope_to(point1)
            b = self.slope_to(point2)
            if a < b:
                return -1
            elif a > b:
                return 1
            else:
                return 0
        return comparator

    def slope_index(self):
        def index(point):
            return self.slope_to(point)
        return index


def main():
    def test(name, actual, expected):
        if actual != expected:
            print("Test {} FAILED get {} Expected {} ".format(name, actual, expected))
        else:
            print("Test {} OK".format(name))

    p = Point(1, 2)
    p1 = Point(1, 3)
    p2 = Point(1, 1)
    p4 = Point(0, 2)
    p5 = Point(2, 2)
    p3 = Point(1, 2)
    p6 = Point(3, 3)
    p7 = Point(0, 0)
    p8 = Point(1, 4)
    p9 = Point(1, 0)
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

    test("Slope {} {}".format(p, p1), p.slope_to(p1), math.inf)
    test("Slope {} {}".format(p, p2), p.slope_to(p2), -math.inf)
    test("Slope {} {}".format(p, p4), p.slope_to(p4), 0)
    test("Slope {} {}".format(p, p3), p.slope_to(p3), 0)
    test("Slope {} {}".format(p, p6), p.slope_to(p6), 0.5)
    test("Slope {} {}".format(p, p7), p.slope_to(p7), 2)

    comparator = p.slope_order()
    test("Slope cmp {} {}".format(p6, p7), comparator(p6, p7), -1)
    test("Slope cmp {} {}".format(p7, p6), comparator(p7, p6), 1)
    test("Slope cmp {} {}".format(p1, p8), comparator(p1, p8), 0)
    test("Slope cmp {} {}".format(p2, p9), comparator(p2, p9), 0)

if __name__ == "__main__":
    main()
