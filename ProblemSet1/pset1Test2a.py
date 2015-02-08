
def countBob(s):
    '''
    Assume s is a string of lower case characters.
    
    Write a program that prints the number of times the string 'bob' occurs in 
    s. 
    
    For example, if s = 'azcbobobegghakl', then your program should print
    Number of times bob occurs is: 2
    '''
    ref = 'bob'
    l = len(s)
    count = 0
    num = 0
    
    print 's is ', s
    for char in s:
        print 'num is ' + str(num) +  ' char is ', char
        if char == 'b':
            if num+2 < l:
                if s[num: num+3] == 'bob':
                    count += 1
        num += 1
    return count

s = 'ebobo'
z = countBob(s)
print 'z is ' + str(z)
s = 'azcbobobegghakl'
z = countBob(s)
print 'z is ' + str(z)
s = 'bobbobobegghakl'
z = countBob(s)
print 'z is ' + str(z)
s = 'bobbobobegghaklbob'
z = countBob(s)
print 'z is ' + str(z)
                    
                    
                
        
    