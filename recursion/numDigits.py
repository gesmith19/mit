def digitsNum(x):
    if x < 10:
        return 1
    else:
        res = digitsNum(x/10)
        return 1 + res
        

x = digitsNum(15)
print ' input 15 and return is ', x
x = digitsNum(15105)
print ' input 105 and return is ', x
x = digitsNum(1)
print ' input 1 and return is ', x