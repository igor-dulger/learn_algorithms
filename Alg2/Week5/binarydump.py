import sys


def main():
    if len(sys.argv) == 2:
        bytes_in_line = int(sys.argv[1])
    else:
        bytes_in_line = 4

    content = sys.stdin.buffer.read()
    block_length = 0
    for c in content:
        print("{0:08b}".format(c), end=" ")
        block_length += 1
        if block_length >= bytes_in_line:
            print()
            block_length = 0
    print()
    print("{0:d} bytes ({1:d} bits)".format(len(content), len(content)*8))


if __name__ == "__main__":
    main()
