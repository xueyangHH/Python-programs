# Name: Xueyang Huang
# Date: May 5th
# Class section: 02
# Name of program: HuangXueyang_assign10_part3.py

def sentiment_init():
    try:
        # open up the movie review file
        fp = open("movie_reviews.txt", "r")
    except:
        return -1
    else:
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
        return sentiment

def compute_sentiment(sentiment, phrase):
    if sentiment == -1:
        return 'Invalid sentiment'
    else:
        phrase = phrase.lower()
        clean_phrase = ''
        for c in phrase:
            if c.isalpha():
                clean_phrase += c
            else:
                clean_phrase += ' '
        phrase = clean_phrase
        phrase = phrase.split(' ')
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
                sum_phrase += average_word
            else:
                invalid_word += 1
        if invalid_word < len(phrase):
            average_phrase = sum_phrase/(len(phrase) - invalid_word)
            return average_phrase
        else:
            return 2.0
