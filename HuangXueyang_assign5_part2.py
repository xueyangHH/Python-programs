# Name: Xueyang Huang
# Date: March 12th
# Class section: 02
# Name of program: HuangXueyang_assign5_part2.py

# set up a while loop to validate data (number of students and tests)
while True:
    students = int(input('How many students are in your class? '))
    if students <= 0:
        print('Invalid # of students, try again.\n')
    else:
        while True:
            tests = int(input('How many tests in this class? '))
            if tests <= 0:
                print('Invalid # of tests, try again.')
            else:
                print('\nHere we go!')
                break
        break

# make an accumulator to keep track of scores of the whole class
class_score = 0

# set up a for loop to keep track of scores of each student's tests    
for s in range(students):
    print('\n**** Student #' + str(s + 1) + '****')
    # accumulator to store the total score of a single student
    total_score = 0
    t = 1
    # data validation in a while loop
    while t <= tests:
        score = int(input('Enter score for test #'+ str(t) + ': '))
        if score < 0:
            print('Invalid score, try again.')
        else:
            t += 1
            total_score += score
            continue
    print('Average score for student #', s + 1, 'is', format(total_score / tests, '.2f'))
    class_score += total_score

# print out the results
print('\nAverage score for all students is:', format(class_score / (students * tests), '.2f'))
        
    
