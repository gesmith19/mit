def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    
    if len(text) < lineLength:
        return text
    else:
        i = text[lineLength -1:].find(' ')
        if i == -1:
            return text
        else:
            return text[:lineLength+ i] + "\n" + insertNewlines(text[lineLength +i:], lineLength)


s = 'abcdef hijklmnop rs tuv wxyz'
print s
s2 = insertNewlines(s, 5)
print s2
print ' '
s1 = 'abcde fhgijklmnop rst uvw xyz'
print s1
s3 = insertNewlines(s1, 5)
print s3

        