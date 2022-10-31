from digest import calculate
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python stats.py <file1_name> <file2_name")
        sys.exit(1)

    d1 = calculate(sys.argv[1])
    d2 = calculate(sys.argv[2])

    r = ''

    for i in range(len(d1)):
        v = bin(d1[i] ^ d2[i])
        v = v[2:]
        v = v.zfill(8)
        r += v

    zeros = r.count('0')
    ones = r.count('1')
    print("N0: ", zeros, "N1: ", ones)

if __name__ == '__main__':
    main()