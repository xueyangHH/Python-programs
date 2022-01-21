# Name: Xueyang Huang
# Date: Feb.5
# Class section: 02
# Name of the program: HuangXueyang_assign2_problem4

# Print out the title
print('--------------------------------------------------------------')
print(format('mL Conversion Calculator', '^63s'))
print('--------------------------------------------------------------')
print()

# Ask the user to enter in a number of milliliters
mL = float(input('How many mL would you like to convert? '))
# The following line could cause a syntax error if I forget the delimiters around .2f
# print(format(mL, .2f), 'mL ...')
print(format(mL, '.2f'), 'mL ...')
print()

# Convert the supplied input into tsp, tbsp, uL and nL
tsp = mL*0.202884
tbsp = tsp/3
# The following line could cause a logic error if I mistype the equation as uL = mL/1000 instead of uL = mL*1000
# uL = mL/1000
uL = mL*1000
# The following line could cause a run-time error if I reverse the previous and the following line because the variable uL would then be undefined
# nL = uL*1000
# uL = mL*1000
nL = uL*1000

# Format the input and the converted data
# The following lines could cause a logic error if I mistype the ">" symbol as "<"
# ftsp = format(tsp, '<20.2f')
# ftbsp = format(tbsp, '<20.2f')
# fuL = format(uL, '<20,.2f')
# fnL = format(nL, '<20,.2f')
ftsp = format(tsp, '>20.2f')
ftbsp = format(tbsp, '>20.2f')
fuL = format(uL, '>20,.2f')
fnL = format(nL, '>20,.2f')

# Print out the results
# The following lines could cause a logic error if I miscount the space that I need for formatting, i.e. 17s instead of 18s
# print(format('... in teaspoons', '17s'), ftsp, 'tsp')
# print(format('... in tablespoons', '17s'), ftbsp, 'tbsp')
# print(format('... in microliters', '17s'), fuL, 'uL')
# print(format('... in nanoliters', '17s'), fnL, 'nL')
print(format('... in teaspoons', '18s'), ftsp, 'tsp')
print(format('... in tablespoons', '18s'), ftbsp, 'tbsp')
print(format('... in microliters', '18s'), fuL, 'uL')
print(format('... in nanoliters', '18s'), fnL, 'nL')
