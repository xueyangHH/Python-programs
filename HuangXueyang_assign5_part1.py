# Name: Xueyang Huang
# Date: March 12th
# Class section: 02
# Name of program: HuangXueyang_assign5_part1.py

# set up variables to store budget, cost, etc.
budget = float(input('Enter budget for your party: '))
cost_s = float(input('Cost per slice of pizza: '))
cost_p = float(input('Cost per whole pizza pie (8 slices): '))
guest = int(input('How many people will be attending your party? '))
total_s = 0

# set up a for loop to keep track of number of slices that each guest wants
for g in range(guest):
    # a while loop to validate the data
    while True:
        slices = int(input('Enter number of slices for person #' + str(g + 1) + ': '))
        if slices <= 0:
            print('Not a valid entry, try again!\n')
        else:
            total_s += slices
            break

# calculate how many pies and slices needed
total_p = total_s // 8
remain_s = total_s % 8
total_c = total_p * cost_p + remain_s * cost_s

# report the results to the user
if total_c <= budget:
    print('You should purchase', total_p, 'pies and', remain_s, 'slices')
    print('Your total cost will be:', format(total_c, '.2f'))
    # if there is still some money left
    if total_c < budget:
        print('You will still have', format(budget - total_c, '.2f'), 'after your order.')
    # if the money is just used up
    else:
        print('You will have no money left after your order.')
# exceeds the budget        
else:
    print('Your order cannot be completed.')
    print('You would need to purchase', total_p, 'pies and', remain_s, 'slices')
    print('This would put you over budget by', format(total_c - budget, '.2f'))




