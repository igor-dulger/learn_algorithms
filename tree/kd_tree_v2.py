from helpers import timer
from point2d import Point2D
from recthv import RectHV


class KdTree(object):

    class Node:
        def __init__(self, point, recv):
            self.point = point
            self.left = None
            self.right = None
            self.recv = recv

        def __str__(self, level=0, indent="   ", axes='x'):
            s = level * indent + "{} {} r={}".format(self.point, axes, self.recv)
            if axes == 'y':
                axes = "x"
            else:
                axes = "y"

            if self.left:
                s = s + "\nl" + self.left.__str__(level + 1, indent, axes)
            if self.right:
                s = s + "\nr" + self.right.__str__(level + 1, indent, axes)
            return s

        def __bool__(self):
            return True

    def __init__(self):
        self.__size = 0
        self.root = None

    def insert(self, point):
        self.root = self.__put(self.root, point, 'x', RectHV(0, 0, 1, 1))
        self.__size += 1

    def is_empty(self):
        return self.__size == 0

    def __range(self, h, rect, axes):
        if rect.contains(h.point):
            yield h.point
        if h.left is not None and rect.intersects(h.left.recv):
            yield from self.__range(h.left, rect, self.__invert_axes(axes))
        if h.right is not None and rect.intersects(h.right.recv):
            yield from self.__range(h.right, rect, self.__invert_axes(axes))

    # def __rangeQ(self, h, rect, axes):
    #     if rect.contains(h.point):
    #         yield h.point
    #
    #     if axes == 'x':
    #         intersects = rect.intersects(RectHV(h.point.x, h.recv.ymin, h.point.x, h.recv.ymax))
    #     else:
    #         intersects = rect.intersects(RectHV(h.recv.xmin, h.point.y, h.recv.xmax, h.point.y))
    #
    #     if not intersects:
    #         cmp = Point2D(rect.xmin, rect.ymin).compare_to(h.point, axes)
    #
    #     if h.left is not None and (intersects or cmp < 0):
    #         yield from self.__range(h.left, rect, self.__invert_axes(axes))
    #     if h.right is not None and (intersects or cmp > 0):
    #         yield from self.__range(h.right, rect, self.__invert_axes(axes))

    def range(self, rect):
        return self.__range(self.root, rect, 'x')

    def __nearest(self, h, point, axes, nearest):
        if h is None:
            return nearest

        if nearest.distance_squared_to(point) > h.point.distance_squared_to(point):
            nearest = h.point
        cmp = point.compare_to(h.point, axes)
        if cmp < 0:
            nearest = self.__nearest(h.left, point, self.__invert_axes(axes), nearest)
            if h.right is not None and h.right.recv.distance_squared_to(point) <= nearest.distance_squared_to(point):
                nearest = self.__nearest(h.right, point, self.__invert_axes(axes), nearest)
        elif cmp > 0:
            nearest = self.__nearest(h.right, point, self.__invert_axes(axes), nearest)
            if h.left is not None and h.left.recv.distance_squared_to(point) <= nearest.distance_squared_to(point):
                nearest = self.__nearest(h.left, point, self.__invert_axes(axes), nearest)
        elif cmp == 0:
            return h.point
        return nearest

    @timer
    def nearest(self, point):
        return self.__nearest(self.root, point, 'x', self.root.point)

    @timer
    def contains(self, point):
        x = self.root
        axes = 'y'
        while x is not None:
            cmp = point.compare_to(x.point, axes)
            if cmp < 0:
                x = x.left
            elif cmp > 0:
                x = x.right
            elif cmp == 0:
                return True
            axes = self.__invert_axes(axes)
        return False

    def __contains__(self, item):
        return self.contains(item)

    @staticmethod
    def __invert_axes(axes):
        if axes == 'y':
            return "x"
        else:
            return "y"

    def __put(self, h, point, axes, recv):
        if h is None:
            return self.Node(point, recv)

        cmp = point.compare_to(h.point, axes)
        if cmp < 0:
            if axes == 'y':
                recv = RectHV(recv.xmin, recv.ymin, recv.xmax, h.point.y)
            else:
                recv = RectHV(recv.xmin, recv.ymin, h.point.x, recv.ymax)
            h.left = self.__put(h.left, point, self.__invert_axes(axes), recv)
        elif cmp > 0:
            if axes == 'y':
                recv = RectHV(recv.xmin, h.point.y, recv.xmax, recv.ymax)
            else:
                recv = RectHV(h.point.x, recv.ymin, recv.xmax, recv.ymax)
            h.right = self.__put(h.right, point, self.__invert_axes(axes), recv)
        elif cmp == 0:
            pass
        return h

    def __str__(self):
        return "Size {} \n {}".format(self.__size, self.root)


def main():
    pass


if __name__ == "__main__":
    main()

# 0.366672,0.374684
# 0.315475,0.368707
# 0.349486,0.38195
