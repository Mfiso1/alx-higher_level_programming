#!/usr/bin/env python3

import sys

def main():
    arguments = sys.argv[1:]
    result = sum(map(int, arguments))
    print(result)

if __name__ == "__main__":
    main()
