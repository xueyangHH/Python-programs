# Name: Xueyang Huang
# Date: May 6th
# Class section: 02
# Name of program: HuangXueyang_assign10_extra_credit.py

import random

try:
    fp = open('python_asg10_Roget_Thesaurus.txt', 'r')
except:
    print('Cannot open the file')
else:
    data = fp.read()
    fp.close()
    thesaurus = {}
    data_list = data.split('\n')
    num = len(data_list)
    print('Total words in thesaurus', num)
    for items in data_list:
        items = items.split(',')
        thesaurus[items[0]] = []
        for w in items[1:]:
            thesaurus[items[0]] += [w]
    try:
        fp = open('bieber_baby.txt', 'r')
    except:
        print('Cannot open the file')
    else:
        while True:
            try:
                chance = float(input('\nEnter a % chance to change a word: '))
            except:
                print('Invalid chance value')
            else:
                if 0 <= chance <= 1:
                    break
                else:
                    print('Invalid chance value')
        lyrics = fp.read().lower()
        lyrics = lyrics.split('\n')
        clean_lyrics = []
        for lines in lyrics:
            lines = lines.split(' ')
            clean_lines = []
            for w in lines:
                clean_words = ''
                for c in w:
                    if c.isalpha() == True:
                        clean_words += c
                    elif c.isdigit() == True:
                        clean_words += ' '
                    else:
                        clean_words += ''
                clean_lines.append(clean_words)
            clean_lyrics.append(clean_lines)
        lyrics = clean_lyrics
        for lines in lyrics:
            if lines != ['']:
                for i in range(len(lines)):
                    if lines[i] in thesaurus:
                        sample = random.random()
                        if sample <= chance:
                            pos = random.randint(0, len(thesaurus[lines[i]])-1)
                            lines[i] = thesaurus[lines[i]][pos].upper()
                        else:
                            continue
                    else:
                        continue
            else:
                continue
        print()
        for lines in lyrics:
            lyrics_str = ''
            for word in lines:
                if word != '':
                    lyrics_str += word+' '
                else:
                    break
            print(lyrics_str)
