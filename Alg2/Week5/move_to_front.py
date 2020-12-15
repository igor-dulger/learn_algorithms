from binary.bitwriter import BitWriter
from binary.bitreader import BitReader
import sys


class MoveToFront(object):
    def __init__(self):
        pass

    @staticmethod
    def __init_alphabet():
        result = []
        for i in range(256):
            result.append(chr(i))
        return "".join(result)

    @staticmethod
    def encode():
        reader = BitReader(sys.stdin.buffer)
        writer = BitWriter(sys.stdout.buffer)
        alphabet = MoveToFront.__init_alphabet()
        data = reader.read_string()
        for c in data:
            pos = alphabet.find(chr(c))
            writer.write_bits(pos, 8)
            alphabet = alphabet[pos] + alphabet[0:pos] + alphabet[pos+1:]
        writer.close()

    @staticmethod
    def decode():
        reader = BitReader(sys.stdin.buffer)
        writer = BitWriter(sys.stdout.buffer)
        alphabet = MoveToFront.__init_alphabet()
        data = reader.read_string()
        for pos in data:
            writer.write_char(alphabet[pos], 8)
            alphabet = alphabet[pos] + alphabet[0:pos] + alphabet[pos+1:]
        writer.close()


def main():
    if len(sys.argv) != 2:
        print("Encode: python move_to_front.py -")
        print("Decode: python move_to_front.py +")
    else:
        if sys.argv[1] == '-':
            MoveToFront.encode()
        elif sys.argv[1] == '+':
            MoveToFront.decode()
        else:
            print("Invalid option", sys.argv[1])


if __name__ == "__main__":
    main()
