'''
# first program in python
# input two numbers, add them together, print them out
# wfp, 9/1/07; rje, 5/5/14

num_str1 = input('Please enter an integer: ')
num_str2 = input('Please enter a floating point number: ')

int1 = int(num_str1)
float1 = float(num_str2)

print('The numbers are: ',int1,' and ',float1)
print('Their sum is: ',int1+float1, 'Their product is:',int1*float1)
'''


rods = int(input('Input rods: '))
meters = rods * 5.0292
furlong = rods/40
mile = meters / 1609.34
feet = meters / 0.3048
time = (mile/3.1)*60
print('You input', rods, 'rods.\n')
print('Conversions')
print('Meters:', meters)
print('Feet:', feet)
print('Miles:', mile)
print('Furlongs:', furlong)
print('Minutes to walk 1.0 rods:', time)
