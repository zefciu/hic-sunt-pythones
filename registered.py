import subprocess as sp
cls_registry = []

class RegisteredMeta(type):

    def __init__(cls, clsname, bases, dict_):
        for b in bases:
            cls_registry.append((b.__name__, clsname))

        return super(RegisteredMeta, cls).__init__(clsname, bases, dict_)

    @classmethod
    def view_graph(metacls):
        dot = sp.Popen(['dot', '-Tpng'], stdin=sp.PIPE, stdout=sp.PIPE)
        buf = ['digraph class_hierarchy {']

        for from_, to in cls_registry:
            buf.append('{0} -> {1};'.format(from_, to))
        buf.append('}')

        data, err = dot.communicate(''.join(buf))
        display = sp.Popen(['display', '-'], stdin=sp.PIPE)
        display.communicate(data)
