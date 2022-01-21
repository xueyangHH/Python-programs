# Name: Xueyang Huang
# Date: March 12th
# Class section: 02
# Name of program: HuangXueyang_assign5_part3b.py

# kicking 1 out
print('1 is techinically not a prime number.')
# set up a for loop to validate prime numbers
for i in range(2, 1001):  
    for d in range(2, i + 1):
        if i % d != 0:
            continue
        # not prime! exit the nested loop and go on to the next number
        elif d < i:
            break
        # prime! automatically exit the nested loop because the numbers in the
        # predetermined range are all run out
        else:
            print(i, 'is a prime number!')
