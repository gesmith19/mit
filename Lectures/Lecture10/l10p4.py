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
    
def search2(L, e):
    print ' '
    print 'e is ' + str(e)
    print 'L is ' + str(L)
    for i in L:
        if i == e:
            print str(i)
            return True
        elif i > e:
            return False
    return False

def search3(L, e):
    print("List L: " + str(L))
    if L[0] == e:
        return True
    elif L[0] > e:
        return False
    else:
        return search3(L[1:], e)
        
def search3a(L, e):
    # Test if the list is empty - if it is, e cannot be in it!
    # Run this test first - so that we don't throw an error trying
    #  to access L[0].
    if L == []:
        return False

    if L[0] == e:
        return True
    elif L[0] > e:
        return False
    else:
        return search3(L[1:], e)    

L=[2,5,9,13,15,101,555]
res = False
res1 = False


#e = 17
e = 565
res = search(L, e)
print res
res1 = search3(L,e)
print res1

e = 555
res = search(L, e)
print res
res1 = search3(L,e)
print res1

e = 15
res = search(L, e)
print res
res1 = search3(L,e)
print res1

L1 = [5]
L2 = []

e = 15
res = search(L1, e)
print res
res1 = search3(L1,e)
print res1

e = 5
res = search(L1, e)
print res
res1 = search3(L1,e)
print res1

e = 15
res = search(L2, e)
print res
res1 = search3(L2,e)
print res1

e = 5
res = search(L2, e)
print res
res1 = search3(L2,e)
print res1