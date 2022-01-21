# Name: Xueyang Huang
# Date: March 25th
# Class section: 02
# Name of program: HuangXueyang_assign6_part2.py

# function:   is_even 
# input:      a positive integer 
# processing: determines if the supplied number is even 
# output:     boolean
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

# function:   is_odd
# input:      a positive integer
# processing: determines if the supplied number is odd
# output:     boolean
def is_odd(x):
    if x % 2 != 0:
        return True
    else:
        return False

# function:   is_prime
# input:      a positive integer
# processing: determines if the supplied number is prime. a prime number is
#             a number that only has two factors - the number 1 and itself.
#             for example, 17 is prime because it only has two factors (1 and 17).
#             in order to determine this you might need to count the # of factors
#             between 1 and the number you are testing. a note on efficiency: if you are
#             testing a number (say, 15) and you find a factor (say, 3) - do you need to even continue
#             to find additional factors?
# output:     boolean
def is_prime(x):
    if x == 1:
        return False
    else:
        for d in range(2, x + 1):
            if x % d != 0:
                continue
            elif d < x:
                return False
                break
            else:
                return True

# function:   is_perfect
# input:      a positive integer
# processing: determines if the supplied number is perfect. a perfect number
#             is a number that is equal to the sum of its factors (i.e. the
#             number 6 is perfect because 6 = 1 + 2 + 3)
# output:     boolean
def is_perfect(x):
    sum_d = 0
    for d in range(1, x + 1):
        if x % d == 0 and d < x:
            sum_d += d
        else:
            continue
    if x == sum_d:
        return True
    else:
        return False

# function:   is_abundant
# input:      a positive integer
# processing: determines if the supplied number is abundant. an abundant number
#             is a number that is less than the sum of its factors (i.e. the
#             number 12 is abundant because 12 < 1 + 2 + 3 + 4 + 6)
# output:     boolean
def is_abundant(x):
    sum_d = 0
    for d in range(1,x + 1):
        if x % d == 0 and d < x:
            sum_d += d
        else:
            continue
    if x < sum_d:
        return True
    else:
        return False

# asking the user for starting number
start = int(input('Enter starting number: '))    
while True:   # validate the starting number
    if start <= 0:
        print('Invalid, try again')
        start = int(input('Enter starting number: '))
    else:     # asking for the ending number
        end = int(input('Enter ending number: '))
        if end <= start:   # validate the ending number
            print('Invalid, try again')
            continue
        else: # write a for loop the analyze all the numbers in between
            for num in range(start, end + 1):
                if num == start:
                    print(num, 'is ...', end = ' ')
                else:
                    print('\n' + str(num) + ' is ...', end = ' ')
                a = is_even(num)
                b = is_odd(num)
                c = is_prime(num)
                d = is_perfect(num)
                e = is_abundant(num)
                if a == True:
                    print('even', end = ' ')
                if b == True:
                    print('odd', end = ' ')
                if c == True:
                    print('prime', end = ' ')
                if d == True:
                    print('perfect', end = ' ')
                if e == True:
                    print('abundant', end = ' ')
        break
