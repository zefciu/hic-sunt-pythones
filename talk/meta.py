class VersionableMeta(type):
    def __init__(cls, clsname, bases, dict_):
        cls.fields = []
        for n, f in dict_.iteritems():
            if isinstance(f, Field):
                f.name = n
                cls.fields.append(f)
                
        return super(VersionableMeta, cls).__init__(clsname, bases, dict_)

# python 2.x
class Versionable(object):
    __metaclass__ = VersionableMeta
    # ...

# python 3.x
class Versionable(object, metaclass=VersionableMeta):
    # ...
