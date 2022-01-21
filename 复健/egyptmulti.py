again = 'y'
while again == 'y':
    while True:
        integers = input('\nPlease input the 2 numbers separated by a space: ')
        integers_l = integers.split(' ')
        if len(integers_l) < 2 or len(integers_l) > 2:
            print('Please input only two items.')
        else:
            break
    a_str = integers_l[0]
    b_str = integers_l[1]
    a = int(a_str)
    b = int(b_str)
    product = 0
    while True:
        print('A =', a, 'and B =', b)
        if b % 2 != 0:
            product += a
            print('B was odd, we add A to make the product:', product)
        if b // 2 == 0:
            break
        elif b // 2 == -1 and b % 2 != 0:
            break
        else:
            a *= 2
            b //= 2
    if product >= 0:
        print('Product is positive')
    else:
        print('Product is negative')
    print('The product of the two numbers is:', product)
    again = input('Do you want to continue? (y/n) ').lower()
    
