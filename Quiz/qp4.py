import math

def myLog(x,b):
    '''
    Write a simple procedure, myLog(x, b), that computes the logarithm of a 
    number x relative to a base b. For example, if x = 16 and b = 2, 
    then the result is 4 - because 24=16. If x = 15 and b = 3, then the result 
    is 2 - because 32 is the largest power of 3 less than 15.
    
    In other words, myLog should return the largest power of b such that b to 
    that power is still less than or equal to x.
    
    x and b are both positive integers; b is an integer greater than or equal 
    to 2. Your function should return an integer answer.
    
    Do not use Python's log functions; instead, please use an iterative or 
    recursive solution to this problem that uses simple arithmatic operators 
    and conditional testing.
    '''
    
    if x < b:
        return 0
    else:
        return 1 + myLog(x/b, b)


def myLog1(x, b):
    
    exp = 1
    if x < b:
        return 0
#    elif x == b:
 #       return 1
    else:
        while  ((b ** exp) <= x):
            exp += 1
    return exp - 1
            
        
x = 0
b = 2
res = myLog(x, b)
print 'myLog: x is ' + str(x) + ' b is ' + str(b) + ' res is ' + str(res)
res = myLog1(x, b)
print 'myLog1: x is ' + str(x) + ' b is ' + str(b) + ' res is ' + str(res)
# res = math.log(x,b)
# print 'math.log: x is ' + str(x) + ' b is ' + str(b) + ' res is ' + str(res) 
print ' '
x = 1
b = 2
res = myLog(x, b)
print 'myLog: x is ' + str(x) + ' b is ' + str(b) + ' res is ' + str(res)
res = myLog1(x, b)
print 'myLog1: x is ' + str(x) + ' b is ' + str(b) + ' res is ' + str(res)
res = math.log(x,b)
print 'math.log: x is ' + str(x) + ' b is ' + str(b) + ' res is ' + str(res)
print ' '
x = 2
b = 2
res = myLog(x, b)
print 'myLog: x is ' + str(x) + ' b is ' + str(b) + ' res is ' + str(res)
res = myLog1(x, b)
print 'myLog1: x is ' + str(x) + ' b is ' + str(b) + ' res is ' + str(res)
res = math.log(x,b)
print 'math.log: x is ' + str(x) + ' b is ' + str(b) + ' res is ' + str(res)
print ' '
x = 16
b = 2
res = myLog(x, b)
print 'myLog: x is ' + str(x) + ' b is ' + str(b) + ' res is ' + str(res)
res = myLog1(x, b)
print 'myLog1: x is ' + str(x) + ' b is ' + str(b) + ' res is ' + str(res)
res = math.log(x,b)
print 'math.log: x is ' + str(x) + ' b is ' + str(b) + ' res is ' + str(res)
print ' '
x = 15
b = 3
res = myLog(x, b)
print 'myLog: x is ' + str(x) + ' b is ' + str(b) + ' res is ' + str(res)
res = myLog1(x, b)
print 'myLog1: x is ' + str(x) + ' b is ' + str(b) + ' res is ' + str(res)
res = math.log(x,b)
print 'math.log: x is ' + str(x) + ' b is ' + str(b) + ' res is ' + str(res)
print ' '

x = 500
b = 5
res = myLog(x, b)
print 'myLog: x is ' + str(x) + ' b is ' + str(b) + ' res is ' + str(res)
res = myLog1(x, b)
print 'myLog1: x is ' + str(x) + ' b is ' + str(b) + ' res is ' + str(res)
res = math.log(x,b)
print 'math.log: x is ' + str(x) + ' b is ' + str(b) + ' res is ' + str(res)
print ' '



    
    