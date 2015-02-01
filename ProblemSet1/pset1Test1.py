def countVowels(s):
    '''
    Assume s is a string of lower case characters.

    Write a program that counts up the number of vowels contained in the string s. 
    Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
    For example, if s = 'azcbobobegghakl', your program should print:

    Number of vowels: 5
    '''
    
    count = 0
    
    for char in s:
        if char in ('a','e','i','o','u'):
            count += 1
    return count
    
s = 'azcbobobegghakl'
z = countVowels(s)
print 'z is ' + str(z)

    
    