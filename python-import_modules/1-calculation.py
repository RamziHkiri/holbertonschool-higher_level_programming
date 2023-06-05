#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, mul, sub, div
    a = 10
    b = 5
    add_res = add(a, b)
    mul_res = mul(a, b)
    sub_res = sub(a, b)
    div_res = div(a, b)
    print(f"{a} + {b} = {add_res}")
    print(f"{a} - {b} = {sub_res}")
    print(f"{a} * {b} = {mul_res}")
    print(f"{a} / {b} = {div_res}")
