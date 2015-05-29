import sys


def main():
    for filename in sys.argv[1:]:
        with open(filename, 'r') as f:
            data = [d for d in f.read().split("\n")]
            for line in data:
                print(line)

if __name__ == '__main__':
    main()
