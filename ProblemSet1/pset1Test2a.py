def countBob(s):
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
                    
                    
                
        
    