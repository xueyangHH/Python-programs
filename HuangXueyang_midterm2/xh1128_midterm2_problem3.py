string = input('Enter an encoded string: ')
decoding = input('Enter decoding instructions: ')

for i in range(0, len(decoding), 2):

    if decoding[i] == 'S':
        if decoding[i+1] == 'W':
            if len(string) % 2 == 0:
                middle = (len(string) // 2) + 1
                sec_half = string[middle-1::]
                fir_half = string[0:middle-1:]
                swap = sec_half+fir_half
                string = swap
            else:
                middle = (len(string)-1)//2 + 1
                sec_half = string[middle-1::]
                fir_half = string[0:middle-1:]
                swap = sec_half+fir_half
                string = swap
            print('SW', string)
        else:
            i += 1
    elif decoding[i] == '-':
        if decoding[i+1].isdigit() == True:
            new_str = ''
            for d in string:
                new_str += chr(ord(d) - int(decoding[i+1]))
            string = new_str
            print(decoding[i:i+2], string)
        else:
            i += 1
    elif decoding[i] == '+':
        if decoding[i+1].isdigit() == True:
            new_str = ''
            for d in string:
                new_str += chr(ord(d) + int(decoding[i+1]))
            string = new_str
            print(decoding[i:i+2], string)
        else:
            i += 1
    else:
        i += 1
