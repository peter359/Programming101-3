import sys


def main():
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        data = [d for d in f.read().split("\n") if d != '']
        for line in data:
            print(line)

if __name__ == '__main__':
    main()
