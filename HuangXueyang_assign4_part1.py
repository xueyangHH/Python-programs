# Name: Xueyang Huang
# Date: February 24th
# Class section: 02
# Name of program: HuangXueyang_assign4_part1.py

# ask the user to enter the sides of their dice
sides = int(input('How many sides on your dice (4, 6, 8, 10, 12 or 20)? '))

while True:
    # determine if the integer they enter is valid
    # if sides in [4,6,8,10,12,20]:
    if sides == 4 or sides == 6 or sides == 8 or sides == 10 or sides == 12 or sides == 20:
        break
    else:
        print('Invalid size, try again.')
        sides = int(input('How many sides on your dice (4, 6, 8, 10, 12 or 20)? '))

print('\nThanks, here we go!')

# import the random and module and set up the accumulator variables
import random
rolls = 0
odds = 0
evens = 0
highs = 0
doubles = 0
high_low = 0
sums = 0
total_d1 = 0
total_d2 = 0

while True:
    # roll two copies of the selected die size
    d1 = random.randint(1,sides)
    d2 = random.randint(1,sides)
    # keep track of number of rolls and sums of value of dice
    rolls += 1
    total_d1 += d1
    total_d2 += d2
    # display the dice value
    print('\n'+str(rolls)+'.'+' dies #1 is *'+str(d1)+'* and dies #2 is *'+str(d2)+'*', end = " ")
    # determine if the dice value qualify as the following stuations
    # 1. A double roll
    # double: d1==d2
    # 2. A high roll
    # high: d1 == sides and d2 == sides
    # 3. A high/low roll
    # high/low: d1==1 and d2==sides or d1==sides or d2==1
    # 4. An even roll
    # even: d1%2==0 and d2%2==0
    # 5. An odd roll
    # odd: d1%2 != 0 and d2%2 != 0
    # 6. A sum value
    # d1+d2==sides
    # 7. Snake eyes
    # d1==1 and d2==1
    if d1 % 2 != 0 and d2 % 2 != 0:
        print('Odd!', end = " ")
        odds += 1
        if d1 == d2:
            print('Double!', end = " ")
            doubles += 1
            if d1 + d2 == sides:
                print('Sum value is size value!', end = " ")
                sums += 1
            elif d1 == 1 and d2 == 1:
                print('Snake Eyes!')
                break
        else:
            if d1 + d2 == sides:
                print('Sum value is size value!', end = " ")
                sums += 1
    elif d1 % 2 == 0 and d2 % 2 == 0:
        print('Even!', end = " ")
        evens += 1
        if d1 == d2:
            print('Double!', end = " ")
            doubles += 1
            if d1 + d2 == sides:
                print('Sum value is size value!', end = " ")
                sums += 1
            elif d1 == sides and d2 == sides:
                    print('High!', end = " ")
                    highs += 1
        else:
            if d1 + d2 == sides:
                print('Sum value is size value!', end = " ")
                sums += 1
    elif (d1 == 1 and d2 == sides) or (d1 == sides and d2 == 1):
        print('High / Low!', end = " ")
        high_low += 1

# report statistics
print('\nYou finally got snake eyes on roll #', rolls)
print('Along the way you rolled DOUBLES', doubles, 'times.', end = " ")
print('('+ str(format((doubles/rolls)*100, '.2f'))+'% of all rolls were doubles)')
print('Along the way you rolled TWO HIGH VALUES', highs, 'times.', end = " ")
print('('+ str(format((highs/rolls)*100, '.2f'))+'% of all rolls were high values)')
print('Along the way you rolled TWO EVENS', evens, 'times.', end = " ")
print('('+ str(format((evens/rolls)*100, '.2f'))+'% of all rolls were evens)')
print('Along the way you rolled TWO ODDS', odds, 'times.', end = " ")
print('('+ str(format((odds/rolls)*100, '.2f'))+'% of all rolls were odds)')
print('Along the way you rolled HIGH / LOW', high_low, 'times.', end = " ")
print('('+ str(format((high_low/rolls)*100, '.2f'))+'% of all rolls were high/low)')
print('Along the way you rolled A SUM VALUE', sums, 'times.', end = " ")
print('('+ str(format((sums/rolls)*100, '.2f'))+'% of all rolls were a sum value)')
print('Average roll for die #1:', format(total_d1/rolls, '.2f'))
print('Average roll for die #2:', format(total_d2/rolls, '.2f'))
