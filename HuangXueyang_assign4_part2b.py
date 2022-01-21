# Name: Xueyang Huang
# Date: February 24th
# Class section: 02
# Name of program: HuangXueyang_assign4_part2b.py

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
        # set up the accumulator variable
        turns = 0
        # set up the code for each player starting with player 1
        player = 1
        while total > 0:
            # first turn goes to player 1
            if player == 1:
                print('\nTurn: Player 1')
                print('There are', total, 'sticks on the table.')
                # ask the player for a number of sticks they would like to pick
                turns = int(input('How many sticks do you want to take (1, 2 or 3)? '))
                total -= turns
                # determine if the number of sticks is valid
                if turns < 1 or turns > 3:
                    print('Sorry, that is not a valid number.')
                    # reset the total number back to what it was
                    total += turns
                    continue
                else:
                    # give the turn to player 2 if there is still sticks left
                    if total > 0:
                        # reset the player code to 2
                        player = 2
                        continue
                    # ask the user again to enter the number of sticks they would pick
                    # if the sticks left are smaller than 0
                    elif total < 0:
                        print('Sorry, that would bring the total # of sticks below 0. Try again.')
                        # reset the total number back to what it was
                        total += turns
                        continue
                    # Game over! Reset the player code to the other player because he/she wins
                    else:
                        print('\nThere are no sticks left on the table! Game over.')
                        player = 2
                        break
            elif player == 2:
                # the next turn goes to player 2
                print('\nTurn: Player 2')
                print('There are', total, 'sticks on the table.')
                # ask the player for a number of sticks they would like to pick
                turns = int(input('How many sticks do you want to take (1, 2 or 3)? '))
                total -= turns
                # determine if the number of sticks is valid
                if turns < 1 or turns > 3:
                    print('Sorry, that is not a valid number.')
                    # reset the total number back to what it was
                    total += turns
                    continue
                else:
                    # give the turn to player 1 if there is still sticks left
                    if total > 0:
                        # reset the player code to 1
                        player = 1
                        continue
                    # ask the user again to enter the number of sticks they would pick
                    # if the sticks left are smaller than 0
                    elif total < 0:
                        print('Sorry, that would bring the total # of sticks below 0. Try again.')
                        # reset the total number back to what it was
                        total += turns
                        continue
                    # Game over! Reset the player code to the other player because he/she wins
                    else:
                        print('\nThere are no sticks left on the table! Game over.')
                        player = 1
                        break
                    
# report the winner to the users
print('Player', player, 'wins!')
