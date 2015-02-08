def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return out + s2
        if s2 == '':
            return out + s1
        else:
            return helpLaceStrings(s1[1:], s2[1:], (out + s1[0] + s2[0]))
    return helpLaceStrings(s1, s2, '')

vshort_s1 = 'A'
short_s1 = 'ABCDEF'
equal_s1 = 'ABCDEFGHIJKL'
long_s1 = 'ABCDEFGHIJKLMNOPQRS'
short_s2 = 'abcdef'
equal_s2 = 'abcdefghijkl'
long_s2 = 'abcdefghijklmnopqrs'

x = laceStringsRecur(short_s1, long_s2)
print x
x = laceStringsRecur(vshort_s1, long_s2)
print x

x = laceStringsRecur(equal_s1, equal_s2)
print x
x = laceStringsRecur(long_s1, short_s2)
print x

x = laceStringsRecur("", short_s2)
print x