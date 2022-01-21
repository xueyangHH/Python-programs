# Name: Xueyang Huang
# Date: April 7th
# Class section: 02
# Name of program: HuangXueyang_assign7_part1b.py

while True:
    username = input('Enter a username: ')
    size = len(username)
    print('* Length of username: ', size)
    print('* All characters are alpha-numeric:', username.isalnum())
    print('* First & last characters are not digits:', (username[0].isdigit() == False) and (username[-1].isdigit() == False))
    uppers = 0
    lowers = 0
    digits = 0
    for c in username:
        if c.isupper():
            uppers += 1
        elif c.islower():
            lowers += 1
        elif c.isdigit():
            digits += 1
    print('* # of uppercase characters in the username:', uppers)
    print('* # of lowercase characters in the username:', lowers)
    print('* # of digits in the username:',digits)
    if (size >= 8 and size <= 15 and username.isalnum() == True and 
        (username[0].isdigit() == False) and (username[-1].isdigit() == False)
        and uppers >= 1 and lowers >= 1 and digits >= 1):
        print('Username is valid!')
        break
    else:
        print('Username is invalid, please try again\n')

while True:
    password = input('\nEnter a password: ')
    size2 = len(password)
    print('* Length of password:', size2)
    if username in password:
        non_repeat = False
        print('* Username is part of password: True')
    else:
        non_repeat = True
        print('* Username is part of password: False')
    uppers2 = 0
    lowers2 = 0
    digits2 = 0
    special = 0
    for c in password:
        if c.isupper():
            uppers2 += 1
        elif c.islower():
            lowers2 += 1
        elif c.isdigit():
            digits2 += 1
        elif 35 <= ord(c) <= 38:
            special += 1
    print('* # of uppercase characters in the password:', uppers2)
    print('* # of lowercase characters in the password:', lowers2)
    print('* # of digits in the password:', digits2)
    print('* # of special characters in the password:', special)
    if (size2 >= 8 and uppers2 > 0 and lowers2
        > 0 and digits2 > 0 and special > 0 and non_repeat):
        print('Password is valid!')
        break
    else:
        print('Password is invalid, please try again')
            
