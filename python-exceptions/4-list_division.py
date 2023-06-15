#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [None] * list_length
    for i in range(0, list_length):
        try:
            new_list[i] = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("devision by 0")
            new_list[i] = 0
            pass
        except IndexError:
            print("out of range")
            new_list[i] = 0
            pass
        except TypeError:
            new_list[i] = 0
            print("wrong type")
            pass
        finally:
            pass
    return new_list
