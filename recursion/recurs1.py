'''
sum input number down to 1 ie if 5 is parameter, add 5+4+3+2+1
'''
def total(x):
    print 'total has been called with', x
    if x > 1:
        print 'in if'
        res = x + total(x-1)
#        print("intermediate result for ", x, " + total (" ,x-1, "): ",res)
        print 'returning res ', res
        return res
    else:
        print 'in else'
        return 1
        
x = total(10)
print 'total is ', x
	 