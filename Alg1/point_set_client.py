from point2d import Point2D
from recthv import RectHV
from helpers import timer
from point_set import PointSET
from kd_tree_v2 import KdTree
from red_black_tree import RedBlackTree

@timer
def main():
    def test(name, actual, expected):
        if actual != expected:
            print("Test {} FAILED get {} Expected {} ".format(name, actual, expected))
        else:
            print("Test {} OK".format(name))

    @timer
    def load(path):
        fd = open(path, "r")
        result = KdTree()
        # result = PointSET()
        for line in [i.strip() for i in fd]:
            if line:
                x, y = [float(chunk) for chunk in line.split()]
                result.insert(Point2D(x, y))
        return result

    @timer
    def get_range(r):
        count = 0
        for p in point_set.range(r):
            # print(p)
            count += 1
        return count

    point_set = load("data/kdtree/input1M.txt")
    # print(point_set)
    # print("Nearest " + str(point_set.nearest(Point2D(0.5, 0.5))))
    print("Contains {} {}".format(Point2D(0.5, 0.5), point_set.contains(Point2D(0.5, 0.5))))
    print("Contains {} {}".format(Point2D(0.144, 0.179), point_set.contains(Point2D(0.144, 0.179))))

    r = RectHV(0.3, 0.3, 0.4, 0.4)
    print("In range of {} - {}".format(r, get_range(r)))


if __name__ == "__main__":
    main()

# 100K
# Get_Range execution time is 0.17269158363342285
# In range of 0.36,0.36 0.4,0.4 - 154
# Get_Range execution time is 0.00264739990234375
# In range of 0.36,0.36 0.4,0.4 - 154

# 400K
# Get_Range execution time is 0.7040400505065918
# In range of 0.36,0.36 0.4,0.4 - 627
# Get_Range execution time is 0.011573553085327148
# In range of 0.36,0.36 0.4,0.4 - 627

# 1M
# Get_Range execution time is 1.8137571811676025
# In range of 0.36,0.36 0.4,0.4 - 1665
# Get_Range execution time is 0.01920795440673828
# In range of 0.36,0.36 0.4,0.4 - 1665

# 10K
# Nearest execution time is 0.01821732521057129
# Nearest 0.50349,0.498866
# Nearest execution time is 0.0001728534698486328
# Nearest 0.50349,0.498866

# 100k
# Nearest execution time is 0.2183701992034912
# Nearest 0.498659,0.500257
# Nearest execution time is 0.0002713203430175781
# Nearest 0.498659,0.500257

# 400K
# Nearest execution time is 0.919940710067749
# Nearest 0.500512,0.500298
# Nearest execution time is 0.00030303001403808594
# Nearest 0.500512,0.500298

# 1M
# nearest execution time 1.4053864479064941
# Nearest 0.499759,0.499591
# Nearest execution time is 0.0005867481231689453
# Nearest 0.499759,0.499591

# For 1M
# Brute-force

# Sorted array
# load execution time 155.1580367088318
# nearest execution time 1.4053864479064941
# Nearest 0.499759,0.499591
# get_range execution time 1.0171232223510742
# In range of 0.3,0.3 0.6,0.6 - 90064
# main execution time 158.15877532958984

# rb_tree V1
# Load execution time is 60.962353467941284
# Nearest execution time is 2.5447070598602295
# Nearest 0.499759,0.499591
# Get_Range execution time is 2.3192403316497803
# In range of 0.3,0.3 0.6,0.6 - 90064
# Main execution time is 65.82642340660095

# red_black_tree V2
# Load execution time is 36.94288897514343
# Nearest execution time is 2.4153802394866943
# Nearest 0.499759,0.499591
# Get_Range execution time is 1.960174560546875
# In range of 0.3,0.3 0.6,0.6 - 90064
# Main execution time is 41.31856846809387
