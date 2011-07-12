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
