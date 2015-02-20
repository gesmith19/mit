def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
#    print "x is ", x + " word is ", word
    if len(x) > len(word):
        return False
    elif x == "":
        return True
    else:
        i = word.find(x[0])
        if i == -1:             # not found in word
            return False
        else:
            return x_ian(x[1:], word[i+1:])
