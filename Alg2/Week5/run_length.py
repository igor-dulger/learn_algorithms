from binary.bitwriter import BitWriter
from binary.bitreader import BitReader
import sys


class RunLength(object):
    def __init__(self):
        self.__r = 256
        self.__lg_r = 8
        self.__writer = BitWriter(sys.stdout.buffer)
        self.__reader = BitReader(sys.stdin.buffer)

    def compress(self):
        bit = 0
        sequence = 0
        while True:
            run = self.__reader.read_boolean()
            if self.__reader.is_empty():
                break
            if run == bit:
                if sequence == 255:
                    self.__writer.write_bits(sequence, self.__lg_r)
                    sequence = 0
                    self.__writer.write_bits(sequence, self.__lg_r)
            else:
                self.__writer.write_bits(sequence, self.__lg_r)
                sequence = 0
                bit = not bit
            sequence += 1

        self.__writer.write_bits(sequence, self.__lg_r)
        self.__writer.close()

    def expand(self):
        bit = 0
        while True:
            run = self.__reader.read_bits(self.__lg_r)
            if self.__reader.is_empty():
                break
            for i in range(run):
                self.__writer.write_boolean(bit)
            bit = not bit

        self.__writer.flush()
        sys.stdout.close()


def main():
    if len(sys.argv) != 2:
        print("Expand: python run_length.py +")
        print("Compress: python run_length.py -")
    else:
        r_l = RunLength()
        if sys.argv[1] == '+':
            r_l.expand()
        elif sys.argv[1] == '-':
            r_l.compress()
        else:
            print("Invalid option", sys.argv[1])


if __name__ == "__main__":
    main()
