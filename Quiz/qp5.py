def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    
    len1 = len(s1)
    len2 = len(s2)
    i = 0
    res = ''
    
    while i < len1 and i < len2:
        res += s1[i] + s2[i]
#        res += s2[i]
        i += 1
    
    res += s1[i:]
    res += s2[i:]
    
    return res

vshort_s1 = 'A'
short_s1 = 'ABCDEF'
equal_s1 = 'ABCDEFGHIJKL'
long_s1 = 'ABCDEFGHIJKLMNOPQRS'
short_s2 = 'abcdef'
equal_s2 = 'abcdefghijkl'
long_s2 = 'abcdefghijklmnopqrs'

x = laceStrings(short_s1, long_s2)
print x
x = laceStrings(vshort_s1, long_s2)
print x

x = laceStrings(equal_s1, equal_s2)
print x
x = laceStrings(long_s1, short_s2)
print x

x = laceStrings("", short_s2)
print x