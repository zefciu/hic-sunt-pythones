from registered import RegisteredMeta

class A(object):
    __metaclass__ = RegisteredMeta

class B(object):
    __metaclass__ = RegisteredMeta

class C(A):
    pass

class D(C, B):
    pass

RegisteredMeta.view_graph()
