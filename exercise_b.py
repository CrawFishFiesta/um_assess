import os
import sys


def merge(amy, ben):

    lena = len(amy)
    lenb = len(ben)

    return lena, lenb


def calc_something(lenb, lena):
    something_to_calculate_is_this_equation = lenb + lena

    return something_to_calculate_is_this_equation



def main():
    """
    This program is suppose to take the lengths of two strings and print out the sum.
    """
    a = "amelia"
    b = "benjamin"

    lena, lenb = merge(a, b)
    total_length_of_TwoStrings_is_thisVALUE = calc_something(lena, lenb)

    print("{}".format(total_length_of_TwoStrings_is_thisVALUE))
    sys.exit()
