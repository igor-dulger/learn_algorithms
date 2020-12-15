# Line segment data type. To represent line segments in the plane, use the data type LineSegment.java,
# which has the following API:
#
# public class LineSegment {
#    public LineSegment(Point p, Point q)        // constructs the line segment between points p and q
#    public   void draw()                        // draws this line segment
#    public String toString()                    // string representation
# }
from Point import Point


class LineSegment(object):
    def __init__(self, p, q):
        if type(p) != Point:
            error = "Invalid argument [p] type [{}] Point expected".format(p.__class__.__name__)
            raise TypeError(error)
        if type(q) != Point:
            error = "Invalid argument [q] type [{}] Point expected".format(q.__class__.__name__)
            raise TypeError(error)
        self.p = p
        self.q = q

    def draw(self):
        pass

    def __str__(self):
        return "p:{} -> q:{}".format(str(self.p), str(self.q))


def main():
    def test(name, actual, expected):
        if actual != expected:
            print("Test {} FAILED get {} Expected {} ".format(name, actual, expected))
        else:
            print("Test {} OK".format(name))

    p = Point(1, 2)
    q = Point(1, 3)
    l = LineSegment(p, q)
    print(l)


if __name__ == "__main__":
    main()

