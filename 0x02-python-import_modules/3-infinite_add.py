#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = 0
    args = sys.argv[1:]


    for arg in sys.argv:
        if arg != sys.argv[0]:
            total += int(arg)

    print(total)
