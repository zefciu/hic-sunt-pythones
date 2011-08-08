import unittest as ut
from registered import RegisteredMeta, cls_registry

class TestRegistered(ut.TestCase):
    def test_registry(self):

        class A(object):
            __metaclass__ = RegisteredMeta

        class B(object):
            __metaclass__ = RegisteredMeta

        class C(A):
            pass

        class D(C, B):
            pass

        self.assertEqual(
            set(cls_registry),
            set([
                ('object', 'A'),
                ('object', 'B'),
                ('A', 'C'),
                ('C', 'D'),
                ('B', 'D'),
            ])
        )
