from binary.bitwriter import BitWriter
from binary.bitreader import BitReader
from strings.circular_sufix_array import CircularSuffixArray
import sys


class BurrowsWheeler(object):
    def __init__(self):
        pass

    @classmethod
    def transform(cls):
        reader = BitReader(sys.stdin.buffer)
        writer = BitWriter(sys.stdout.buffer)
        data = reader.read_string()
        cfa = CircularSuffixArray(data)

        for i in range(cfa.length()):
            if cfa.index(i) == 0:
                writer.write_bits(i, 32)
                break

        for i in range(cfa.length()):
            writer.write_bits(data[(cfa.index(i)-1) % cfa.length()], 8)
        writer.close()

    @classmethod
    def inverse_transform(cls):
        reader = BitReader(sys.stdin.buffer)
        writer = BitWriter(sys.stdout.buffer)
        first = reader.read_bits(32)
        t = reader.read_string()
        t_pos = []
        next_index = []

        for i in range(256):
            t_pos.append([])

        for i in range(len(t)):
            t_pos[t[i]].append(i)

        t_sorted = sorted(t)

        for v in t_sorted:
            next_index.append(t_pos[v].pop(0))

        for i in range(len(t)):
            writer.write_bits(t_sorted[first], 8)
            first = next_index[first]
        writer.close()


def main():
    if len(sys.argv) != 2:
        print("Transform: python burrows_wheeler.py -")
        print("Inverse: python burrows_wheeler.py +")
    else:
        if sys.argv[1] == '-':
            BurrowsWheeler.transform()
        elif sys.argv[1] == '+':
            BurrowsWheeler.inverse_transform()
        else:
            print("Invalid option", sys.argv[1])


if __name__ == "__main__":
    main()
