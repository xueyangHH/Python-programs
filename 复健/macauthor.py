print('''
This is a puzzle favored by Gen. MacArthur. You will be asked to secretly type
in your birth month (as an integer) and your age
The computer will make a special calculation, yielding a new integer
The computer will then calculate, using only that special number, your birth
month and age
''')
month = input('Give me your birth month: ')
age = input('Give me your age: ')
num = (((int(month) * 2) + 5) * 50) + int(age) - 365
print('The special number is: ', num)
processed_n = num + 115
print('The computer calculates then that you were born in the', str(processed_n)[0],
      'month and are', str(processed_n)[1:], 'years old')
