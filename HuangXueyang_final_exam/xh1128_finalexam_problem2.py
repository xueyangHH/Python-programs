# function:   dictionary_to_lists
# input:      a dictionary
# processing: converts the dictionary into a pair of two lists.  the first list
#             that gets generated will contain the keys of the original
#             dictionary, and the second list will contain the values of the
#             dictionary.  the lists should be parallel (i.e. the element at 
#             position 0 in the first list should match the element at position 0 
#             in the second list). if the dictionary is empty the program should 
#             simply return two empty lists
# output:     two lists

def dictionary_to_list(dic):
    keys = []
    values = []
    for key, value in dic.items():
        keys.append(key)
        values.append(value)
    return keys,values



# function:   biggest_and_smallest_words
# input:      a phrase (string) and a delimiter character (string)
# processing: isolates individual words from the supplied string using the 
#             delimiter character as a guide. the function then identifies
#             the biggest (longest) and smallest strings in the supplied phrase.
#             if there are two or more strings that qualify (i.e. "aaa" and "bbb"
#             are of the same length) you can pick just one to return.
# output:     two strings

def biggest_and_smallest_words(phrase, string):
    phrase = phrase.split(string)
    biggest = ''
    smallest = ''
    max_len = 0
    min_len = 1000000
    for i in phrase:
        if len(i) >= max_len:
            max_len = len(i)
            biggest = i
        if len(i) <= min_len:
            min_len = len(i)
            smallest = i
    return biggest, smallest



# function:   flatten_list
# input:      a list
# processing: analyzes the given list and "flattens" any nested lists that may
#             be present.  for example, the list [ 1, [2,3], 4 ] has 3 elements
#             (an integer, a list, and an integer) -- this function would 
#             "flatten" it to become [ 1, 2, 3, 4] 
#             note that for this function you cannot be guaranteed that a list
#             will actually need "flattening" (i.e. [1,2,3] is already flattened)
#             you are, however, guaranteed that any lists that do need to be
#             flattened will only contain one dimensional lists (i.e. you will 
#             never have to deal with this situation: [ 1, [2, [3,4] ] ] )
#             your function should also count how many "flattens" it needed to make
#             in order to fully process the list.
#             
#             * YOU MAY NOT USE ANY TECHNIQUE WE HAVE NOT COVERED IN CLASS TO DO THIS *
#             (hint: if you keep getting runtime errors when trying to solve this 
#             problem what does that mean? can you use this to your advantage?)
#             
# output:     a list containing the flattened version of the original list, and
#             the number of "flattened" lists contained in the new list

def flatten_list(list1):
    num = 0
    new_list = []
    for i in list1:
        if str(i).isdigit() == True:
            new_list.append(i)
        else:
            num += 1
            for n in i:
                new_list.append(n)
    return new_list, num

    
