# Name: Xueyang Huang
# Date: April 7th
# Class section: 02
# Name of program: HuangXueyang_assign7_part1a.py

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
