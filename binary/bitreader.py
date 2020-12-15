class BitReader(object):
    def __init__(self, f):
        self.input = f
        self.accumulator = 0
        self.bcount = 0
        self.read = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def _read_from_stream(self):
        a = self.input.read(1)
        if a:
            self.accumulator = ord(a)
        self.bcount = 8
        self.read = len(a)

    def _read_bit(self):
        if not self.bcount:
            self._read_from_stream()
        rv = (self.accumulator & (1 << self.bcount-1)) >> self.bcount-1
        self.bcount -= 1
        return rv

    def read_bits(self, n):
        v = 0
        while n > 0:
            v = (v << 1) | self._read_bit()
            n -= 1
        return v

    def read_string(self):
        return self.input.read()

    def read_boolean(self):
        return self.read_bits(1)

    def read_char(self, n):
        return chr(self.read_bits(n))

    def is_empty(self):
        return self.read == 0


if __name__ == '__main__':
    import os
    import sys

    # Determine this module's name from it's file name and import it.
    module_name = os.path.splitext(os.path.basename(__file__))[0]
    bitio = __import__(module_name)

    # reader = BitReader(sys.stdin.buffer)
    # print("Size", len(reader.read_string()))

    # with open('bitio_test.dat', 'wb') as outfile:
    #     with bitio.BitWriter(outfile) as writer:
    #         chars = '12345abcde'
    #         for ch in chars:
    #             writer.writebits(ord(ch), 7)
    #
    # with open('bitio_test.dat', 'rb') as infile:
    #     with bitio.BitReader(infile) as reader:
    #         chars = []
    #         while True:
    #             x = reader.readbits(7)
    #             if not reader.read:  # End-of-file?
    #                 break
    #             chars.append(chr(x))
    #         print(''.join(chars))