while True:
    integer = input('Please give me an integer (negative integer to quit): ')
    if int(integer) < 0:
        print('Thanks for playing')
        break
    else:
        if len(integer) > 1:
            copy1 = integer
            copy2 = integer
            print('\nAdditive loop')
            sum_i = 0
            add_persist = 0
            while len(copy1) != 1:
                sum_i = 0
                for i in range(len(copy1)):
                    sum_i += int(copy1[i])
                copy1 = str(sum_i)
                add_persist += 1
                print('sum:', sum_i)
            add_root = sum_i
            print('\nMultiplicative loop')
            product_i = 1
            multi_persist = 0
            while len(copy2) != 1:
                product_i = 1
                for i in range(len(copy2)):
                    product_i *= int(copy2[i])
                copy2 = str(product_i)
                multi_persist += 1
                print('product:', product_i)
            multi_root = product_i
        else:
            add_persist = 0
            multi_persist = 0
            add_root = integer
            multi_root = integer
        print('\nFor the integer:', integer)
        print('Additive persistence:', add_persist, ',', 'Additive Root:', add_root)
        print('Multiplicative Persistence:', multi_persist, ',', 'Multiplicative Root:', multi_root, '\n')
            
