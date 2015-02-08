def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    if n == 0:
        return True
    elif n < 0:
        return False
    else:
        return McNuggets(n - 6) or McNuggets(n - 9) or McNuggets(n - 20)

n = 6
x = McNuggets(n)
print 'n is ' + str(n) + ' x is ' + str(x)

n = 9
x = McNuggets(n)
print 'n is ' + str(n) + ' x is ' + str(x)

n = 20
x = McNuggets(n)
print 'n is ' + str(n) + ' x is ' + str(x)

n = 29
x = McNuggets(n)
print 'n is ' + str(n) + ' x is ' + str(x)

n = 72
x = McNuggets(n)
print 'n is ' + str(n) + ' x is ' + str(x)

n = 19
x = McNuggets(n)
print 'n is ' + str(n) + ' x is ' + str(x)