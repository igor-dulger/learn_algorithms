# Write a program FastCollinearPoints.java that implements this algorithm.
#
# public class FastCollinearPoints {
#    public FastCollinearPoints(Point[] points)     // finds all line segments containing 4 or more points
#    public           int numberOfSegments()        // the number of line segments
#    public LineSegment[] segments()                // the line segments
# }
# The method segments() should include each maximal line segment containing 4 (or more) points exactly once.
# For example, if 5 points appear on a line segment in the order p→q→r→s→t, then do not include
# the subsegments p→s or q→t.
#
# Corner cases. Throw a java.lang.IllegalArgumentException if the argument to the constructor is null, if any point
# in the array is null, or if the argument to the constructor contains a repeated point.
#
# Performance requirement. The order of growth of the running time of your program should be n2 log n in the worst
# case and it should use space proportional to n plus the number of line segments returned. FastCollinearPoints
# should work properly even if the input has 5 or more collinear points.

from Point import Point
from CollinearPoints import CollinearPoints
from LineSegment import LineSegment
import logging
from helpers import timer

logger = logging.getLogger('FastCollinearPoints')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logger.addHandler(ch)


class FastCollinearPoints(CollinearPoints):
    @timer
    def find_segments(self):
        lines = {i: [] for i in self.points}

        def add_segment(i, start, line_size, points, slope):
            lines[self.points[i]].append(slope)
            for p_index in range(start, start+line_size):
                lines[points[p_index]].append(slope)
            self.segments.append(LineSegment(self.points[i], points[start+line_size-1]))

        for i in range(len(self.points)):
            logger.debug("> {} <".format(str(self.points[i])))
            points = sorted(self.points[i+1:], key=self.points[i].slope_index())
            last_slope = None
            start = 0
            line_size = 0
            for j in range(len(points)):
                slope = self.points[i].slope_to(points[j])

                if lines.get(points[j]) and slope in lines[points[j]]:
                    continue

                if last_slope == slope or last_slope is None:
                    line_size += 1
                else:
                    if line_size >= 3:
                        add_segment(i, start, line_size, points, last_slope)
                    start = j
                    line_size = 1

                last_slope = slope
                logger.debug("j:{} {} {} range:{} {}".format(j, str(points[j]), self.points[i].slope_to(points[j]), start, line_size))
            if line_size >= 3:
                add_segment(i, start, line_size, points, last_slope)


def main():
    def test(name, actual, expected):
        if actual != expected:
            print("Test {} FAILED get {} Expected {} ".format(name, actual, expected))
        else:
            print("Test {} OK".format(name))

    fd = open("data/collinear/rs1423.txt", "r")
    fd.readline()
    point_list = []
    for line in [i.strip() for i in fd]:
        if line:
            x, y = [int(chunk) for chunk in line.split()]
            point_list.append(Point(x, y))

    bcp = FastCollinearPoints(point_list)
    logger.info(bcp)

if __name__ == "__main__":
    main()

# 100 <class 'str'>: find_segments execution time 0.09665179252624512
# 200 <class 'str'>: find_segments execution time 0.35279202461242676
# 400 <class 'str'>: find_segments execution time 1.4272582530975342
# 1000 <class 'str'>: find_segments execution time 8.52099084854126
# 2000 <class 'str'>: find_segments execution time 36.51841402053833
# 3000 <class 'str'>: find_segments execution time 76.62577152252197