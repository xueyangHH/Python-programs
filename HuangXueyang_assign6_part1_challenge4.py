# Name: Xueyang Huang
# Date: March 25th
# Class section: 02
# Name of program: HuangXueyang_assign6_part1_challenge4.py

# function:   simple_sort_version1
# input:      two numeric values
# processing: sort the two values in ascending order
# output:     two values in sorted order
def simple_sort_version1(a,b):
    if a > b:
        return b,a
    else:
        return a,b
