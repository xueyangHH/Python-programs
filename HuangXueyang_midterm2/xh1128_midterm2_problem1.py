import random

lowers = "abcdefghijklmnopqrstuvwxyz"
uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "01234567890"
symbols = "!@#$%^&*()[]{}?><,.-="
mixed = lowers + uppers + digits + symbols
listing = ''

while True:
    command = str.lower(input('(g)enerate, (l)ist or (q)uit: '))
    if command == 'g':
        password = ''
        pattern = str.lower(input('Enter a pattern: '))
        for d in pattern:
            if d not in ['u', 'l', 'd', 's', '?']:
                print('Invalid characters used in pattern, operation canceled\n')
                invalid = True
                break
            else:
                invalid = False
                continue
        if invalid == True:
            continue
        else:
            for i in range(len(pattern)):
                in_u = random.randint(0,25)
                in_l = random.randint(0,25)
                in_d = random.randint(0,9)
                in_s = random.randint(0,20)
                in_m = random.randint(0,83)
                if pattern[i] == 'u':
                    password += uppers[in_u]
                elif pattern[i] == 'l':
                    password += lowers[in_l]
                elif pattern[i] == 'd':
                    password += digits[in_d]
                elif pattern[i] == 's':
                    password += symbols[in_s]
                else:
                    password += mixed[in_m]
            listing += password + '\n'
            print('Your password is:', password)
            print()
    elif command == 'l':
        print(listing)
    elif command == 'q':
        break
    else:
        print('Unknown command\n')
        continue
