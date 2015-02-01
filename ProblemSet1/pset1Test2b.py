def countBob(s):
    '''
    Assume s is a string of lower case characters.
    Write a program that prints the number of times the string 'bob' occurs in s. 
    For example, if s = 'azcbobobegghakl', then your program should print
    
    Number of times bob occurs is: 2
    '''
    
    ref = 'bob'
    l = len(s)
    count = 0
    num = 0
    ret = 0
    
 #   while (ret = s.find('bob',num)!= -1):
    while True:
        print 'num is ' + str(num)
        ret = s.find('bob',num)
        print 'ret is ' + str(ret)
        if ret == -1:
            break
        count += 1
        num = ret + 1
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