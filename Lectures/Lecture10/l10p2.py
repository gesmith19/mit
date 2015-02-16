def search(L, e):
    print ' '
    print 'e is ' + str(e)
    print 'L is ' + str(L)
    for i in range(len(L)):
        print str(L[i])
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
    
def search1(L, e):
    print ' '
    print 'e is ' + str(e)
    print 'L is ' + str(L)
    for i in L:
        print str(i)
        if i == e:
            return True
        if i > e:
            return False
    return False
    

L=[2,5,9,13,15,101,555]
res = False
res1 = False

e = 17
res = search(L, e)
print res
res1 = search1(L,e)
print res1

e = 555
res = search(L, e)
print res
res1 = search1(L,e)
print res1

e = 15
res = search(L, e)
print res
res1 = search1(L,e)
print res1

L1 = [5]
L2 = []

e = 15
res = search(L1, e)
print res
res1 = search1(L1,e)
print res1

e = 5
res = search(L1, e)
print res
res1 = search1(L1,e)
print res1

e = 15
res = search(L2, e)
print res
res1 = search1(L2,e)
print res1

e = 5
res = search(L2, e)
print res
res1 = search1(L2,e)
print res1