# Name: Xueyang Huang
# Date: April 21st
# Class section: 02
# Name of program: HuangXueyang_assign8_part3.py

# product lists
product_names = ["soft drink", "onion rings", "small fries"]
product_costs = [0.99, 1.29, 1.49]
product_inventory = [10, 5, 20]

while True:

    option = input('(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ').lower()
    if option == 'q':
        print('See you soon!')
        break
    elif option == 'u':
        while True:
            mod_product = input('Enter a product name: ').lower()
            if mod_product in product_names:
                mod_pos = product_names.index(mod_product)
                print('What would you like to update?')
                choice = input('(n)ame, (c)ost or (q)uantity: ').lower()
                if choice == 'n':
                    while True:
                        mod_name = input('Enter a new name: ').lower()
                        if mod_name in product_names:
                            print('Duplicate name!')
                        else:
                            for i in range(len(product_names)):
                                if product_names[i] == mod_product:
                                    product_names[i] = mod_name
                                else:
                                    continue
                            break
                    print('Product name has been updated\n')
                    break
                elif choice == 'c':
                    while True:
                        mod_cost_str = input('Enter a new cost: ')
                        try:
                            mod_cost = float(mod_cost_str)
                        except:
                            print('Invalid cost!')
                        else:
                            if float(mod_cost) <= 0:
                                print('Invalid cost!')
                            else:
                                for i in range(len(product_costs)):
                                    if i == mod_pos:
                                        product_costs[i] = float(mod_cost)
                                    else:
                                        continue
                                break
                    print('Product cost has been updated\n')
                    break
                elif choice == 'q':
                    while True:
                        mod_quant = input('Enter a new quantity: ')
                        if mod_quant.isdigit() == True:
                            if int(mod_quant) == 0:
                                print('Invalid quantity!')
                            else:
                                for i in range(len(product_inventory)):
                                    if i == mod_pos:
                                        product_inventory[i] = int(mod_quant)
                                    else:
                                        continue
                                break
                        else:
                            print('Invalid quantity!')
                    print('Product quantity has been updated\n')
                    break
                else:
                    print('Invalid option')
                    break
            else:
                print("Product doesn't exist. Can't update.\n")
                break
    elif option == 'a':
        while True:
            new_name = input('Enter a new product name: ').lower()
            if new_name in product_names:
                print('Sorry, we already sell that product. Try again.')
            else:
                while True:
                    new_cost_str = input('Enter a product cost: ')
                    try:
                        new_cost = float(new_cost_str)
                    except:
                        print('Invalid cost. Try again.')
                        continue
                    else:
                        if float(new_cost) <= 0:
                            print('Invalid cost. Try again.')
                        else:
                            break
                while True:
                    new_quant = input('How many of these products do we have? ')
                    if new_quant.isdigit() == True:
                        if int(new_quant) == 0:
                            print('Invalid quantity. Try again.')
                        else:
                            break
                    else:
                        print('Invalid quantity. Try again.')
                break
        print('Product added!\n')
        product_names.append(new_name)
        product_costs.append(float(new_cost))
        product_inventory.append(int(new_quant))
    elif option == 'r':
        if len(product_names) > 0:
            rem_name = input('Enter a product name: ').lower()
            if rem_name in product_names:
                rem_pos = product_names.index(rem_name)
                new_product_names = []
                new_costs = []
                new_inventory = []
                for i in product_names:
                    if i == rem_name:
                        continue
                    else:
                        new_product_names.append(i)
                product_names = new_product_names
                for i in range(len(product_costs)):
                    if i == rem_pos:
                        continue
                    else:
                        new_costs.append(product_costs[i])
                product_costs = new_costs
                for i in range(len(product_inventory)):
                    if i == rem_pos:
                        continue
                    else:
                        new_inventory.append(product_inventory[i])
                product_inventory = new_inventory
                print('Product removed!\n')
            else:
                print("Product doesn't exist. Can't remove\n")
        else:
            print("There is no product in store!\n")
    elif option == 's':
        name = input('Enter a product name: ').lower()
        if name in product_names:
            position = product_names.index(name)
            print('We sell '+ '"' + name + '"' + ' at '+ str(product_costs[position]) + ' per unit')
            print('We currently have', product_inventory[position], 'in stock\n')
        else:
            print("Sorry, we don't sell " + '"' + name + '"' + '\n')
    elif option == 'l':
        if len(product_names) != 0:
            print(format('Product', '24s'), format('Price', '>5s'), 'Quantity')
            for n in range(len(product_names)):
                print(format(product_names[n], '24s'), format(product_costs[n], '>5.2f'), format(product_inventory[n], '>8d'))
            print()
        else:
            print('No products in store!\n')
    elif option == 'e':
        if len(product_names) != 0:
            max_pos = product_costs.index(max(product_costs))
            min_pos = product_costs.index(min(product_costs))
            total = 0
            for i in range(len(product_costs)):
                total += product_costs[i] * product_inventory[i]
            print(format('Most expensive product:', '29s')+str(max(product_costs))+' ('+product_names[max_pos]+')')
            print(format('Least expensive product:', '29s')+str(min(product_costs))+' ('+product_names[min_pos]+')')
            print(format('Total value of all products:', '28s'), format(total, '.2f'), '\n')
        else:
            print('No products in store!\n')
    else:
        print('Invalid option, try again\n')
