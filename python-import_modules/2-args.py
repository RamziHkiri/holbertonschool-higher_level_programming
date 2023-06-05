#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv[1:]
    arg_n = len(args)
    if arg_n == 0:
        print("0 arguments.")
    else:
        print("{} {}".format(arg_n, "arguments" if arg_n > 1 else "argument"))
        i = 0
        for arg in sys.argv[1:]:
            i += 1
            print("{}: {}".format(i, arg))
