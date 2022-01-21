# Name: Xueyang Huang
# Date: March 25th
# Class section: 02
# Name of program: HuangXueyang_assign6_part1_challenge3.py

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
                if day > 28 and month == 2:
                    return False
                else:
                    return True
