# Brute force. Write a program BruteCollinearPoints.java that examines 4 points at a time and checks whether they all
# lie on the same line segment, returning all such line segments. To check whether the 4 points p, q, r, and s are
# collinear, check whether the three slopes between p and q, between p and r, and between p and s are all equal.
#
# public class BruteCollinearPoints {
#    public BruteCollinearPoints(Point[] points)    // finds all line segments containing 4 points
#    public           int numberOfSegments()        // the number of line segments
#    public LineSegment[] segments()                // the line segments
# }
# The method segments() should include each line segment containing 4 points exactly once. If 4 points appear on a
# line segment in the order p→q→r→s, then you should include either the line segment p→s or s→p (but not both) and you
# should not include subsegments such as p→r or q→r. For simplicity, we will not supply any input
# to BruteCollinearPoints that has 5 or more collinear points.
#
# Corner cases. Throw a java.lang.IllegalArgumentException if the argument to the constructor is null, if any point
# in the array is null, or if the argument to the constructor contains a repeated point.
#
# Performance requirement. The order of growth of the running time of your program should be n4 in the worst case and
# it should use space proportional to n plus the number of line segments returned.

from Point import Point
from CollinearPoints import CollinearPoints
from LineSegment import LineSegment
from deque import Deque
import logging

logger = logging.getLogger('BruteCollinearPoints')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)


class BruteCollinearPoints(CollinearPoints):
    def find_segments(self):
        for i in range(len(self.points)):
            logger.debug(str(self.points[i]) + "-------------------------------------")
            for j in range(i+1, len(self.points)):
                stack = Deque()
                stack.add_last(i)
                stack.add_last(j)
                slope1 = self.points[i].slope_to(self.points[j])
                logger.debug(str(self.points[i])+", "+str(self.points[j])+","+str(slope1))
                for k in range(j+1, len(self.points)):
                    slope2 = self.points[i].slope_to(self.points[k])
                    if slope1 == slope2:
                        stack.add_last(k)
                        logger.debug("{} {} {} Points:{}".format(self.points[k], slope1, slope2, stack.size()))
                if stack.size() >= 4:
                    self.segments.append(LineSegment(self.points[i], self.points[stack.remove_last()]))



def main():
    def test(name, actual, expected):
        if actual != expected:
            print("Test {} FAILED get {} Expected {} ".format(name, actual, expected))
        else:
            print("Test {} OK".format(name))

    fd = open("data/collinear/input10.txt", "r")
    fd.readline()
    point_list = []
    for line in [i.strip() for i in fd]:
        if line:
            x, y = [int(chunk) for chunk in line.split()]
            point_list.append(Point(x, y))

    bcp = BruteCollinearPoints(point_list)
    print(bcp)

if __name__ == "__main__":
    main()
