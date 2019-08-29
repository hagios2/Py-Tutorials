def break_words(stuff):
    """This function will break up words for us"""
    #get the argv and split it into a list when ' ' is encountered 
    words = stuff.split(' ')

    #return the words
    return words


def sort_words(words):
    """Sorts the words"""

    #built in function for sorting a list 
    return sorted(words)


def print_first_word(kwords):
    """Prints the first after popping it off."""

    #take off the first word on the stack
    word = kwords.pop(0)
   
   #print it here
    print(word)


def print_last_word(words):
    """Prints the last word after popping it off."""

    #take off the last word on/under the stack or reverse the stack and print the first
    word = words.pop(-1)

    #print it here
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    
    #call break words function to split the words in to a list
    words = break_words(sentence)

    #get the sort words function to sort the words in the list
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""

    #split the sentence into a list
    words = break_words(sentence)
    
    #call the first word on the stack for the list
    print_first_word(words)

    #call the last word on the stack for the list
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""

    #break sentence into a list and return sorted list
    words = sort_sentence(sentence)

    #print the first on the stack
    print_first_word(words)

    #print the last on the stack
    print_last_word(words)