# Name: Xueyang Huang
# Date: Jan.31
# class section: 02
# Name of the program: HuangXueyang_assign1_problem2.py

# Ask the user to enter their names
name1 = input('Please enter name #1: ')
name2 = input('Please enter name #2: ')
name3 = input('Please enter name #3: ')

# Shuffle and print out the names
print('')
print('Here are your names in every possible order:')
print('--------------------------------------------')
print('')

# First possible order
print('1. ', name1, ', ', name2, ', ', name3, sep='')
print('')

# Second possible order
print('2. *', name1, '* *', name3, '* *', name2, '*', sep='')
print('')

# Third possible order
print('3. ', end='')
print(name2, name1, name3, sep='-')
print('')

# Fourth possible order
print('4.', end='')
print(name2, '\n', name3, '\n', name1, sep='')
print('')

# Fifth possible order
print('5. ', end='')
print(name3, '\n', name2, '\n', name1, sep='   ')
print('')

# Sixth possible order
print('6. ', end='')
print(name3, '\n', '---', name1, '\n', '---', name2, sep='')

