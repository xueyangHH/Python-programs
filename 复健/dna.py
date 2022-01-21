str1 = input('String 1: ').lower()
str2 = input('String 2: ').lower()
str_len = [len(str1), len(str2)]
while True:
    while True:
        print('\nWhat do you want to do: ')
        command = input('a (add)\nd (delete)\ns (Score)\nq (quit): ')
        if command == 'a' or command == 'd' or command == 's' or command == 'q':
            break
        else:
            print('Cannot read command\n')
    if command == 'a':
        while True:
            choice_a = input('\nWork on which string (1 or 2): ')
            if choice_a == '1' or choice_a == '2':
                if choice_a == '1':
                    str_a = str1
                elif choice_a == '2':
                    str_a = str2
                break
            else:
                print('Cannot read')
        while True:
            pos_a = int(input('Before what index: '))
            if pos_a not in range(len(str_a)+1):
                print('Index out of range\n')
            else:
                break
        str_copy = ''
        for i in range(len(str_a)):
            if i == pos_a:
                str_copy += '-' + str_a[i]
            else:
                str_copy += str_a[i]
        if choice_a == '1':
            str1 = str_copy
        elif choice_a == '2':
            str2 = str_copy
    elif command == 'd':
        while True:
            choice_d = input('\nWork on which string (1 or 2): ')
            if choice_d == '1' or choice_d == '2':
                if choice_d == '1':
                    str_d = str1
                elif choice_d == '2':
                    str_d = str2
                break
            else:
                print('Cannot read')
        while True:
            pos_d = int(input('Delete what index: '))
            if pos_d not in range(len(str_d)+1):
                print('Index out of range\n')
            else:
                break
        str_copy = ''
        for i in range(len(str_d)):
            if i == pos_d:
                continue
            else:
                str_copy += str_d[i]
        if choice_d == '1':
            str1 = str_copy
        elif choice_d == '2':
            str2 = str_copy
    elif command == 's':
        str1_copy = ''
        str2_copy = ''
        match = 0
        mismatch = 0
        for i in range(max(str_len)):
            if i in range(len(str1)) and i in range(len(str2)):
                if str1[i] == str2[i]:
                    str1_copy += str1[i]
                    str2_copy += str2[i]
                    match += 1
                else:
                    str1_copy += str1[i].upper()
                    str2_copy += str2[i].upper()
                    mismatch += 1
            else:
                if len(str1) < len(str2):
                    str1_copy += '-'
                    str2_copy += str2[i].upper()
                    mismatch += 1
                else:
                    str2_copy += '-'
                    str1_copy += str1[i].upper()
                    mismatch += 1
        print('\nMatches:', match, 'Mismatches:', mismatch)
        print('Str1:', str1_copy)
        print('Str2:', str2_copy)
    else:
        break
        









