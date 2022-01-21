# Name: Xueyang Huang
# Date: April 1st
# Class section: 02
# Name of program: HuangXueyang_assign6_part4.py

# This is an escape room game.
# Main goal: find the key to the locked door
# solution: the key is in the safe in the bedroom downstairs
# 1st goal: find the password for the safe
# solution: go to the study upstairs and find the notebook
# 2nd goal: on the notebook it says the password is "my birthday", find the birthday
# solution: go to the bathroom for the phone
# 3rd goal: find the birthday on the phone
# solution: the birthday is stored in the "Calendar" app on the phone
# notes: user does not have to take anything he/she saw except the key and water
#        the safe in the bedroom can only allow up to 5 incorrect trials
#        if the trails are all used up, game over (but the user can choose to start over)
#        if the user want to renew his/her num of trials, they can drink the water in the kitchen
#        if the water is drunk, then the user has to start over
#        the password for the safe (or birthday) is randomly generate every time the game starts
#        this game is only using absolute orientation, so relative directions such as "left" or
#        "right" won't be identified
#        user can quit the game anytime by typing in "quit" commmand when prompted

import random

# global variables to keep track of what happened in the game so far
iswater = True
key_taken = False
safe_opened = False
false_tries = 0

# function:   valid_date
# input:      two integers (one is month and the other is day)
# processing: test if the input date is valid or not
# output:     boolean
def valid_date(month,day):
    if month < 1 or month > 12:
        return False
    else:
        # c. day (1,31) for month (1,3,5,7,8,10,12)
        if day < 1 or day > 31:
            return False
        else:
            # d. day must be in the range of (1,30) for month (4,6,9,11)
            if (day > 30 and month == 4 or day > 30 and month == 6 or day > 30
                and month == 9 or day > 30 and month == 11):
                return False
            else:
                # e. day (1,29) for month (2) AND leap years (no day 30 for all years)
                if day > 29 and month == 2:
                    return False
                else:
                    return True

# function:   main_room
# input:      none
# processing: inform the user what they need to do at the beginning of this game
#             by the letter on the table, present the locked door, two stairways
#             (to the bedroom and study)and two passages (to the kitchen and the bathroom)
# output:     return other functions
def main_room():

    print()
    print('--------------------------------------------------')
    print('This is the main room.')
    print('You look to the front and notice a white door. The door is locked.')
    print('You also see a letter lying on a table.')
    print('To the north is a stairway up to a study. To the south is a stairway down to a bedroom.')
    print('To the west is a passage to a bathroom, to the east is a passage to a kitchen.')

    global key_taken
    
    while True:
        
        choice = str.lower(input('\nWhat would you like to do? '))
        # they want to open the door
        if choice in ['open','door','unlock']:
            if key_taken == False:
                print('The door is locked and can only be opened by the key.')
            else:
                print('The door is open! You are free! Game over')
                return 'end'
        # they want to read the letter
        elif choice in ['read','letter']:
            print('You pick up the letter and start to read it.')
            print("""
Dear user,\n
    Welcome to this shabby little escape room game! In this game you are trapped
in this tiny house, and your goal is to figure out how to open the white door
in front of you and escape. You will start your journey in the main room, which
is the room you are in right now. Throughout the game, you will have to explore
all the rooms in this house, and get all the clues from which you will finally
find the key out. To start with, you cannot take anything in the house except
for the key and the water. You can read this letter as many times as you want.
You cannot move anything irrelevant to the game. Words indicating relative
directions such as "left" or "right" cannot be identified. Also, you will only
be connected to all the other rooms throught the main room. Trying to reach other
rooms when you are in a room other than the main room is impractical. Lastly, You
can quit the game anytime by simply typing in "quit" when prompted.\n
    And that's everything you need to know about the game. Good luck!
            """)
        # they want to mess with the table
        elif choice == 'table':
            print("I don't think the table has anything to do with the game.")
        # they don't know where they are
        elif choice == 'main room':
            print('You are already here.')
        # they want to go to the bedroom
        elif choice in ['south','bedroom','down','downstairs']:
            return bedroom
        # they want to go to the study
        elif choice in ['north','study','up','upstairs']:
            return study
        # they want to go to the bathroom
        elif choice in ['west','bathroom']:
            return bathroom
        # they want to go to the kitchen
        elif choice in ['east','kitchen']:
            return kitchen
        # they want to end the game immediately
        elif choice == 'quit':
            confirm = input('Do you want to quit the game immediately? (y/n) ')
            if confirm == 'y':
                print('Thanks for playing!')
                return 'end'
            else:
                continue
        # command not understood
        else:
            print("I don't understand that")


# function:   bedroom
# input:      none
# processing: present the user with items in the room (a bed and a locked safe)
# output:     return other functions
def bedroom():
    
    global key_taken
    global safe_opened
    global false_tries
    global month
    global day
    
    print()
    print('--------------------------------------------------')
    
    # if the safe is still locked
    if safe_opened == False:
        print('You are now in the bedroom. There is a bed and a safe here. The safe is locked.')
        while false_tries < 5:
            
            choice = str.lower(input('\nWhat would you like to do? '))
            # they want to open the safe
            if choice in ['open','safe','unlock']:
                trying = 'y'
                while trying == 'y':
                    password = input('Please enter the password (4-digit numbers only): ')
                    if password.isdigit() == True:
                        if password == str(month) + str(day):
                            print('The safe is now open. The key lies in there.')
                            safe_opened = True
                            take = str.lower(input('Do you want to take the key? (y/n) '))
                            if take == 'y':
                                print('You have the key now!')
                                key_taken = True
                                break
                            else:
                                break
                        else:
                            false_tries += 1
                            print('The password is incorrect.')
                            if false_tries == 5:
                                break
                            print('You are allowed for up to', (5 - false_tries), 'trials.')
                            trying = str.lower(input('Would you like to try again? (y/n): '))
                    else:
                        print('Please enter numbers only.')
            # they want to mess with the bed
            elif choice == 'bed':
                print("I don't think the bed has anything to do with the game.")
            # they don't know where they are
            elif choice == 'bedroom':
                print('You are already here.')
            # they want to go to the main room
            elif choice in ['north','main room','up','upstairs']:
                return main_room
            # they want to go to other rooms
            elif choice in ['study','bathroom','kitchen']:
                print('You cannot go to any rooms without going back to main room first.')
            # they want to end the game immediately
            elif choice == 'quit':
                confirm = input('Do you want to quit the game immediately? (y/n) ')
                if confirm == 'y':
                    print('Thanks for playing!')
                    return 'end'
                else:
                    continue
            # commands not understood
            else:
                print("I don't understand that.")
                
        if false_tries == 5:
            print('You have reached the upper limit of incorrect attempts.')
            print('The safe cannot be unlocked anymore. Game over')
            life = input('Would you like to start over? (y/n) ')
            if life == 'y':
                return main_room
            else:
                print('\nThanks for playing!')
                return 'end'
            
    # if it is not the first time they enter the room and the safe is open        
    else:
        print('You are now in the bedroom. There is a bed and a safe here. The safe is open.')
        while True:
            
            choice = str.lower(input('\nWhat would you like to do? '))
            # they want to mess with the bed
            if choice == 'bed':
                print("I don't think the bed has anything to do with the game.")
            # they don't know where they are
            elif choice == 'bedroom':
                print('You are already here.')
            # they want to go to the main room
            elif choice in ['north','main room','up','upstairs']:
                return main_room
            # they want to go to other rooms
            elif choice in ['study','bathroom','kitchen']:
                print('You cannot go to any rooms without going back to main room first.')
            # they want to end the game immediately
            elif choice == 'quit':
                confirm = input('Do you want to quit the game immediately? (y/n) ')
                if confirm == 'y':
                    print('Thanks for playing!')
                    return 'end'
                else:
                    continue
            # commands not understood
            else:
                print("I don't understand that.")
              

# function:   study
# input:      none
# processing: present the user with items in the room (a desk and a notebook)
# output:     return other functions
def study():
    
    print()
    print('--------------------------------------------------')
    print('You are now in the study. There is a notebook on a desk.')
    
    while True:
        
        choice = str.lower(input('\nWhat would you like to do? '))
        # they want to look at the notebook
        if choice in ['read','look','notebook']:
            print('You are looking at the notebook. The note wrote: "password hint: my birthday"')
        # they want to mess with the desk
        elif choice == 'desk':
            print("I don't think the desk has anything to do with the game.")
        # they don't know where they are
        elif choice == 'study':
            print('You are already here.')
        # they want to go to the main room
        elif choice in ['south','main room','down','downstairs']:
            return main_room
        # they want to go to other rooms
        elif choice in ['bedroom','bathroom','kitchen']:
            print('You cannot go to any rooms without going back to main room first.')
        # they want to end the game immediately
        elif choice == 'quit':
            confirm = input('Do you want to quit the game immediately? (y/n) ')
            if confirm == 'y':
                print('Thanks for playing!')
                return 'end'
            else:
                continue
        # commands not understood
        else:
            print("I don't understand that.")


# function:   bathroom
# input:      none
# processing: present the user with items in the room (a cell phone)
# output:     return other functions
def bathroom():

    global day
    global m_alpha
    
    print()
    print('--------------------------------------------------')
    print('You are now in the bathroom. Someone left a cell phone on the floor. The phone does not have any password.')

    while True:
        
        choice = str.lower(input('\nWhat would you like to do? '))
        # they want to check out the phone
        if choice in ['phone','cell phone','unlock']:
            print('You just unlocked the phone. The apps in this phone are Photo Album, Calendar, and Mailbox.')
            trying = 'y'
            while trying == 'y':
                app = str.lower(input('Which app do you want to open? '))
                if app == 'calendar':
                    print('You open the Calendar app and notice a schedule under', m_alpha, day, 'named "birthday".')
                    trying = str.lower(input('Would you like to open another app? (y/n) '))
                elif app == 'photo album':
                    print('There is no photo on this phone.')
                    trying = str.lower(input('Would you like to open another app? (y/n) '))
                elif app == 'mailbox':
                    print('There is no email on this phone.')
                    trying = str.lower(input('Would you like to open another app? (y/n) '))
                else:
                    print('There is no such app on this phone.')
                    trying = str.lower(input('Would you like to open another app? (y/n) '))
        # they don't know where they are
        elif choice == 'bathroom':
            print('You are already here.')
        # they want to go back to the main room
        elif choice in ['east','main room']:
            return main_room
        # they want to go to other rooms
        elif choice in ['bedroom','study','kitchen']:
            print('You cannot go to any rooms without going back to main room first.')
        # they want to end the game immediately
        elif choice == 'quit':
            confirm = input('Do you want to quit the game immediately? (y/n) ')
            if confirm == 'y':
                print('Thanks for playing!')
                return 'end'
            else:
                continue
        # commands not understood
        else:
            print("I don't understand that.")

# function:   kitchen
# input:      none
# processing: present the user with items in the room (a table and a glass of water)
# output:     return other functions
def kitchen():
    
    global iswater
    
    print()
    print('--------------------------------------------------')
    print('You are now in the kitchen. There is a glass of water on a table.')

    while True:
        choice = str.lower(input('\nWhat would you like to do? '))
        # they want to mess with the table
        if choice == 'table':
            print("I don't think the table has anything to do with the game.")
        elif choice == 'glass':
            print('There is a silver lettering on the glass: "Author: Xueyang Huang"')
        # they don't know where they are
        elif choice == 'kitchen':
            print('You are already here.')
        # they want to go to the main room
        elif choice in ['west','main room']:
            return main_room
        # they want to go to other rooms
        elif choice in ['bedroom','bathroom','study']:
            print('You cannot go to any rooms without going back to main room first.')
        elif choice in ['water','drink','consume']:
            if iswater == True:
                print('You just drank the MAGIC water. Oops! Now you have to start over.')
                iswater = False
                return main_room
        # they want to end the game immediately
        elif choice == 'quit':
            confirm = input('Do you want to quit the game immediately? (y/n) ')
            if confirm == 'y':
                print('Thanks for playing!')
                return 'end'
            else:
                continue
        # commands not understood
        else:
            print("I don't understand that.")
        
current_room = main_room
print()
print('You just woke up. You find out that you are in a strange room.', end = '')

while True:
    month = random.randint(1,12)
    day = random.randint(1,31)
    valid = valid_date(month,day)
    if valid == False:
        continue
    else:
        break
    
if month < 10:
    month = '0' + str(month)
if day < 10:
    day = '0' + str(day)

while True:
    if month == '01':
        m_alpha = 'January'
    elif month == '02':
        m_alpha = 'February'
    elif month == '03':
        m_alpha = 'March'
    elif month == '04':
        m_alpha = 'April'
    elif month == '05':
        m_alpha = 'May'
    elif month == '06':
        m_alpha = 'June'
    elif month == '07':
        m_alpha = 'July'
    elif month == '08':
        m_alpha = 'August'
    elif month == '09':
        m_alpha = 'September'
    elif month == 10:
        m_alpha = 'October'
    elif month == 11:
        m_alpha = 'November'
    else:
        m_alpha = 'December'
    next_action = current_room()
    if next_action == 'end':
        break
    else:
        current_room = next_action
        if iswater == False or false_tries == 5:
            iswater = True
            key_taken = False
            safe_opened = False
            false_tries = 0
            while True:
                month = random.randint(1,12)
                day = random.randint(1,31)
                valid = valid_date(month,day)
                if valid == False:
                    continue
                else:
                    break
            if month < 10:
                month = '0' + str(month)
            if day < 10:
                day = '0' + str(day)
