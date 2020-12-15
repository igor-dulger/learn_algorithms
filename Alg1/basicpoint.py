from abc import ABC
from abc import abstractmethod


class BasicPoint(ABC):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def draw(self):
        pass

    def draw_to(self, point):
        pass

    def compare_to(self, point, axes=None):
        if type(self) == type(point):
            if self.y < point.y:
                return -1
            elif self.y > point.y:
                return 1
            elif self.x < point.x:
                return -1
            elif self.x > point.x:
                return 1
            else:
                return 0
        else:
            raise ValueError("Can't compare {} and {}".format(self.__class__.__name__, point.__class__.__name__))

    def __cmp__(self, other):
        self.compare_to(other)

    def __lt__(self, other):
        if other is None: return False
        return self.compare_to(other) < 0

    def __gt__(self, other):
        if other is None: return False
        return self.compare_to(other) > 0

    def __eq__(self, other):
        if other is None: return False
        return self.compare_to(other) == 0

    def __le__(self, other):
        if other is None: return False
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):
        if other is None: return False
        return self.__gt__(other) or self.__eq__(other)

    def __ne__(self, other):
        if other is None: return False
        return not self.__eq__(other)

    def __str__(self):
        return "{},{}".format(self.x, self.y)

    def __repr__(self):
        return "X:{} Y:{}".format(self.x, self.y)

    def __hash__(self):
        return hash(str(self.x) + str(self.y))


def main():
    pass


if __name__ == "__main__":
    main()
