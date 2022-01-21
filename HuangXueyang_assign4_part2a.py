# Name: Xueyang Huang
# Date: February 24th
# Class section: 02
# Name of program: HuangXueyang_assign4_part2a.py

# set up the controlling variable
looping = 'yes'

# write a while loop to determine if the user enter a valid total number of sticks
while looping == 'yes':
    # ask the user for a total number of sticks
    total = int(input('How many sticks (10-100)? '))
    # determine if the total number falls in the range [10,100]
    if total < 10:
        print("Sorry, that's too few sticks. Try again.")
    elif total > 100:
        print("Sorry, that's too many sticks. Try again.")
    else:
        print("Great Let's play ... ")
        looping = 'no'
        # force the first while loop to end and continue to the next while loop
        # set up the accumulator variable
        turns = 0
        # determine the status of the total number
        while total > 0:
            print('\nThere are', total, 'sticks on the table.')
            # ask the user for a number of sticks they would like to pick
            turns = int(input('How many sticks do you want to take (1, 2 or 3)? '))
            total -= turns
            # determine if the number of sticks is valid
            if turns < 1 or turns > 3:
                print('Sorry, that is not a valid number.')
                # reset the total number back to what it was
                total += turns
                continue
            else:
                # go back to iteration if there is still sticks left
                if total > 0:
                    continue
                # ask the user to enter the number of sticks they would pick again
                # if the sticks left are smaller than 0
                elif total < 0:
                    print('Sorry, that would bring the total # of sticks below 0. Try again.')
                    # reset the total number back to what it was
                    total += turns
                    continue
                # Game over!
                else:
                    print('\nThere are no sticks left on the table! Game over.')
                    break
