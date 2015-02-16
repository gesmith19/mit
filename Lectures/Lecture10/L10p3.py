num = 6
L = [5, 0, 2, 4, 6, 3, 1]
val = 0
for i in range(0, num):
    print 'i is ' + str (i) + ' val is ' + str(L[val]), 
    val = L[L[val]]
    print ' val is '  + str(val)
