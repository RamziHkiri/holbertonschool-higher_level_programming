#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or isinstance(roman_string, str):
        return 0
    roman_numbers = {"I": 1,
                     "V": 5,
                     "X": 10,
                     "L": 50,
                     "C": 100,
                     "D": 500,
                     "M": 1000}
    sum = 0
    prev_val = 1000
    for char in roman_string:
        if char in roman_numbers:
            if roman_numbers[char] <= prev_val:
                sum += roman_numbers[char]
            else:
                sum = roman_numbers[char] - sum
            prev_val = roman_numbers[char]
        else:
            sum = 0
            break
    return sum
