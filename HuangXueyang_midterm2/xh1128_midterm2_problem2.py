import random

def deal(deck):
    card1 = ''
    rest = ''
    for i in range(len(deck)):
        if i == 0:
            card1 += deck[i]
        else:
            rest += deck[i]
    return card1,rest
'''
deck = "234567890JQKA"
card1,deck = deal(deck)
print(card1,deck)
'''
def remove_card(deck, pos):
    des_card = ''
    rest = ''
    for i in range(len(deck)):
        if i == pos:
            des_card += deck[i]
        else:
            rest += deck[i]
    return des_card, rest
'''
card2,deck = remove_card(deck,5)
print(card2,deck)
'''

def cut_deck(deck):
    if len(deck) % 2 == 0:
        middle = (len(deck) // 2) + 1
        sec_half = deck[middle-1::]
        fir_half = deck[0:middle-1:]
        cut = sec_half+fir_half
    else:
        middle = (len(deck)-1)//2 + 1
        sec_half = deck[middle-1::]
        fir_half = deck[0:middle-1:]
        cut = sec_half+fir_half
    return cut

'''
deck = cut_deck(deck)
print (deck)
'''

'''
def shuffle(deck):
    new_deck = ''
    for i in range(len(deck)):
        card = random.randint(0, len(deck)-1)
        new_deck += deck[card]
        deck = remove_card(deck, card)
'''


def shuffle(deck):
    new_deck = ''
    card = random.randint(0, len(deck)-1)
    for i in range(len(deck)):
        new_deck += deck[card]
        delete, deck = remove_card(deck, card)
        if len(deck) > 1:
            card = random.randint(0, len(deck)-1)
        else:
            new_deck += deck
            break
    return new_deck

deck = '90JQKA34567'
new_deck = shuffle(deck)
print(new_deck)




