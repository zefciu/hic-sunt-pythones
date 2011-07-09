class Field(object):
    """Fields are descriptors used in versionable objects."""

    def __init__(self, **kwargs):
        if 'default' in kwargs:
            self.default = kwargs['default']


    def __set__(self, inst, v):
        if self.is_compatible(v):
            inst._current[self.name] = v
        else:
            raise TypeError('Type {0} is not compatible with {1}'.format(
                type(v), type(self)
            ))

    def __get__(self, inst, cls):
        try:
            return inst._current[self.name]
        except KeyError:
            if hasattr(self, 'default'):
                return self.default
            raise AttributeError(
                    'Field {0} not set and no default value'.format(self.name)
                )

    def __delete__(self, inst):
        try:
            del inst._current[self.name]
        except KeyError:
            raise AttributeError, 'Field {0} already unset'.format(self.name)

    def is_compatible(self, v):
        return True

