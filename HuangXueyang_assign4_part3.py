# Name: Xueyang Huang
# Date: February 26th
# Class section: 02
# Name of program: HuangXueyang_assign4_part4.py

# import the modules
import random
import math
import time

# set up accumulator variables to keep track of valid/invalid throws
red = 0
blue = 0
green = 0
darkgrey = 0
lightgrey = 0
misses = 0

# write a while loop to generate number of throws
while True:
    # ask the user to enter a number of throws
    throws = int(input('Number of throws: '))
    # keep track of how many throws are yet to complete
    throws_left = throws
    # determine if the number of throws entered is valid or not
    if throws <= 0:
        print('Invalid, try again!')
        continue
    else:
        break

# ask the user if they want to draw their output with turtle
while True:
    consent = input('Would you like to draw your results using turtle graphics? (yes/no): ')
    # determine if the response is valid or not
    if consent == 'yes' or consent == 'no':
        # for the previous question, if the user chose yes, import turtle graphics       
        if consent == 'yes':
            # set up turtle
            import turtle
            turtle.tracer(0)
            turtle.setup(800,500)
            turtle.pensize(1)
            turtle.setheading(135)
            turtle.penup()
        break
    else:
        print('Invalid, try again')

# keep track of the time
starttime = time.time()

# write a while loop to continuously throw at these shapes
while throws_left > 0:
    
    # generate a random coordinate with two dimensions
    x = random.uniform(0,800)
    y = random.uniform(0,500)

    # create distance variables
    dist_blue = math.sqrt((x - 400) ** 2 + (y - 150) ** 2)
    dist_smallgrey = math.sqrt(((x - 150) ** 2 + (y - 200) ** 2))
    dist_biggrey = math.sqrt(((x - 150) ** 2 + (y - 300) ** 2))
    
    # set up the ranges of the shapes
    # determine if the random throw falls within the ranges of these shapes
    # red rectangle: x [350, 450], y [300,450]
    if 350 < x < 450 and 300 < y < 450:
        red += 1
        throws_left -= 1
        # if the user want to draw the output, run the turtle graphics
        # because turtle uses a Cartesian coordinate plane, the value of x and y
        # have to be converted so that it can adapt to the coordinates on the canvas
        if consent == 'yes':
            turtle.goto(x - 395, 255 - y)
            turtle.pendown()
            turtle.pencolor('red')
            turtle.forward(10 * math.sqrt(2))
            turtle.penup()
            continue
    
    # green rectangle with holes: x [550,750], y [50,450], excluding
    # x [600,700] and y [100,200]
    # x [600,650] and y [250,300]
    # x [650,700] and y [350,400]
    elif ((550 < x < 750 and 50 < y < 450) and not(600 < x < 700 and 100 < y < 200)
        and not(600 < x < 650 and 250 < y < 300) and not(650 < x < 700 and 350 < y < 400)):
        green += 1
        throws_left -= 1
        # drawing
        if consent == 'yes':
            turtle.goto(x - 395, 255 - y)
            turtle.pendown()
            turtle.pencolor('green')
            turtle.forward(10 * math.sqrt(2))
            turtle.penup()
            continue
    
    # blue circle: if the distance between (x,y) and (400,150) is smaller or
    # equal to 100, then the dart hits the blue circle
    elif dist_blue <= 100:
        blue += 1
        throws_left -= 1
        # if the user want to draw the output, run the turtle graphics
        if consent == 'yes':
            turtle.goto(x - 395, 255 - y)
            turtle.pendown()
            turtle.pencolor('blue')
            turtle.forward(10 * math.sqrt(2))
            turtle.penup()
            continue
    
    # grey BB-8: if the distance between (x,y) and (150,200) is smaller or
    # equal to 50
    # or if the distance between (x,y) and (150,300) is smaller or equal to 100
    # then the dart hits the grey BB-8
    # and if the dart hits the intersection of the two grey circles, then the dart hits
    # the light grey area. Otherwise, the dart hits the dark grey area
    elif dist_smallgrey <= 50 and dist_biggrey <= 100:
        lightgrey += 1
        throws_left -= 1
        # drawing
        if consent == 'yes':
            turtle.goto(x - 395, 255 - y)
            turtle.pendown()
            turtle.pencolor('light grey')
            turtle.forward(10 * math.sqrt(2))
            turtle.penup()
            continue
    
    elif ((dist_smallgrey <= 50 and dist_biggrey > 100) or
          (dist_smallgrey > 50 and dist_biggrey <= 100)):
        darkgrey += 1
        throws_left -= 1
        # drawing
        if consent == 'yes':
            turtle.goto(x - 395, 255 - y)
            turtle.pendown()
            turtle.pencolor('dark grey')
            turtle.forward(10 * math.sqrt(2))
            turtle.penup()
            continue

    # the throws that missed the targets
    else:
        throws_left -= 1
        continue

# stop timing
endtime = time.time()

# compute the time elapsed
elapse = round((endtime - starttime), 2)

# if the user chose to draw the results, then update turtle
if consent == 'yes':
    turtle.update()

# calculate the chance that the dart hit/missed any of these shapes
totalhits = red + blue + green + darkgrey + lightgrey
misses = throws - totalhits
red_chance = format((red/throws)*100, '.2f')
blue_chance = format((blue/throws)*100, '.2f')
green_chance = format((green/throws)*100, '.2f')
darkgrey_chance = format((darkgrey/throws)*100, '.2f')
lightgrey_chance = format((lightgrey/throws)*100, '.2f')
misses_chance = format((misses/throws)*100, '.2f')

# print out the results to the user
print('\nTotal time elapsed:', elapse, 'seconds')
print(format('Red:', '<11s') + format(red, '>11,d') + ' (' + red_chance + '%)')
print(format('Blue:', '<11s') + format(blue, '>11,d') + ' (' + blue_chance + '%)')
print(format('Green:', '<11s') + format(green, '>11,d') + ' (' + green_chance + '%)')
print(format('Dark Grey:', '<11s') + format(darkgrey, '>11,d') + ' (' + darkgrey_chance + '%)')
print(format('Light Grey:', '<11s') + format(lightgrey, '>11,d') + ' (' + lightgrey_chance + '%)')
print(format('Misses:', '<11s') + format(misses, '>11,d') + ' (' + misses_chance + '%)')
