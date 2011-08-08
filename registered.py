import subprocess as sp
import os
cls_registry = []

class RegisteredMeta(type):

    def __init__(cls, clsname, bases, dict_):
        for b in bases:
            cls_registry.append((b.__name__, clsname))

        return super(RegisteredMeta, cls).__init__(clsname, bases, dict_)

    @classmethod
    def view_graph(metacls):
        display = sp.Popen('dot -Tpng | display -', shell=True)

        display.stdin.write('digraph class_hierarchy {')
        for from_, to in cls_registry:
            display.stdin.write('{0} -> {1};'.format(from_, to))
        display.stdin.write('}')
        display.stdin.close()
