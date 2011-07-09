from field import Field

class VersionableMeta(type):
    def __init__(cls, clsname, bases, dict_):
        cls.fields = []
        for n, f in dict_.iteritems():
            if isinstance(f, Field):
                f.name = n
                cls.fields.append(f)

        if '__repr_format__' in dict_:
            def rpr(self):
                params = self._current.copy()
                params['version'] = self._version
                for f in cls.fields:
                    if hasattr(f, 'default'):
                        params.setdefault(f.name, f.default)
                return dict_['__repr_format__'].format(**params)

            cls.__str__ = rpr
            cls.__repr__ = rpr
            dict_['s'] = rpr


        return super(VersionableMeta, cls).__init__(clsname, bases, dict_)

class Versionable(object):
    __metaclass__ = VersionableMeta
    
    def __init__(self):
        self._current = {}
        self._versions = []
        self._version = None

    def commit(self):
        self._versions.append(self._current.copy())
        self._version = len(self._versions)
        return self._version

    def checkout(self, version):
        if self._version and self._current != self._versions[self._version - 1]:
            raise Exception, 'Uncommited changes exist'
        else:
            self._version = version
            self._current = self._versions[self._version -1].copy()

    def revert(self):
        self._current = self._versions[self._version - 1].copy()
