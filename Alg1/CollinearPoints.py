class CollinearPoints(object):
    def __init__(self, points):
        self.points = sorted(points)
        self.segments = []

        self.find_segments()

    def find_segments(self):
        pass

    def number_of_segments(self):
        return len(self.segments)

    def segments(self):
        return self.segments

    def __str__(self):
        result = []
        result.append("Points:")
        result.append("\n".join(([str(i) for i in self.points])))
        result.append("Segments:")
        result.append("\n".join(([str(i) for i in self.segments])))
        return "\n".join(result)


def main():
    pass

if __name__ == "__main__":
    main()


