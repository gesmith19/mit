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
    print "x is ", x + "word is ", word
    if len(x) > len(word):
        return False
    elif x == "":
        return True
    else:
        i = 0
        for c in word:
            if x[0] == word[i]:
                return x_ian(x[1:], word[i+1:])
            else:
                i += 1
        return False
        