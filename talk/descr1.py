class Field(object):
    """Fields are descriptors used in versionable objects."""

    def __init__(self, name, **kwargs):
        self.name = name
        if 'default' in kwargs:
            self.default = kwargs['default']


    def __set__(self, inst, v):
        if self.is_compatible(v):
            inst._current[self.name] = v
        else:
            raise TypeError('Type {0} is not compatible with {1}'.format(
                type(v), type(self)
            ))
        
    def is_compatible(self, v):
        return True
