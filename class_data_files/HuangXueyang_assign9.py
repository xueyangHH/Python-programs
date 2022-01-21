# Name: Xueyang Huang
# Date: April 27th
# Class section: 02
# Name of program: HuangXueyang_assign9.py

filename = input('which file do you want to work with? ')

try:
    file_pointer = open(filename+'.txt', 'r')
except:
    print('File did not open!')
else:
    print('Successfully opened', filename+'.txt')
    alldata = file_pointer.read()
    file_pointer.close()
    good = 0
    bad = 0
    tests = alldata.split('\n')
    all_scores = []
    students = []
    for item in tests:
        answers_list = item.split(',')
        student = answers_list[0]
        answers = answers_list[1:]
        if len(answers) == 25:
            if student[0] == 'N':
                good += 1
                students.append(student)
                answerkey = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
                score = 0
                answerkey_list = answerkey.split(',')
                for i in range(len(answers)):
                    if answers[i] == answerkey_list[i]:
                        score += 4
                    elif answers[i] == '':
                        score += 0
                    else:
                        score -= 1
                all_scores.append(score)
            else:
                bad += 1
        else:
            bad += 1
    mean = sum(all_scores)/len(all_scores)
    all_scores_c = all_scores.copy()
    all_scores_c.sort()
    if len(all_scores_c) % 2 == 0:
        median = (all_scores_c[len(all_scores_c)//2-1] + all_scores_c[len(all_scores_c)//2])/2
    else:
        median = all_scores_c[(len(all_scores_c)-1)//2]
    unique_score = []
    times = []
    for score in all_scores:
        if score not in unique_score:
            unique_score.append(score)
            times.append(1)
        else:
            times[unique_score.index(score)] += 1
    max_pos = []
    for i in range(len(times)):
        if times[i] == max(times):
            max_pos.append(i)
    modes = []
    for i in max_pos:
        modes.append(unique_score[i])
    mode = ''
    for i in modes:
        mode += str(i) + ' '
    print('\nGrade Summary:')
    print('Total students:', good)
    print('Unusable lines in the file:', bad)
    print('Highest score:', max(all_scores))
    print('Lowest score:', min(all_scores))
    print('Mean score:', format(mean, '.2f'))
    print('Median score:', int(median))
    print('Mode:', mode)
    print('Range:', max(all_scores) - min(all_scores))
    while True:
        curve_ornot = input("Would you like to curve the exam? 'y' or 'n': ")
        if curve_ornot == 'y':
            while True:
                curved_mean_str = input('Enter a desired mean (i.e. 75.0 to 76.0): ')
                try:
                    curved_mean = float(curved_mean_str)
                except:
                    print('Invalid curve, try again.\n')
                else:
                    if curved_mean <= 0:
                        print('Invalid curve, try again.\n')
                    else:
                        break
            break
        elif curve_ornot == 'n':
            break
        else:
            print('Invalid command\n')
    file_object = open(filename+'_grades.txt', 'w')
    for i in range(len(students)):
        if curve_ornot == 'y':
            file_object.write(students[i]+','+str(all_scores[i])+','+format(all_scores[i]+(curved_mean - mean),'.2f'))
        else:
            file_object.write(students[i]+','+str(all_scores[i]))
        file_object.write('\n')
    file_object.close()
    print('Done! Check your grade file!')
    
