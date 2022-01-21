# Name: Xueyang Huang
# Date: March 12th
# Class section: 02
# Name of program: HuangXueyang_assign5_part3d.py

# data validation in a while loop
while True:
    # store the two values
    start = int(input('Start number: '))
    end = int(input('End number: '))
    if start <= 0 or end <= 0:
        print('Start and end must be positive\n')
    elif start >= end:
        print('End number must be greater than start number\n')
    else:
        # store the number of spaces needed to align the numbers
        space = len(str(end)) + 1
        # keep track of how many numbers printed
        i_tracker = 0
        # use a for loop to determine prime numbers
        for i in range(start, end + 1):
            for d in range(2, i + 1):
                if i % d != 0:
                    continue        
                elif d < i:
                    break            
                else:
                    # format the printed numbers with predetermined space value
                    print(format(i, '>' + str(space) + 'd'), end = '')
                    i_tracker += 1
                    # once ten numbers got printed go to the next line
                    if i_tracker % 10 == 0:
                        print()
        break
