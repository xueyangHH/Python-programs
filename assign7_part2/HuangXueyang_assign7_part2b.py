# Name: Xueyang Huang
# Date: April 8th
# Class section: 02
# Name of program: HuangXueyang_assign7_part2b.py

# make sure to save this file along with part2a in one folder
# at least I did it on my computer and it runned perfectly
# if you do not and the program crashes, it is not my fault
from HuangXueyang_assign7_part2a import *

while True:
    
    while True:
        choice = input('(e)ncode, (d)ecode or (q)uit: ')
        
        if choice == 'e' or choice == 'd':
            while True:
                num = input('Enter a number between 1 and 5: ')
                if num.isdigit() == True:
                    if 1 <= int(num) <= 5:
                        break
                    else:
                        print('Invalid number, try again.')
                else:
                    print('Invalid input, try again.')
            
            if choice == 'e':
                phrase = input('Enter a phrase to encode: ')
                word1 = add_letters(phrase,int(num))
                word2 = shift_characters(word1,int(num))
                print('Your encoded word is:', word2, '\n')
            else:
                phrase = input('Enter a phrase to decode: ')
                word1 = remove_letters(phrase,int(num))
                word2 = shift_characters(word1,-int(num))
                print('Your decoded word is:', word2, '\n')
                
        elif choice == 'q':
            break
        
        else:
            print('Invalid, try again.\n')

    break
    
