#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    i = len(sys.argv) - 1
    if i == 0:
        print("0")
    else:
        sum = 0
        for arg in range(1, i+1):
            sum += int(sys.argv[arg])
        print(sum)
