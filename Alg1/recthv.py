# public class RectHV {
#    public    RectHV(double xmin, double ymin,      // construct the rectangle [xmin, xmax] x [ymin, ymax]
#                     double xmax, double ymax)      // throw a java.lang.IllegalArgumentException if (xmin > xmax) or
# (ymin > ymax)
#    public  double xmin()                           // minimum x-coordinate of rectangle
#    public  double ymin()                           // minimum y-coordinate of rectangle
#    public  double xmax()                           // maximum x-coordinate of rectangle
#    public  double ymax()                           // maximum y-coordinate of rectangle
#    public boolean contains(Point2D p)              // does this rectangle contain the point p
# (either inside or on boundary)?
#    public boolean intersects(RectHV that)          // does this rectangle intersect that rectangle
# (at one or more points)?
#    public  double distanceTo(Point2D p)            // Euclidean distance from point p to closest point in rectangle
#    public  double distanceSquaredTo(Point2D p)     // square of Euclidean distance from point p to closest
# point in rectangle
#    public boolean equals(Object that)              // does this rectangle equal that object?
#    public    void draw()                           // draw to standard draw
#    public  String toString()                       // string representation
from point2d import Point2D


class RectHV(object):
    def __init__(self, xmin, ymin, xmax, ymax):
        if xmin > xmax or ymin > ymax:
            raise ValueError("Min point is bigger that Max point")

        self.__xmin = xmin
        self.__ymin = ymin
        self.__xmax = xmax
        self.__ymax = ymax

    @property
    def xmin(self):
        return self.__xmin

    @property
    def ymin(self):
        return self.__ymin

    @property
    def xmax(self):
        return self.__xmax

    @property
    def ymax(self):
        return self.__ymax

    def contains(self, point):
        return self.xmin <= point.x <= self.xmax and self.ymin <= point.y <= self.ymax

    def intersects(self, rect):
        return self.contains(Point2D(rect.xmin, rect.ymin)) or \
               self.contains(Point2D(rect.xmin, rect.ymax)) or \
               self.contains(Point2D(rect.xmax, rect.ymin)) or \
               self.contains(Point2D(rect.xmax, rect.ymax)) or \
               rect.contains(Point2D(self.xmin, self.ymin)) or \
               rect.contains(Point2D(self.xmin, self.ymax)) or \
               rect.contains(Point2D(self.xmax, self.ymin)) or \
               rect.contains(Point2D(self.xmax, self.ymax)) or \
               (rect.xmin <= self.xmin <= rect.xmax and self.ymin <= rect.ymin <= self.xmax) or \
               (self.xmin <= rect.xmin <= self.xmax and rect.ymin <= self.ymin <= rect.xmax)

    def __find_intersection_point(self, point):
        if point.x <= self.xmin:
            x = self.xmin
        elif point.x >= self.xmax:
            x = self.xmax
        else:
            x = point.x

        if point.y <= self.ymin:
            y = self.ymin
        elif point.y >= self.ymax:
            y = self.ymax
        else:
            y = point.y

        return Point2D(x, y)

    def distance_to(self, point):
        if self.contains(point):
            return 0
        else:
            return point.distance_to(self.__find_intersection_point(point))

    def distance_squared_to(self, point):
        if self.contains(point):
            return 0
        else:
            return point.distance_squared_to(self.__find_intersection_point(point))

    def equals(self, that):
        return self is that

    def __eq__(self, other):
        return self.xmin == other.xmin and \
               self.ymin == other.ymin and \
               self.xmax == other.xmax and \
               self.ymax == other.ymax

    def __str__(self):
        return "{},{} {},{}".format(self.xmin, self.ymin, self.xmax, self.ymax)

    def __repr__(self):
        return "Min:{},{} \nMax:{},{}\n".format(self.xmin, self.ymin, self.xmax, self.ymax)


def main():
    def test(name, actual, expected):
        if actual != expected:
            print("Test {} FAILED get {} Expected {} ".format(name, actual, expected))
        else:
            print("Test {} OK".format(name))

    r = RectHV(0, 0, 4, 4)
    r1 = RectHV(0, 0, 4, 4)

    try:
        r2 = RectHV(4, 4, 0, 9)
    except Exception as e:
        test("Constructor test", type(e), ValueError)
    else:
        test("Constructor test", True, False)

    r3 = RectHV(2, 2, 6, 6)
    r4 = RectHV(2, 2, 6, 3)
    r5 = RectHV(4, 0, 6, 4)
    r6 = RectHV(5, 5, 6, 6)

    p = Point2D(0.5, 3.5)
    p1 = Point2D(4.5, 3.5)
    p2 = Point2D(0, 3.5)
    p3 = Point2D(4, 3.5)
    p4 = Point2D(2.5, 0)
    p5 = Point2D(2.5, 4)
    p6 = Point2D(7, 8)

    print(r)
    print(repr(r))

    test("r({}) = r1({})".format(r, r1), r == r1, True)

    test("r({}) contains p({})".format(r, p), r.contains(p), True)
    test("r({}) NOT contains p({})".format(r, p), r.contains(p1), False)
    test("r({}) contains p({})".format(r, p), r.contains(p2), True)
    test("r({}) contains p({})".format(r, p), r.contains(p3), True)
    test("r({}) contains p({})".format(r, p), r.contains(p4), True)
    test("r({}) contains p({})".format(r, p), r.contains(p5), True)

    test("r({}) distance to p({}) 0".format(r, p), r.distance_to(p), 0)
    test("r({}) square distance to p({}) 0".format(r, p), r.distance_squared_to(p), 0)
    test("r({}) distance to p({})".format(r, p1), r.distance_to(p1), p1.distance_to(Point2D(4, 3.5)))
    test("r({}) squared distance to p({})".format(r, p1), r.distance_squared_to(p1), p1.distance_squared_to(Point2D(4, 3.5)))
    test("r({}) distance to p({})".format(r, p6), r.distance_to(p6), 5)
    test("r({}) squared distance to p({})".format(r, p6), r.distance_squared_to(p6), 25)

    test("r({}) intersects r({})".format(r, r1), r.intersects(r1), True)
    test("r({}) intersects r({})".format(r, r3), r.intersects(r3), True)
    test("r({}) intersects r({})".format(r, r4), r.intersects(r4), True)
    test("r({}) intersects r({})".format(r, r5), r.intersects(r5), True)
    test("r({}) NOT intersects r({})".format(r, r6), r.intersects(r6), False)

    test("r({}) equal r({})".format(r, r), r.equals(r), True)
    test("r({}) not equal r1({})".format(r, r1), r.equals(r1), False)


if __name__ == "__main__":
    main()