class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
        
    def __len__(self):
        ''' returns the number of elements in the set'''
        return len(self.vals)
        
    def intersect(self, s2):
        res = intSet()
        for e in self.vals:
#            print 'e is ' + str(e)
            if s2.member(e) == True:
#                print('is in other set')
                res.insert(e)
#                print res
        return res
        
s = intSet()
s.insert(1)
s.insert(2)
s.insert(3)
s.insert(4)
s.insert(5)

s1 = intSet()
s1.insert(1)
s1.insert(3)
s1.insert(5)
s1.insert(7)
s1.insert(9)

s2 = intSet()

res =  s.intersect(s1)
print res
        
