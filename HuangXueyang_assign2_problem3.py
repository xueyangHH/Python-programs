# Name: Xueyang Huang
# Date: Feb.5
# Class section: 02
# Name of the program: HuangXueyang_assign2_problem3

# Print out the title
print('Minecraft block distance calculator')
print()

# Ask the user for Block #1's x component
block1x = float(input('Block #1 x: '))

# Ask the user for Block #1's y component
block1y = float(input('Block #1 y: '))

# Ask the user for Block #1's z component
block1z = float(input('Block #1 z: '))

# Ask the user for Block #2's x component
block2x = float(input('Block #2 x: '))

# Ask the user for Block #2's y component
block2y = float(input('Block #2 y: '))

# Ask the user for Block #2's z component
block2z = float(input('Block #2 z: '))
print()

# Compute x, y and z distance between the two blocks
xdist = abs(block2x - block1x)
ydist = abs(block2y - block1y)
zdist = abs(block2z - block1z)

# compute the straight-line distance between the two blocks formatted to two decimal places.
SL_dist = ((block2x-block1x)**2+(block2y-block1y)**2+(block2z-block1z)**2)**.5

# Print out the results
print('X distance:', int(xdist))
print('Y distance:', int(ydist))
print('Z distance:', int(zdist))
print('Straight line distance:', format(SL_dist, '.2f'))
