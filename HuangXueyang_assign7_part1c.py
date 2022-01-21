# Name: Xueyang Huang
# Date: April 10th
# Class section: 02
# Name of program: HuangXueyang_assign7_part1c.py

import random

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
    uppers = 0
    lowers = 0
    digits = 0
    special = 0
    invalid = 0
    for c in password:
        if c.isupper():
            uppers += 1
        elif c.islower():
            lowers += 1
        elif c.isdigit():
            digits += 1
        elif 35 <= ord(c) <= 38:
            special += 1
        else:
            invalid += 1
    print('* # of uppercase characters in the password:', uppers)
    print('* # of lowercase characters in the password:', lowers)
    print('* # of digits in the password:', digits)
    print('* # of special characters in the password:', special)
    print('* # of invalid characters in the password:', invalid)
    if (size2 >= 8 and uppers > 0 and lowers
        > 0 and digits > 0 and special > 0 and non_repeat):
        print('Password is valid!')
        break
    else:
        print('Password is invalid')
        while True:
            fixing = str.lower(input('\nWould you like us to fix your password for you? '))
            if fixing == 'yes' or fixing == 'no':
                break
            else:
                print("I don't understand that.")
        if fixing == 'no':
            continue
        else:
            if password != '':     # if user actually enters something for password
                original_password = password
                temp_password = ''
                # any invalid characters like space or !
                invalid = 0
                for c in original_password:
                    if (35 <= ord(c) <= 38 or 48 <= ord(c) <= 57 or 65 <= ord(c) <= 90
                        or 97 <= ord(c) <= 122):
                        temp_password += c
                    else:
                        invalid += 1
                        continue
                if invalid > 0 :
                    print('* New password with invalid characters removed:', temp_password)
                else:   # good password need no fix
                    temp_password = original_password
                # username in password
                if username in temp_password:
                    choice = random.randint(1,4)
                    if choice == 1:
                        in_char = random.randint(65,90)
                    elif choice == 2:
                        in_char = random.randint(97,122)
                    elif choice == 3:
                        in_char = random.randint(48,57)
                    else:
                        in_char = random.randint(35,38)
                    spot = random.randint(0,len(username)-2)
                    pw_holder = ''
                    for i in range(0,len(temp_password)):
                        if temp_password[i] not in username:
                            pw_holder += temp_password[i]
                        else:
                            if temp_password[i:i+len(username)] != username:
                                pw_holder += temp_password[i]
                            else:   # immediately enter the for loop after getting
                                    # the first letter of the username
                                for i in range(i,i+len(username)):
                                    pw_holder += temp_password[i]
                                    if temp_password[i] == username[spot]:
                                        pw_holder += chr(in_char)
                                break   # immediately break after username is added
                                        # to the password
                    for i in range(i+1, len(temp_password)): # add all the rest part
                        pw_holder += temp_password[i]
                    temp_password = pw_holder
                    print('Username is in password - interrupting string to remove it', temp_password)
                # lack of valid characters
                if uppers == 0 or lowers == 0 or digits == 0 or special == 0:
                    final_pw = ''
                    in_upper = random.randint(65,90)
                    in_lower = random.randint(97,122)
                    in_digit = random.randint(48,57)
                    in_special = random.randint(35,38)
                    for d in range(0,len(temp_password)):
                        if d != len(temp_password)-1:
                            spot2 = random.randint(1,2) # user random number to  decide whether to add a character or not
                            final_pw += temp_password[d]
                            if spot2 == 1: # adding
                                if uppers == 0:
                                    final_pw += chr(in_upper)
                                    uppers += 1
                                    print('* Adding a random uppercase character at a random position:', final_pw+temp_password[d+1::])
                                elif lowers == 0:
                                    final_pw += chr(in_lower)
                                    lowers += 1
                                    print('* Adding a random lowercase character at a random position:', final_pw+temp_password[d+1::])
                                elif digits == 0:
                                    final_pw += chr(in_digit)
                                    digits += 1
                                    print('* Adding a random digit character at a random position:', final_pw+temp_password[d+1::])
                                elif special == 0:
                                    final_pw += chr(in_special)
                                    special += 1
                                    print('* Adding a random special character at a random position:', final_pw+temp_password[d+1::])
                            else:          # not adding
                                continue
                        else:   # if got really unlucky and not adding all lacking characters
                                # before exiting the for loop
                            final_pw += temp_password[d]
                            if uppers == 0:
                                final_pw += chr(in_upper)
                                uppers += 1
                                print('* Adding a random uppercase character at a random position:', final_pw)
                            if lowers == 0:
                                final_pw += chr(in_lower)
                                lowers += 1
                                print('* Adding a random lowercase character at a random position:', final_pw)
                            if digits == 0:
                                final_pw += chr(in_digit)
                                digits += 1
                                print('* Adding a random digit character at a random position:', final_pw)
                            if special == 0:
                                final_pw += chr(in_special)
                                special += 1
                                print('* Adding a random speicial character at a random position:', final_pw)
                else:   # good password need no fix
                    final_pw = temp_password
                # not long enough
                if len(final_pw) < 8:
                    final_pw_l = ''
                    if len(final_pw) == 4: 
                        for d in range(4):
                            choice = random.randint(1,4)
                            if choice == 1:
                                change = 'upppercase'
                                in_char = random.randint(65,90)
                            elif choice == 2:
                                change = 'lowercase'
                                in_char = random.randint(97,122)
                            elif choice == 3:
                                change = 'digit'
                                in_char = random.randint(48,57)
                            else:
                                change = 'special'
                                in_char = random.randint(35,38)
                            final_pw_l += final_pw[d]
                            final_pw_l += chr(in_char)
                            print('* Adding a random', change, 'character at a random position:', final_pw_l+final_pw[d+1::])
                    else:
                        track = 0 # keep track of how many additional characters
                        for d in range(0,len(final_pw)):
                            choice = random.randint(1,4)
                            if choice == 1:
                                change = 'upppercase'
                                in_char = random.randint(65,90)
                            elif choice == 2:
                                change = 'lowercase'
                                in_char = random.randint(97,122)
                            elif choice == 3:
                                change = 'digit'
                                in_char = random.randint(48,57)
                            else:
                                change = 'special'
                                in_char = random.randint(35,38)
                            if d != len(final_pw)-1:
                                spot2 = random.randint(1,2)
                                final_pw_l += final_pw[d]
                                if spot2 == 1:  # adding
                                    if track < 8 - len(final_pw): # not reaching 8
                                        final_pw_l += chr(in_char)
                                        print('* Adding a random', change, 'character at a random position:', final_pw_l+final_pw[d+1::])
                                        track += 1
                                    else: # as soon as reaching 8 break
                                        continue
                                else:   # not adding
                                    continue
                            else:   # if unlucky enough
                                final_pw_l += final_pw[d]
                                while len(final_pw_l) < 8:
                                    choice = random.randint(1,4)
                                    if choice == 1:
                                        change = 'upppercase'
                                        in_char = random.randint(65,90)
                                    elif choice == 2:
                                        change = 'lowercase'
                                        in_char = random.randint(97,122)
                                    elif choice == 3:
                                        change = 'digit'
                                        in_char = random.randint(48,57)
                                    else:
                                        change = 'special'
                                        in_char = random.randint(35,38)
                                    final_pw_l += chr(in_char)
                                    print('* Adding a random', change, 'character at a random position:', final_pw_l)

                    print('Your new password is', final_pw_l)    
                            
                else:   # good password need no fix
                    print('Your new password is', final_pw)
            else:   # if the user does not enter any password at all
                while True:
                    new_pw = ''
                    for i in range(8):
                        choice = random.randint(1,4)
                        if choice == 1:
                            change = 'uppercase'
                            in_char = random.randint(65,90)
                            uppers += 1
                        elif choice == 2:
                            change = 'lowercase'
                            in_char = random.randint(97,122)
                            lowers += 1
                        elif choice == 3:
                            change = 'digit'
                            in_char = random.randint(48,57)
                            digits += 1
                        else:
                            change = 'special'
                            in_char = random.randint(35,38)
                            special += 1
                        new_pw += chr(in_char)
                        print('* Adding a random', change, 'character at a random position:', new_pw)
                    if uppers == 0 or lowers == 0 or digits == 0 or special == 0 or username in new_pw:
                        uppers = 0    # if any of those requirements are not met, loop again
                        lowers = 0
                        digits = 0
                        special = 0
                        continue
                    else:
                        print('Your new password is', new_pw)
                        break
        break        
