#!/usr/bin/python3
def weight_average(my_list=[]):
    sum1 = 0
    sum2 = 0
    for tuple in my_list:
        sum1 += tuple[0] * tuple[1]
        sum2 += tuple[1]
    return sum1 / sum2
