# Name: Xueyang Huang
# Date: March 12th
# Class section: 02
# Name of program: HuangXueyang_assign5_part3c.py

# data validation in a while loop
while True:
    # store the two values in two variables
    start = int(input('Start number: '))
    end = int(input('End number: '))
    if start <= 0 or end <= 0:
        print('Start and end must be positive\n')
    elif start >= end:
        print('End number must be greater than start number\n')
    else:
        print()
        # use a for loop to validate prime numbers
        for i in range(start, end + 1):  
            for d in range(2, i + 1):
                if i % d != 0:
                    continue        
                elif d < i:
                    break            
                else:
                    print(i)
        break
