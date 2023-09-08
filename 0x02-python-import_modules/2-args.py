#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    no_arg = len(arguments)

    if no_arg == 0:
        print("0 arguments.")
    elif no_arg == 1:
        print("1 argument:")
        print(f"1: {arguments[0]}")
    else:
        print(f"{no_arg} arguments:")
        for j, arg in enumerate(arguments, start=1):
            print(f"{j}: {arg}")
