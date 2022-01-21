# Name: Xueyang Huang
# Date: May 4th
# Class section: 02
# Name of program: HuangXueyang_assign10_part1&2.py

import time

try:
    # open up the movie review file
    fp = open("movie_reviews.txt", "r")
except:
    print ("Can't open file")
else:
    start = time.time()
    data = fp.read().lower()
    fp.close()

    # isolate each review
    reviews = data.split("\n")

    # set up a dictionary to hold all of our vocab words
    sentiment = {}

    # visit every line in the file
    for line in reviews:

        score = int(line[0])
        rest = line[2:]

        # isolate each word in the review
        words = rest.split(" ")

        # clean up words
        for w in words:
            clean = ""
            for c in w:
                if c.isalpha():
                    clean += c

            # add to dictionary
            if len(clean) > 0:

                # see if this word is in our dictionary
                if clean not in sentiment:
                  sentiment[ clean ] = [ score, 1 ]
                else:
                  sentiment[ clean ][0] += score
                  sentiment[ clean ][1] += 1
    end = time.time()
    elapse = end - start
    print('Initializing sentiment database')
    print('Sentiment database initialization complete')
    print('Total unique works analyzed:', len(sentiment))
    print('Analysis took', format(elapse, '.2f'), 'seconds to complete')

    # ask the user for a word
    word = input("\nEnter a word to test: ")

    # see if we know about this word
    if word in sentiment:
        print( "'"+word+"' appears "+str(sentiment[word][1])+" times")
        print("The average score for reviews containing the word '"+word+"'"+' is '+str(sentiment[word][0]/sentiment[word][1]))
        if sentiment[word][0]/sentiment[word][1] >= 2:
            print("This is a positive word")
        else:
            print("This is a negative word")
    else:
        print("'"+word+"' appears 0 times")
        print('There is no average score for reviews containing the word '+"'"+word+"'")
        print('Cannot determine if this word is positive or negative')
        
    phrase_str = input('\nEnter a phrase to test: ').lower()
    clean_phrase = ''
    for c in phrase_str:
        if c.isalpha():
            clean_phrase += c
        else:
            clean_phrase += ' '
    phrase_str = clean_phrase
    phrase = phrase_str.split(' ')
    clean_phrase = []
    for i in range(len(phrase)):
        if phrase[i] == '':
            continue
        else:
            clean_phrase.append(phrase[i])
    phrase = clean_phrase
    sum_phrase = 0
    invalid_word = 0
    for word in phrase:
        if word in sentiment:
            average_word = sentiment[word][0]/sentiment[word][1]
            print('* '+"'"+word+"'"+' appears '+str(sentiment[word][1])+' times with an average rating of '+str(average_word))
            sum_phrase += average_word
        else:
            invalid_word += 1
            print('* '+"'"+word+"'"+' does not have a rating')
    if invalid_word < len(phrase):
        average_phrase = sum_phrase/(len(phrase) - invalid_word)
        print('Average score for this phrase is:', average_phrase)
        if average_phrase >= 2:
            print('This is a POSITIVE phrase')
        else:
            print('This is a NEGATIVE phrase')
    else:
        print('Not enough data to compute sentiment')
