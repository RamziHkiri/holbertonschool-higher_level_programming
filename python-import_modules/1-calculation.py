#!/usr/bin/python3
from re import X


if __name__ == "__main__":
    from calculator_1 import add, mul, sub, div
    a = 10
    b = 5
    add_res = add(a, b)
    mul_res = mul(a, b)
    sub_res = sub(a, b)
    div_res = div(a, b)
    print("{} + {} = {}".format(a, b, add_res))
    print("{} - {} = {}".format(a, b, sub_res))
    print("{} * {} = {}".format(a, b, mul_res))
    print("{} / {} = {}".format(a, b, div_res))
