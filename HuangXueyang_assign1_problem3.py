# Name: Xueyang Huang
# Date: Jan.31
# Class section: 02
# Name of the program: HuangXueyang_assign1_problem3.py

# print out the title
print('--------------------------------------------------------------')
print(format('mL to US Fluid Volume Units', '>43s'))
print('--------------------------------------------------------------')

# create the variables and format the names of the units
unit1 = format('mL:', '16s')
unit2 = format('tsp:', '16s')
unit3 = format('tbsp:', '16s')
unit4 = format('cup(s):', '16s')
unit5 = format('pint(s):', '16s')
unit6 = format('quart(s):', '16s')
unit7 = format('gallon(s):', '16s')
unit8 = format('fl oz:', '16s')

# create the variables for the numeric (converted) data
mLn = 250.0
tspn = mLn*0.202884
tbspn = tspn/3
cupn = tbspn/16
pintn = cupn/2
quartn = pintn/2
gallonn = quartn/4
flozn = mLn/29.5735

# format the numeric data
fmLn = format(mLn, '.1f')
ftspn = format(tspn, '.15f')
ftbspn = format(tbspn, '.3f')
fcupn = format(cupn, '.7f')
fpintn = format(pintn, '.8f')
fquartn = format(quartn, '.9f')
fgallonn = format(gallonn, '.11f')
fflozn = format(flozn, '.15f')

# display the results
print('\t'+unit1+fmLn)
print('\t'+unit2+ftspn)
print('\t'+unit3+ftbspn)
print('\t'+unit4+fcupn)
print('\t'+unit5+fpintn)
print('\t'+unit6+fquartn)
print('\t'+unit7+fgallonn)
print('\t'+unit8+fflozn)

# ending line
print('--------------------------------------------------------------')
