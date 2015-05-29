import sys
from random import randint


def main():
    filename = sys.argv[1]
    n = int(sys.argv[2])
    contents = [str(randint(1, 1000)) for i in range(0, n)]
    with open(filename, "w") as f:
        f.write(" ".join(contents))


if __name__ == '__main__':
    main()
