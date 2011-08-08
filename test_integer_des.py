import unittest as ut
from integer_des import IntegerDescriptor

class TestIntegerDescriptor(ut.TestCase):

    def setUp(self):
        class A(object):
            x = IntegerDescriptor(default = 1)

        self.a = A()

    def test_correct(self):
        self.a.x = 10
        self.assertEqual(self.a.x, 10)
       
    def test_round(self):
        self.a.x = 3.14159
        self.assertEqual(self.a.x, 3)

    def test_error(self):
        def wrong():
            self.a.x = 'abc'

        self.assertRaises(ValueError, wrong)

    def test_default(self):
        self.assertEqual(self.a.x, 1)


