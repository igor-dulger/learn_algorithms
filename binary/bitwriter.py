class BitWriter(object):
    def __init__(self, f):
        self.accumulator = 0
        self.bcount = 0
        self.out = f

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.flush()

    def __del__(self):
        try:
            self.flush()
        except ValueError:   # I/O operation on closed file.
            pass

    def close(self):
        self.flush()
        self.out.close()

    def _write_bit(self, bit):
        if self.bcount == 8:
            self.flush()
        if bit > 0:
            self.accumulator |= 1 << 7-self.bcount
        self.bcount += 1

    def write_bits(self, bits, n):
        while n > 0:
            self._write_bit(bits & 1 << n-1)
            n -= 1

    def write_boolean(self, n):
        return self.write_bits(int(n), 1)

    def write_char(self, c, n):
        return self.write_bits(ord(c), n)

    def flush(self):
        self.out.write(bytearray([self.accumulator]))
        self.accumulator = 0
        self.bcount = 0


if __name__ == '__main__':
    import os
    import sys

    # Determine this module's name from it's file name and import it.
    module_name = os.path.splitext(os.path.basename(__file__))[0]
    bitio = __import__(module_name)

    # with open('bitio_test.dat', 'wb') as outfile:
    #     with bitio.BitWriter(outfile) as writer:
    #         writer.write_boolean(0)
    #         writer.write_boolean(0)
    #         writer.write_boolean(1)
    #         writer.write_boolean(1)
    #         writer.write_boolean(0)
    #         writer.write_boolean(0)
    #         writer.write_boolean(0)
    #         writer.write_boolean(1)
    #         writer.write_char('C')
    #         chars = '12345abcde'
    #         for ch in chars:
    #             writer.write_bits(ord(ch), 7)


    # with open('bitio_test.dat', 'rb') as infile:
    #     with bitio.BitReader(infile) as reader:
    #         chars = []
    #         while True:
    #             x = reader.readbits(7)
    #             if not reader.read:  # End-of-file?
    #                 break
    #             chars.append(chr(x))
    #         print(''.join(chars))