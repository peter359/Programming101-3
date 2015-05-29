import sys


def main():
    with open(sys.argv[1], "r") as f:
        numbers = f.read().split(" ")
        print(sum([int(n) for n in numbers]))

if __name__ == '__main__':
    main()
