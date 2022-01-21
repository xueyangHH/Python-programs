try:
    fp = open('class_data.txt', 'r')
except:
    print('Cannot open!')
else:
    data = fp.read()
    fp.close()
    data_list = data.split('\n')
    classes = {}
    for item in data_list:
        class_info = item.split(',')
        classes[class_info[0]] = class_info[1]
    try:
        fp = open('enrollment_data.txt', 'r')
    except:
        print('Cannot open!')
    else:
        enroll_data = fp.read()
        fp.close()
        enroll_list = enroll_data.split('\n')
        enrollment = {}
        for item in enroll_list:
            enroll_info = item.split(',')
            if enroll_info[0] in classes:
                if enroll_info[0] not in enrollment:
                    enrollment[enroll_info[0]] = [enroll_info[1]+','+enroll_info[2]]
                else:
                    enrollment[enroll_info[0]] += [enroll_info[1]+','+enroll_info[2]]
    print('NYU Computer Science Registration System')
    class_id = input('Enter a course ID (i.e. CS0002, CS0004): ')
    if class_id in classes:
        print('The title of this class is:', classes[class_id])
        if class_id in enrollment:
            print('The course has', len(enrollment[class_id]), 'students enrolled')
            for stu in enrollment[class_id]:
                print('*', stu)
        else:
            print('The course has 0 students enrolled')
    else:
        print('Cannot find this course')
    
