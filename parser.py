'''
a = str.lower(input('hi:'))
if a in ['downstairs','letter']:
    print('okay')
'''
'''
password = input('iiiii')
if password.isnumeric() == True:
    print('hi')
else:
    print('no')
'''
'''
print("""
Dear user,\n
    Welcome to this shabby little escape room game! In this game you are trapped
in this tiny house, and your goal is to figure out how to open the white dooor
in front of you and escape. You will start your journey in the main room, which
is the room you are in right now. Throughout the game, you will have to explore
all the rooms in this house, and get all the clues from which you will finally
find the key out. To start with, you cannot take anything in the house except
for the key and the water. You can read this letter as many times as you want.
You cannot move anything irrelevant to the game. Also, you will only be connected
to all the other rooms throught the main room. Trying to reach other rooms when
you are in a room other than the main room is impractical.\n
    And that's everything you need to know about the game. Good luck!
""")
'''
import random

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
                if day > 28 and month == 2:
                    return False
                else:
                    return True

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

print(m_alpha, day)
