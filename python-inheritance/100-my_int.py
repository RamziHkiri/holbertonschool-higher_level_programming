#!/usr/bin/python3
""" Define MyInt that inherits from  class int. """


class MyInt(int):
    """ redefine eq and ne methods of class int"""

    def __eq__(self, value):
        if self.real != value:
            return True
        else:
            return False

    def __ne__(self, value):
        if self.real == value:
            return True
        else:
            return False
