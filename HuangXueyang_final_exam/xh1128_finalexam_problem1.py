coin_data = "5D,4Q,3N,100Z,DUD,17P,1H"
valid_coin_codes = "PNDQH"
valid_coin_values = [0.01, 0.05, 0.1, 0.25, 0.5]

coin_data = coin_data.split(',')
valid_coins = []
coin_values = []
for item in coin_data:
    if item[0:-1].isdigit() == True:
        if item[-1] in valid_coin_codes:
            valid_coins += [item]
            coin_value = valid_coin_values[valid_coin_codes.index(item[-1])]*int(item[0:-1])
            coin_values.append(coin_value)
        else:
            continue
    else:
        continue

for item in coin_data:
    if item in valid_coins:
        print(item[0:-1]+' '+item[-1]+' =', format(coin_values[valid_coins.index(item)], '.2f'))
    else:
        print(item[0:-1]+' '+item[-1]+' is invalid, rejecting')
total = sum(coin_values)
print ("You currently have:", format(total, '.2f'), "in your pocket")

