'''
Write a function that takes in a base and an exp and recursively computes baseexp. You are not allowed to
use the ** operator!
'''

def power(base, exp):
    print 'in power ', base, exp
    if exp == 0:
        return 1
    else:
        res = base * power(base, exp-1)
        print 'base ' , base, ' res ', res
        return res

x = power(2,4)
print ('2 to the power 3 ', x)