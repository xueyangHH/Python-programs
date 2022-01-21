# Name: Xueyang Huang
# Date: February 19th
# Class seciton: 02
# Name of program: HuangXueyang_assign3_problem2.py

# import the random module and set up the variable
import random
print("I'm thinking of a number between 1 and 10!")
number = random.randint(1,10)
# Ask the user to guess a number
guess1 = int(input("What's your guess? "))
# report the invalid number at each guess
# Compare the number to the presupposed number
# print out the result
if guess1 >= 1 and guess1 <= 10:
    # possibility 1: 1st guess right
    # tell the user the number of the trials: 1
    if guess1 == number:
        print('You got it!')
        print('The secret number was', str(number) + '.')
        print('It took you 1 try to guess the number.')
    else:
        if guess1 > number:
            print('Too high, try again.')
            guess2 = int(input("What's your guess? "))
            # p2: 1st guess higher, 2nd guess right
            # tell the user the number of the trials: 2
            if guess2 >= 1 and guess2 <= 10:
                if guess2 == number:
                    print('You got it!')
                    print('The secret number was', str(number) + '.')
                    print('It took you 2 tries to guess the number.')
                else:
                    if guess2 > number:
                        print('Too high, try again.')
                        guess3 = int(input("What's your guess? "))
                        if guess3 >= 1 and guess3 <= 10:
                            # p3: 1st guess higher, 2nd guess higher, 3rd guess right
                            # tell the user the number of the trials: 3
                            if guess3 == number:
                                print('You got it!')
                                print('The secret number was', str(number) + '.')
                                print('It took you 3 tries to guess the number.')
                            # p4: 1st guess higher, 2nd guess higher, 3rd guess wrong
                            else:
                                print('The secret number was', str(number) + '.')
                                print("You didn't guess the number.")
                        else:
                            print('The number you entered is invalid.')
                    else:
                        print('Too low, try again.')
                        guess3 = int(input("What's your guess? "))
                        if guess3 >= 1 and guess3 <= 10:
                            # p5: 1st guess higher, 2nd guess lower, 3rd guess right
                            # tell the user the number of the trials: 3
                            if guess3 == number:
                                print('You got it!')
                                print('The secret number was', str(number) + '.')
                                print('It took you 3 tries to guess the number.')
                            # p6: 1st guess higher, 2nd guess lower, 3rd guess wrong
                            else:
                                print('The secret number was', str(number) + '.')
                                print("You didn't guess the number.")
                        else:
                            print('The number you entered is invalid.')        
            else:
                print('The number you entered is invalid.')
        else:
            print('Too low, try again.')
            guess2 = int(input("What's your guess? "))
            if guess2 >= 1 and guess2 <= 10:
                # p7: 1st guess lower, 2nd guess right
                # tell the user the number of the trials: 2
                if guess2 == number:
                    print('You got it!')
                    print('The secret number was', str(number) + '.')
                    print('It took you 2 tries to guess the number.')
                else:
                    if guess2 > number:
                        print('Too high, try again.')
                        guess3 = int(input("What's your guess? "))
                        if guess3 >= 1 and guess3 <= 10:
                            # p8: 1st guess lower, 2nd guess higher, 3rd guess right
                            # tell the user the number of the trials: 3
                            if guess3 == number:
                                print('You got it!')
                                print('The secret number was', str(number) + '.')
                                print('It took you 3 tries to guess the number.')
                            # p9: 1st guess lower, 2nd guess higher, 3rd guess wrong
                            else:
                                print('The secret number was', str(number) + '.')
                                print("You didn't guess the number.")
                        else:
                            print('The number you entered is invalid.')
                    else:
                        print('Too low, try again.')
                        guess3 = int(input("What's your guess? "))
                        if guess3 >= 1 and guess3 <= 10:
                            # p10: 1st guess lower, 2nd guess lower, 3rd guess right
                            # tell the user the number of the trials: 3
                            if guess3 == number:
                                print('You got it!')
                                print('The secret number was', str(number) + '.')
                                print('It took you 3 tries to guess the number.')
                            # p11: 1st guess lower, 2nd guess lower, 3rd guess wrong
                            else:
                                print('The secret number was', str(number) + '.')
                                print("You didn't guess the number.")
                        else:
                            print('The number you entered is invalid.')
            else:
                print('The number you entered is invalid.')
else:
    print('The number you entered is invalid.')
