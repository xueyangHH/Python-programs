# Name: Xueyang Huang
# Date: Feb.5
# Class section: 02
# Name of the program: HuangXueyang_assign2_problem2

# ask the user to enter two numbers
# first number
n1 = int(input('Enter a number between 0 and 999: '))

# second number
n2 = int(input('Enter another number between 0 and 999: '))

# calculations of ones
n1_one = int(n1%10)
n2_one = int(n2%10)
sum_ones = n1_one + n2_one

# calculations of tens
n1_ten = int((n1%100 - n1_one)/10)
n2_ten = int((n2%100 - n2_one)/10)
sum_tens = n1_ten + n2_ten

# calculations of hundreds
n1_hun = int(n1//100)
n2_hun = int(n2//100)
sum_huns = n1_hun + n2_hun

# print out the sums
print(format('Sum of ones', '15s'), '=', n1_one, '+', n2_one, '=', sum_ones)
print(format('Sum of tens', '15s'), '=', n1_ten, '+', n2_ten, '=', sum_tens)
print(format('Sum of hundreds', '15s'), '=', n1_hun, '+', n2_hun, '=', sum_huns)
