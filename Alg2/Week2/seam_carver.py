import math
from dequeue.deque import Deque
import imageio
from helpers import basic

class SeamCarver(object):

    class Pixel(object):
        def __init__(self, r, g, b):
            self.__r = r
            self.__g = g
            self.__b = b
            self.__energy = 0

        @property
        def r(self):
            return self.__r

        @property
        def g(self):
            return self.__g

        @property
        def b(self):
            return self.__b

        @property
        def energy(self):
            return self.__energy

        @energy.setter
        def energy(self, energy):
            self.__energy = energy

        def __str__(self):
            return self.__repr__()

        def __repr__(self):
            return str({"R": self.r, "G": self.g, "B": self.b, "E": self.energy})

    def __init__(self, picture):
        if picture is None:
            raise ValueError("Invalid picture, image object expected")
        self.__picture = picture
        self.__width = len(picture[0])
        self.__height = len(picture)

        self.__pixels = []
        for y, row in enumerate(picture):
            self.__pixels.append([self.Pixel(*[int(color) for color in pixel]) for pixel in row])

        for y in range(self.__height):
            for x in range(self.__width):
                self.__pixels[y][x].energy = self.__get_pixel_energy(x, y)

    def picture(self):
        return self.__picture

    def width(self):
        return self.__width

    def height(self):
        return self.__height

    def energy(self, x, y):
        self.__check_x(x)
        self.__check_y(y)
        return self.__pixels[y][x].energy

    @basic.timer
    def find_vertical_seam(self):
        self.__reset_paths(vertical=True)

        for y in range(self.__height - 1):
            for x in range(self.__width):
                if x > 0:
                    self.__relax(x, y, x-1, y+1)

                self.__relax(x, y, x, y+1)

                if x < self.__width - 1:
                    self.__relax(x, y, x+1, y+1)

        last_y = self.__height - 1
        min_path = self.__distances[last_y][0]
        min_path_x = 0
        for x in range(self.__width):
            if self.__distances[last_y][x] < min_path:
                min_path = self.__distances[last_y][x]
                min_path_x = x

        result = Deque()
        y = self.__height-1

        while min_path_x is not None:
            result.add_first(min_path_x)
            min_path_x, y = self.__from_path[y][min_path_x]

        return [el for el in result]

    @basic.timer
    def find_horizontal_seam(self):
        self.__reset_paths(vertical=False)

        for x in range(self.__width - 1):
            for y in range(self.__height):
                if y > 0:
                    self.__relax(x, y, x+1, y-1)

                self.__relax(x, y, x+1, y)

                if y < self.__height - 1:
                    self.__relax(x, y, x+1, y+1)

        last_x = self.__width - 1
        min_path = self.__distances[0][last_x]
        min_path_y = 0
        for y in range(self.__height):
            if self.__distances[y][last_x] < min_path:
                min_path = self.__distances[y][last_x]
                min_path_y = y

        result = Deque()
        x = self.__width-1

        while min_path_y is not None:
            result.add_first(min_path_y)
            x, min_path_y = self.__from_path[min_path_y][x]

        return [el for el in result]

    def remove_vertical_seam(self, seam):
        if self.__width <= 1:
            raise ValueError("Can't resize picture, it is too small")

        self.__check_seam(seam, self.__height)

        prev = seam[0]
        for y, x in enumerate(seam):
            self.__check_x(x)
            self.__check_distance(prev, x)
            prev = x
            self.__pixels[y] = self.__pixels[y][:x] + self.__pixels[y][x+1:]

        self.__width -= 1

        for y, x in enumerate(seam):
            if x > 0:
                self.__pixels[y][x - 1].energy = self.__get_pixel_energy(x - 1, y)

            if x < self.__width:
                self.__pixels[y][x].energy = self.__get_pixel_energy(x, y)

    def remove_horizontal_seam(self, seam):
        if self.__height <= 1:
            raise ValueError("Can't resize picture, it is too small")

        self.__check_seam(seam, self.__width)

        prev = seam[0]
        for x, y in enumerate(seam):
            self.__check_y(y)
            self.__check_distance(prev, y)
            prev = y
            for t_y in range(y+1, self.__height):
                self.__pixels[t_y-1][x] = self.__pixels[t_y][x]
        del self.__pixels[self.__height-1]
        self.__height -= 1

        for x, y in enumerate(seam):
            if y > 0:
                self.__pixels[y-1][x].energy = self.__get_pixel_energy(x, y-1)

            if y < self.__height:
                self.__pixels[y][x].energy = self.__get_pixel_energy(x, y)

    @basic.timer
    def __reset_paths(self, vertical=True):
        self.__from_path = [[(None, None) for x in range(self.__width)] for y in range(self.__height)]
        self.__distances = [[math.inf for x in range(self.__width)] for y in range(self.__height)]
        if vertical:
            self.__distances[0] = [self.__pixels[0][x].energy for x in range(self.__width)]
        else:
            for y in range(self.__height):
                self.__distances[y][0] = self.__pixels[y][0].energy

    def __relax(self, from_x, from_y, to_x, to_y):
        # print("From", from_x, from_y, "to", to_x, to_y)
        possible_distance = self.__distances[from_y][from_x] + self.__pixels[to_y][to_x].energy
        # print("Possible", possible_distance, "old", self.__distances[to_y][to_x])
        if possible_distance < self.__distances[to_y][to_x]:
            self.__distances[to_y][to_x] = possible_distance
            self.__from_path[to_y][to_x] = (from_x, from_y)

    def __get_rgb(self, x, y):
        return self.__pixels[y][x]

    def __get_pixel_energy(self, x, y):
        if x == 0 or x == self.__width-1 or y == 0 or y == self.__height-1:
            return 1000

        left_x = self.__get_rgb(x-1, y)
        right_x = self.__get_rgb(x+1, y)
        top_y = self.__get_rgb(x, y-1)
        bottom_y = self.__get_rgb(x, y+1)
        delta_x = (left_x.r - right_x.r) ** 2 + (left_x.g - right_x.g) ** 2 + (left_x.b - right_x.b) ** 2
        delta_y = (top_y.r - bottom_y.r) ** 2 + (top_y.g - bottom_y.g) ** 2 + (top_y.b - bottom_y.b) ** 2
        return math.sqrt(delta_x + delta_y)

    @staticmethod
    def __check_seam(seam, length):
        if seam is None:
            raise ValueError("Invalid seam, array expected")

        if len(seam) != length:
            raise ValueError(
                "Invalid seam, array length expected to be {} actual length is {}".format(length, len(seam))
            )

    def __check_x(self, x):
        if not 0 <= x < self.__width:
            raise ValueError("Invalid x, it must be between 0 and {}".format(self.__width-1))

    def __check_y(self, y):
        if not 0 <= y < self.__height:
            raise ValueError("Invalid x, it must be between 0 and {}".format(self.__height-1))

    @staticmethod
    def __check_distance(prev, current):
        if abs(prev - current) > 1:
            raise ValueError("Invalid seam sequence, {prev} {x} are too far away".format(prev, current))

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        matrix = ""
        for row in self.__pixels:
            matrix += ", ".join((str(p) for p in row)) + "\n"
        return "Width: {}\nHeight: {}\nMatrix: \n{}".format(self.__width, self.__height, matrix)


def main():

    d = SeamCarver(imageio.imread("../data/seam/HJocean.png"))
    # print(d)
    print(d.find_vertical_seam())
    # d.remove_vertical_seam(d.find_vertical_seam())
    # print(d)
    print(d.find_horizontal_seam())
    # d.remove_horizontal_seam(d.find_horizontal_seam())
    # print(d)
    #
    # for i in d.adj(0):
    #     print(i)


if __name__ == "__main__":
    main()
