class Queue(object):
    """a basic implementation of a FIFO queue.  Uses lists"""

    def __init__(self):
        """Create an empty queue"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def remove(self):
        """Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self"""
        try:
             return self.vals.pop(0)
        except:
            raise ValueError('queue is empty')
