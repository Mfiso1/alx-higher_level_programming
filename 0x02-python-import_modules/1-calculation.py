#!/usr/bin/python3

import calculator_1 as arithmetic_functions

if __name__ == "__main__":
    a = 10
    b = 5

    print("{:d} / {:d} = {:d}".format(a, b, arithmetic_functions.div(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, arithmetic_functions.mul(a, b)))
    print("{:d} + {:d} = {:d}".format(a, b, arithmetic_functions.add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, arithmetic_functions.sub(a, b)))
