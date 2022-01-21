# Name: Xueyang Huang
# Date: March 25th
# Class section: 02
# Name of program: HuangXueyang_assign6_part1_challenge1.py

# these are the basic arithmetic functions you will be using for this challenge

# function:   add
# input:      two integers/floats
# processing: adds the two supplied values
# output:     returns the sum (integer/float)
def add(a,b):
    return a+b

# function:   sub
# input:      two integers/floats
# processing: subtracts the two supplied values
# output:     returns the difference (integer/float)
def sub(a,b):
    return a-b

# function:   mult
# input:      two integers/floats
# processing: multiplies the two supplied values
# output:     returns the product (integer/float)
def mult(a,b):
    return a*b

# function:   sqrt
# input:      one integer/float
# processing: computes the square root of the supplied value
# output:     returns the square root (float)
def sqrt(a):
    return a**0.5

# function:   square
# input:      one integer/float
# processing: raises the supplied integer/float to the 2nd power
# output:     returns the square (integer/float)
def square(a):
    return a**2

# these are the two points you will be using

# point 1
x1 = 0
y1 = 0

# point 2
x2 = 100
y2 = 100

# compute the distance between the two points above using the distance formula.
# you may ONLY use the functions above to do this - no math operators are allowed!  
# your calculation must also be done on a single line.
distance = sqrt( add( square( sub(x1,x2) ), square( sub(y1,y2) ) ) )

print (distance) # answer should be 141.4213562373095
