# Name: Xueyang Huang
# Date: April 11th
# Class section: 02
# Name of program: HuangXueyang_assign7_part3.py

while True:
    seed = input('Enter a six digit seed: ')
    if seed.isdigit() == True:
        if len(seed) == 6:
            break
        else:
            print('The seed is not 6-digit long, please try again\n')
    else:
        print('Invalid seed, please try again\n')
bad_seed = False

low_num = input('Enter lowest possible random integer: ')
while True:
    if '-' in low_num:
        if low_num[1::].isdigit() == False:
            print('Invalid low values, please try again.\n')
            low_num = input('Enter lowest possible random integer: ')
        else:
            high_num = input('Enter highest possible random integer: ')
            if '-' in high_num:
                if high_num[1::].isdigit() == True:
                    if int(high_num) > int(low_num):
                        break
                    else:
                        print('Invalid high values, please try again.\n')
                else:
                    print('Invalid high values, please try again.\n')
            else:
                if high_num.isdigit() == True:
                    if int(high_num) > int(low_num):
                        break
                    else:
                        print('Invalid high values, please try again.\n')
                else:
                    print('Invalid high values, please try again.\n')
    else:
        if low_num.isdigit() == False:
            print('Invalid low values, please try again.\n')
            low_num = input('Enter lowest possible random integer: ')
        else:
            high_num = input('Enter highest possible random integer: ')
            if high_num.isdigit() == True:
                if int(high_num) > int(low_num):
                    break
                else:
                    print('Invalid high values, please try again.\n')
            else:
                print('Invalid high values, please try again.\n')

while True:
    num = input('\nHow many random numbers do you want to generate? ')
    if num.isdigit() == False:
        print('Invalid, try again.')
    else:
        if int(num) >= 1:
            break
        else:
            print('Invalid, try again.')
    
for i in range(int(num)):
    # one major drawback: when the seed approaches a number that has a lot of
    # zeros in it (i.e. x00000/0000x0/0x000x, but some seeds like that with
    # a certain pattern won't cause any problem),
    # the random number generator will always yield a numeric value of the lowest
    # number in the range because the middle of the square will become 000000,
    # or the PRNG will enter a cycle where it always generate a same set of numbers
    # solution: find out the positive number(s) in the seed and replace overmany
    # zeros with the positive number(s)
    pos_num = 0
    place1 = 0
    place2 = 0
    for c in range(len(seed)): # fliter the seed
        if int(seed[c]) > 0:
            pos_num += 1 # keep track of num of positive numbers
            if pos_num == 1:
                place1 = c
            elif pos_num == 2:
                place2 = c
        else:
            continue
    if pos_num == 1: # only one pos number
        if int(seed[-1]) > 0:# if the pos num is already at the end of the seed
            if int(seed[-1]) != 1:
                bad_seed = False
                seed = '0' * 5 + seed[place1] # good seed
            else: # if the pos num is 1
                bad_seed = True
                seed = '0' * 5 + str(int(seed[-1])+1)
        else: # if not then replace all the zeros in the seed with the pos num
            bad_seed = True
            seed = seed[place1] * 6
    elif pos_num == 2: # if two pos numbers
        if ((int(seed[-2]) > 0 and int(seed[-1]) > 0) or (int(seed[-3]) > 0
            and int(seed[-2]) > 0)): # they are next to each other at the end or one digit to the end and good
            if int(seed[-2]) > 0 and int(seed[-1]) > 0:
                bad_seed = False
                seed = '0' * 4 + seed[place1] + seed[place2]
            elif int(seed[-3]) > 0 and int(seed[-2]) > 0:
                bad_seed = False
                seed = '0' * 3 + seed[place1] + seed[place2] + '0'
        elif ((int(seed[-5]) > 0 and int(seed[-3]) > 0) or (int(seed[-4]) > 0
            and int(seed[-2]) > 0) or (int(seed[-3]) > 0 and int(seed[-1]) > 0)
              or (int(seed[-6]) > 0 and int(seed[-3]) > 0) or (int(seed[-5]) > 0
            and int(seed[-2]) > 0) or (int(seed[-4]) > 0 and int(seed[-1]) > 0)):
            bad_seed = False  # if only one/two zero(s) between them then good
        else: # if not then mix the only two pos values up (three of each)
            bad_seed = True
            seed = seed[place1] * 3 + seed[place2] * 3
    elif pos_num == 0:
        bad_seed = True
        seed = '000002'
    # this is not the best solution to fix the flaw, but it can capture most of
    # the bad seeds that the user enters and turn them into something that would
    # definitely work; lots of type II errors here but I cannot do any further
    if bad_seed == False:
        print('\nSeed value:', seed)
    else:
        print('\nModified seed value:', seed)
    square = str(int(seed) ** 2)
    print('Square of seed:', square)
    if len(square) > 6:
        if len(square) % 2 == 0:
            start = (len(square) - 6) // 2
            middle = square[start:-start:1]
        else:
            start = (len(square) - 7) // 2
            middle = square[start:(-start-1):1]
    else:
        middle = square
    print('Middle 6 digits of square:', middle)
    percent = int(middle)/999999
    print('Percentage =', middle, '/999999 =', percent)
    print('Scaling up to a number between', low_num, 'and', high_num)
    prim_rand = (int(high_num) - int(low_num)) * percent + int(low_num)
    print('(', high_num, '-', low_num, ')', '*', percent, '+', low_num, '=', prim_rand)
    rand_num = int(prim_rand)
    print('Converted to an integer:', rand_num)
    seed = middle

