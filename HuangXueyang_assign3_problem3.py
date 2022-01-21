# Name: Xueyang Huang
# Date: February 19th
# Class section: 02
# Name of program: HuangXueyang_assign3_problem3.py

# ask the user for a date (8 digits)
date = int(input('Enter a date in YYYYMMDD format (i.e. 20200128 for January 28th, 2020): '))
# separate year, month and day from the 8-digit date
year = int(date // 10000)
month = int((date % 10000 - date % 100)/100)
day = int(date % 100)
# determine the date if:
# 1. the date is invalid
# a. year must be in the range of (1,9999)
if year < 0 or year > 9999:
    print("That's not a valid date!")
else:
    # b. month must be in the range of (1,12)
    if month < 1 or month > 12:
        print("That's not a valid date!")
    else:
        # c. day (1,31) for month (1,3,5,7,8,10,12)
        if day < 1 or day > 31:
            print("That's not a valid date!")
        else:
            # d. day must be in the range of (1,30) for month (4,6,9,11)
            if (day > 30 and month == 4 or day > 30 and month == 6 or day > 30
                and month == 9 or day > 30 and month == 11):
                print("That's not a valid date!")
            else:
                # e. day (1,29) for month (2) AND leap years (no day 30 for all years)
                if day > 29 and month == 2:
                    print("That's not a valid date!")
                else:
                    # f. day (1,28) for month (2) AND non leap years
                    if (day > 28 and month == 2 and year % 4 != 0 or day > 28
                        and month == 2 and year % 100 == 0 and year % 400 != 0):
                        print("That's not a valid date!")
                    else:
                        # 2. the date is before the beginning of the semester
                        # the date is valid AND smaller than 20200127
                        if date < 20200127:
                            print("This date is before the semester begins!")
                        # 3. the date is after the end of the semester
                        # the date is valid AND larger than 20200511
                        elif date > 20200511:
                            print("This date is after the semester ends!")
                        else:
                            # 4. the date is during the semester AND one of the days we have classes
                            # date: 0127, 0129, 0203, 0205, 0210, 0212, 0219, 0224, 0226, 0302, 0304, 0309
                            # date: 0311, 0323, 0325, 0330, 0401, 0406, 0408, 0413, 0415, 0420, 0422, 0427
                            # date: 0429, 0504, 0506, 0511
                            month = str(month)
                            day = str(day)
                            if (month+day == '127' or month+day == '129' or month+day == '203' or month+day == '205' or
                                month+day == '210' or month+day == '212' or month+day == '219' or month+day == '224' or
                                month+day == '226' or month+day == '302' or month+day == '304' or month+day == '309' or
                                month+day == '311' or month+day == '323' or month+day == '325' or month+day == '330' or
                                month+day == '401' or month+day == '406' or month+day == '408' or month+day == '413' or
                                month+day == '415' or month+day == '420' or month+day == '422' or month+day == '427' or
                                month+day == '429' or month+day == '504' or month+day == '506' or month+day == '511'):
                                print('You have class today!')
                            # 5. the date is during the semester but is not among the days we have classes
                            else:
                                print("You don't have class today!")
