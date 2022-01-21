# Name: Xueyang Huang
# Date: April 24th
# Class section: 02
# Name of program: HuangXueyang_assign8_part5.py

import random

cards  = ['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts', '5 of Hearts', '4 of Hearts', '3 of Hearts', '2 of Hearts', 'Ace of Hearts', 'King of Hearts', 'Queen of Hearts', 'Jack of Hearts', '10 of Diamonds', '9 of Diamonds', '8 of Diamonds', '7 of Diamonds', '6 of Diamonds', '5 of Diamonds', '4 of Diamonds', '3 of Diamonds', '2 of Diamonds', 'Ace of Diamonds', 'King of Diamonds', 'Queen of Diamonds', 'Jack of Diamonds', '10 of Clubs', '9 of Clubs', '8 of Clubs', '7 of Clubs', '6 of Clubs', '5 of Clubs', '4 of Clubs', '3 of Clubs', '2 of Clubs', 'Ace of Clubs', 'King of Clubs', 'Queen of Clubs', 'Jack of Clubs', '10 of Spades', '9 of Spades', '8 of Spades', '7 of Spades', '6 of Spades', '5 of Spades', '4 of Spades', '3 of Spades', '2 of Spades', 'Ace of Spades', 'King of Spades', 'Queen of Spades', 'Jack of Spades']

values = [10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10]

ace_value = [1,11]
ace_names = []
for v in range(len(values)):
    if values[v] == ace_value:
        ace_names.append(cards[v])
    else:
        continue

# ask the user for an amount for they bank of money
print('To play this game, you need to enter an amount of money as your initial deposit')
print('And then enter an amount of money at each round as your bet')
print('Each hand you choose to play will cost you the bet from your deposit')
print('So please make sure you enter a number larger than $0')
while True:
    bank_str = input('Enter an amount of money ($): ')
    try:
        bank = float(bank_str)
    except:
        print('Not a valid input, try again')
    else:
        if bank <= 0:
            print('Please enter a number larger than 0')
            continue
        else:
            break
            
while bank > 0:
    
    while True:
        bet_str = input('\nEnter your bet ($): ')
        try:
            bet = float(bet_str)
        except:
            print('Not a valid input, try again')
        else:
            if bet <= 0:
                print('Please enter a number larger than 0')
            elif bet > bank:
                print('Bet is larger than the deposit!')
            else:
                break
            
    blackjack = False
    bust = False
    c_blackjack = False
    c_bust = False
    c_exceed = False
    user_cards = []
    com_cards = []
    rest_cards = cards
    rest_values = values
    sum_cards = 0
    csum_cards = 0
    ace_find = False
    cace_find = False

    # taking two random cards from the deck to the user
    # the random pos in rest of cards cannot align with the pos in cards
    bank -= bet
    print('\nCurrent deposit: $', bank)
    while len(user_cards) < 2:
        cardpos = random.randint(0,len(rest_cards)-1)
        for i in range(len(rest_cards)):
            if i == cardpos:
                user_cards.append(rest_cards[i])
                if sum_cards == 0: # picking the first card
                    if rest_cards[i] in ace_names: 
                        sum_cards += 1
                        sum_cards1 = 1
                        sum_cards2 = 11
                    else:
                        sum_cards += rest_values[i]
                elif sum_cards == 1: # if the first one is Ace
                    ace_find = True
                    if rest_cards[i] in ace_names: # if the second is Ace
                        sum_cards1 += 1
                        sum_cards2 += 1
                    else: # if the second is not Ace
                        sum_cards1 = 1 + rest_values[i]
                        sum_cards2 = 11 + rest_values[i]
                        if sum_cards2 == 21:
                            blackjack = True
                        elif sum_cards2 > 21:
                            ace_find = False
                            sum_cards = sum_cards1
                        else:
                            continue
                else: # the first is not Ace
                    if rest_cards[i] in ace_names:  # if the second one is Ace
                        ace_find = True
                        sum_cards1 = sum_cards + 1
                        sum_cards2 = sum_cards + 11
                        if sum_cards2 == 21:
                            blackjack = True
                        elif sum_cards2 > 21:
                            ace_find = False
                            sum_cards = sum_cards1
                        else:
                            continue
                    else: # if the second one is not Ace
                        sum_cards += rest_values[i]
            else:
                continue
        rest_cards = []
        rest_values = []
        for c in range(len(cards)):
            if cards[c] not in user_cards:
                rest_cards.append(cards[c])
                rest_values.append(values[c])
                
    # report the individual and sum value of the two cards
    if ace_find == True:
        print('Player hand:', user_cards, 'is worth', sum_cards1, 'or', sum_cards2)
        if blackjack == True:
            bank += bet * 2
            print('You got Blackjack! You win!')
    else:
        print('Player hand:', user_cards, 'is worth', sum_cards)

    # let the user choose to hit or stand, do a validation
    while blackjack == False and bust == False:
        choice = input('(h)it or (s)tand? ').lower()
        # if the user choose to hit, choose another random card and report the sum
        # if there was an Ace before or in this round the user gets an Ace, determine
        # the sum value, if ace = 11 will go bust then automatically adjust the ace value
        # to 1, otherwise keep going
        # until the user gets 21 points and WINS, or get bust and LOSE automatically
        if choice == 'h':
            cardpos = random.randint(0,len(rest_cards)-1)
            print('You drew', rest_cards[cardpos])
            for i in range(len(rest_cards)):
                if i == cardpos:
                    user_cards.append(rest_cards[i])
                    if ace_find == True:
                        if rest_cards[i] in ace_names:
                            sum_cards1 += 1
                            sum_cards2 += 1
                            if sum_cards2 == 21:
                                blackjack = True
                                break
                        else:
                            sum_cards1 += rest_values[i]
                            sum_cards2 += rest_values[i]
                            if sum_cards2 == 21:
                                blackjack = True
                                break
                            elif sum_cards2 > 21:
                                ace_find = False
                                sum_cards = sum_cards1
                            elif sum_cards2 < 21:
                                continue
                    else:
                        if rest_cards[i] in ace_names:
                            ace_find = True
                            sum_cards1 = sum_cards + 1
                            sum_cards2 = sum_cards + 11
                            if sum_cards1 == 21 or sum_cards2 == 21:
                                blackjack = True
                                break
                            elif sum_cards2 > 21:
                                ace_find = False
                                sum_cards = sum_cards1
                            elif sum_cards2 < 21:
                                continue
                        else:
                            sum_cards += rest_values[i]
                            if sum_cards == 21:
                                blackjack = True
                                break
                            elif sum_cards > 21:
                                bust = True
                                break
                else:
                    continue
            rest_cards = []
            rest_values = []
            for c in range(len(cards)):
                if cards[c] not in user_cards:
                    rest_cards.append(cards[c])
                    rest_values.append(values[c])  
            if ace_find == True:
                print('Player hand:', user_cards, 'is worth', sum_cards1, 'or', sum_cards2)
                if blackjack == True:
                    bank += bet * 2
                    print('You got Blackjack! You win!')
            else:
                print('Player hand:', user_cards, 'is worth', sum_cards)
                if blackjack == True:
                    bank += bet * 2
                    print('You got Blackjack! You win!')
                elif bust == True:
                    print('Bust!\nComputer wins!')
        elif choice == 's':
            print()
            break
        else:
            print('Invalid command, try again')

    # if the user choose to stand, then the computer first randomly picks two
    # cards, and then keep hitting until
    # a. the computer gets 21 points and WINS
    # b. computer's points over user's points and WINS
    # c. computer gets bust and USER WINS
    if blackjack == False and bust == False and choice == 's':
        while len(com_cards) < 2:
            cardpos = random.randint(0,len(rest_cards)-1)
            for i in range(len(rest_cards)):
                if i == cardpos:
                    com_cards.append(rest_cards[i])
                    if csum_cards == 0: # picking the first card
                        if rest_cards[i] in ace_names: 
                            csum_cards += 1
                            csum_cards1 = 1
                            csum_cards2 = 11
                        else:
                            csum_cards += rest_values[i]
                    elif csum_cards == 1: # if the first one is Ace
                        cace_find = True
                        if rest_cards[i] in ace_names: # if the second is Ace
                            csum_cards1 += 1
                            csum_cards2 += 1
                        else: # if the second is not Ace
                            csum_cards1 = 1 + rest_values[i]
                            csum_cards2 = 11 + rest_values[i]
                            if csum_cards2 == 21:
                                c_blackjack = True
                            elif csum_cards2 > 21:
                                cace_find = False
                                csum_cards = csum_cards1
                            else:
                                continue
                    else: # the first is not Ace
                        if rest_cards[i] in ace_names:  # if the second one is Ace
                            cace_find = True
                            csum_cards1 = csum_cards + 1
                            csum_cards2 = csum_cards + 11
                            if csum_cards2 == 21:
                                c_blackjack = True
                            elif csum_cards2 > 21:
                                cace_find = False
                                csum_cards = csum_cards1
                            else:
                                continue
                        else: # if the second one is not Ace
                            csum_cards += rest_values[i]
                else:
                    continue
            rest_cards = []
            rest_values = []
            for c in range(len(cards)):
                if cards[c] not in user_cards:
                    rest_cards.append(cards[c])
                    rest_values.append(values[c])
                    
        if cace_find == True and ace_find == True:
            if csum_cards2 > sum_cards2:
                c_exceed = True
        elif cace_find == False and ace_find == True:
            if csum_cards > sum_cards2:
                c_exceed = True
        elif cace_find == True and ace_find == False:
            if csum_cards2 > sum_cards:
                c_exceed = True
        elif cace_find == False and ace_find == False:
            if csum_cards > sum_cards:
                c_exceed = True
        if cace_find == True:
            print('Computer hand:', com_cards, 'is worth', csum_cards1, 'or', csum_cards2)
            if c_blackjack == True:
                print('Computer got 21! Blackjack!\nComputer wins!')
            elif c_exceed == True:
                print('Computer wins!')
        else:
            print('Computer hand:', com_cards, 'is worth', csum_cards)
            if c_exceed == True:
                print('Computer wins!')
            
        while c_blackjack == False and c_bust == False and c_exceed == False:
            cardpos = random.randint(0,len(rest_cards)-1)
            print('Computer drew', rest_cards[cardpos])
            for i in range(len(rest_cards)):
                if i == cardpos:
                    com_cards.append(rest_cards[cardpos])
                    if cace_find == True:
                        if rest_cards[i] in ace_names:
                            csum_cards1 += 1
                            csum_cards2 += 1
                            if csum_cards2 == 21:
                                c_blackjack = True
                                break
                        else:
                            csum_cards1 += rest_values[i]
                            csum_cards2 += rest_values[i]
                            if csum_cards2 == 21:
                                c_blackjack = True
                                break
                            elif csum_cards2 > 21:
                                cace_find = False
                                csum_cards = csum_cards1
                            elif csum_cards2 < 21:
                                continue
                    else:
                        if rest_cards[i] in ace_names:
                            cace_find = True
                            csum_cards1 = csum_cards + 1
                            csum_cards2 = csum_cards + 11
                            if csum_cards1 == 21 or csum_cards2 == 21:
                                c_blackjack = True
                                break
                            elif csum_cards2 > 21:
                                cace_find = False
                                csum_cards = csum_cards1
                            elif csum_cards2 < 21:
                                continue
                        else:
                            csum_cards += rest_values[i]
                            if csum_cards == 21:
                                c_blackjack = True
                                break
                            elif csum_cards > 21:
                                c_bust = True
                                break
                else:
                    continue
            rest_cards = []
            rest_values = []
            for c in range(len(cards)):
                if cards[c] not in user_cards:
                    rest_cards.append(cards[c])
                    rest_values.append(values[c]) 
            if cace_find == True and ace_find == True:
                if csum_cards2 > sum_cards2:
                    c_exceed = True
            elif cace_find == False and ace_find == True:
                if csum_cards > sum_cards2:
                    c_exceed = True
            elif cace_find == True and ace_find == False:
                if csum_cards2 > sum_cards:
                    c_exceed = True
            elif cace_find == False and ace_find == False:
                if csum_cards > sum_cards:
                    c_exceed = True
            if cace_find == True:
                print('Computer hand:', com_cards, 'is worth', csum_cards1, 'or', csum_cards2)
                if c_blackjack == True:
                    print('Computer got 21! Blackjack!\nComputer wins!')
                elif c_exceed == True:
                    print('Computer wins!')
            else:
                print('Computer hand:', com_cards, 'is worth', csum_cards)
                if c_blackjack == True:
                    print('Computer got 21! Blackjack!\nComputer wins!')
                elif c_bust == True:
                    bank += bet * 2
                    print('Bust!\nPlayer wins!')
                elif c_exceed == True:
                    print('Computer wins!')
    print('Current deposit: $', bank)
    if bank > 0:
        print('\nStarting a new game...')

print('\nRan out of money! Game over.')


