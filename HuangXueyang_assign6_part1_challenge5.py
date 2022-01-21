# Name: Xueyang Huang
# Date: March 25th
# Class section: 02
# Name of program: HuangXueyang_assign6_part1_challenge5.py

# function:   simple_sort_version2
# input:      three numeric values
# processing: sort the three values in ascending order
# output:     three values in sorted order
def simple_sort_version2(a,b,c):
    if a <= b <= c:
        return a,b,c
    elif c <= b <= a:
        return c,b,a
    elif b <= a <= c:
        return b,a,c
    elif b <= c <= a:
        return b,c,a
    elif c <= a <= b:
        return c,a,b
    else:
        return a,c,b
