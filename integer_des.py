import random as rnd
import string

class IntegerDescriptor(object):
    def __init__(self, default=0):
        self.name = ''.join(
            (rnd.choice(string.ascii_lowercase) for i in range(10))
        )
        self.default = default
  
    def __get__(self, inst, cls):
        return inst.__dict__.get(self.name, self.default)

    def __set__(self, inst, v):
        v = int(v) # May raise TypeError
        inst.__dict__[self.name] = v

    def __delete__(self, inst):
        del inst.__dict__[self.name]
