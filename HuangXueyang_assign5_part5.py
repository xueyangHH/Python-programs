# Name: Xueyang Huang
# Date: March 16th
# Class section: 02
# Name of program: HuangXueyang_assign5_part5.py

# Challenge #1: Arch
while True:   # write a while loop to validate the user input of width
    width = int(input3d('Enter a width that can be evenly divided by 50(100-1000):'))
    if (width < 100 or width > 1000) or (width % 50 != 0):
        print('Invalid width, try again.')
    else:
        break

while True:   # write a while loop to validate the user input of height
    height = int(input3d('Enter a height that can be evenly divided by 50(100-500):'))
    if (height < 100 or height > 500) or (height % 50 != 0):
        print('Invalid height, try again.')
    else:
        break

# modify the user input of width/height so that they can fit with PySculpture3D
width_m = width / 2
height_m = height - 25

# write three for loops to build the arch
for w in range(-width_m, width_m + 1, 50):
    cube(w,height,0)

for h1 in range(0, height_m, 50):
    cube(-width_m,h1,0)

for h2 in range(0, height_m, 50):
    cube(width_m,h2,0)



# Challenge #2: Random Branching
import random

while True:   # write a while loop to validate the random input
    height = random.randint(250, 500)   # generate a random height
    if height % 25 != 0:
        continue
    else:     # validated! go on to write a for loop to build the stem along y axis
        for y in range(0, height + 1, 25):
            cube(0,y,0,25,25,25)
            offshoot = random.randint(1,2)   # take a chance to branch
            if offshoot == 1:   # if it gets 1, no branching
                continue
            else:   # if it gets 2, then branch
                while True:   # write a while loop to validate the random input
                    width = random.randint(25, 100)   # generate a random width
                    if width % 25 != 0:
                        continue
                    else:     # validated! go on to write a for loop to build a branch
                        orient = random.randint(1,2)   # take a chance to branch left or right
                        for x in range(0, width + 1, 25):
                            if orient == 1:   # right branching (towards the positive side of x axis)
                                cube(x,y,0,25,25,25)
                            else:   # left branching (towards the negative side of x axis)
                                cube(-x,y,0,25,25,25)
                        break   # remember to break the while loop or it'll be a logic error
        break   # same
