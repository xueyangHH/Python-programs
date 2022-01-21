# Name: Xueyang Huang
# Date: April 8th
# Class section: 02
# Name of program: HuangXueyang_assign7_part4.py

# function:   string_length
# input:      a word (String)
# processing: computes the length of the supplied String (without using the len() function)
# output:     returns the length of the string (integer)

def string_length(word):
    digits = 0
    for c in word:
        digits += 1
    return digits

'''
# sample code:
print ( string_length("apple") )	# 5
print ( string_length("pear")  )	# 4
print ( string_length("")      )	# 0
'''

# function:   string_isalpha
# input:      a word (String)
# processing: determines if the supplied String contains all alphabetic characters (A-Z,a-z)
#             DO NOT USE THE "isalpha()" METHOD or any other String methods!
# output:     returns True of False (boolean)

def string_isalpha(word):
    if word != '':
        for c in word:
            if 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122:
                continue
            else:
                return False
        return True
    else:
        return False

'''    
# sample code:
print ( string_isalpha("apple")     )	# True
print ( string_isalpha("pear!")     )	# False
print ( string_isalpha("123")       )	# False
print ( string_isalpha("123 AbC")   )	# False
print ( string_isalpha("abc1")      )	# False
print ( string_isalpha("")          )	# False
'''

# function:   string_isupper
# input:      a word (String)
# processing: determines if the supplied String contains all uppercase characters (A-Z)
#             DO NOT USE THE "isupper()" METHOD or any other String methods!
# output:     returns True of False (boolean)
def string_isupper(word):
    if word != '':
        for c in word:
            if 65 <= ord(c) <= 90:
                continue
            else:
                return False
        return True
    else:
        return False

'''
# sample code:
print ( string_isupper("apple")     )	# False
print ( string_isupper("PEAR")      )	# True
print ( string_isupper("123")       )	# False
print ( string_isupper("123 AbC")   )	# False
print ( string_isupper("ApPLE")     )	# False
print ( string_isupper("")          )	# False
'''

# function:   string_isdigit
# input:      a word (String)
# processing: determines if the supplied String contains all numeric characters (0-9)
#             DO NOT USE THE "isdigit()" METHOD or any other String methods!
# output:     returns True of False (boolean)
def string_isdigit(word):
    if word != '':
        for c in word:
            if 48 <= ord(c) <= 57:
                continue
            else:
                return False
        return True
    else:
        return False

'''
# sample code:    
print ( string_isdigit("apple")     )	# False
print ( string_isdigit("PEAR")      )	# False
print ( string_isdigit("123")       )	# True
print ( string_isdigit("123 AbC")   )	# False
print ( string_isdigit("ApPLE")     )	# False
print ( string_isdigit("")          )	# False
'''

# function:   string_swapcase
# input:      a word (String)
# processing: swaps uppercase characters with lowercase characters & vice-versa
#             DO NOT USE THE "swapcase()" METHOD or any other String methods!
# output:     returns a new copy of the String
def string_swapcase(word):
    newword = ''
    for c in word:
        if 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122:
            if 65 <= ord(c) <= 90:
                newword += chr(ord(c) + 32)
            elif 97 <= ord(c) <= 122:
                newword += chr(ord(c) - 32)
        else:
            newword += c
    return newword

'''
# sample code:
print ( string_swapcase("apple")     )	# APPLE
print ( string_swapcase("PEAR")      )	# pear
print ( string_swapcase("123")       )	# 123
print ( string_swapcase("123 AbC")   )	# 123 aBc
print ( string_swapcase("ApPLE")     )	# aPple
print ( string_swapcase("")          )	# (nothing prints)
'''

# function:   string_lower
# input:      a word (String)
# processing: converts all characters in a String to their lowecase equivalents
#             DO NOT USE THE "lower()" METHOD OR "str.lower()"! or any other String methods!
# output:     returns a new copy of the String
def string_lower(word):
    newword = ''
    for c in word:
        if 65 <= ord(c) <= 90:
            if 65 <= ord(c) <= 90:
                newword += chr(ord(c) + 32)
        else:
            newword += c
    return newword

'''
# sample code:
print ( string_lower("apple")     )	# apple
print ( string_lower("PEAR")      )	# pear
print ( string_lower("123")       )	# 123
print ( string_lower("123 AbC")   )	# 123 abc
print ( string_lower("ApPLE")     )	# apple
print ( string_lower("")          )	# (nothing prints)
'''
