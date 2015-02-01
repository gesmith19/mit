'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
'''
# s = 'cyqfjhcclkbxpbojgkar'

# s = 'azcbobobegghakl'

s = 'abccbcde'
result =''
current =''

for char in s:
    print ('current is '+ current + ' result is ' + result)
    if (current == ''):
        current = char
    elif (current[-1] <= char):
        current += char
    elif (current[-1] > char):
        if (len(result) < len(current)):
            result = current
            current = char
        else:
            current = char
    if (len(current) > len(result)):
        result = current

print 'current is ', current        
print 'Longest substring in alphabetical order is: ', result 