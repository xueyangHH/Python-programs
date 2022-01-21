# Name: Xueyang Huang
# Date: March 12th
# Class section: 02
# Name of program: HuangXueyang_assign5_part3a.py

# data validation in a while loop
while True:
    num = int(input('Enter a positive number to test: '))
    if num <= 0:
        print('Invalid number! Try again.\n')
    # kicking 1 out
    elif num == 1:
        print('\n1 is techinically not a prime number.')
        break
    # kicking 2 out for that it cannot go through the following loop
    elif num == 2:
        print('\n2 is a prime number!')
        break
    else:
        print()
        # set up a for loop to validate a prime number
        for d in range(2, num):
            if num % d != 0:
                print(d, 'is NOT a divisor of', num, '... continuing')
            # stop immediately when a divisor is found
            else:
                print(d, 'is a divisor of', num, '... stopping')
                print('\n' + str(num) + ' is not a prime number.')
                break
        # the value of the divisor does not need to reach the value of the testing number
        if d == num - 1:
            print('\n' + str(num) + ' is a prime number!')
        break
