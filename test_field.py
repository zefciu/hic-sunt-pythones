import unittest as ut
from field import Field
from versionable import Versionable

class Numeric(Field):
    def is_compatible(self, v):
        if isinstance(v, (int, float)):
            return True
        return False

class Test(ut.TestCase):
    def setUp(self):

        class Person(Versionable):
            title = Field(default = 'Pan/Pani')
            name = Field()
            wage = Numeric()

        self.Person = Person
        self.p = Person()

    def test_wrong_type(self):
        def wrong():
            self.p.wage = 'xyz'
        self.assertRaises(TypeError, wrong)

    def test_set_get(self):
        self.p.title = 'Pan'
        self.assertEqual(self.p.title, 'Pan')

    def test_get_default(self):
        self.assertEqual(self.p.title, 'Pan/Pani')

    def test_get_unset(self):
        self.assertRaises(AttributeError, lambda: self.p.name)

    def test_set_del_get(self):
        self.p.name = 'Anna'
        self.p.title = 'Pani'
        self.assertEqual(self.p.name, 'Anna')
        self.assertEqual(self.p.title, 'Pani')
        del self.p.name
        del self.p.title
        self.assertEqual(self.p.title, 'Pan/Pani')
        self.assertRaises(AttributeError, lambda: self.p.name)

    def test_double_del(self):

        def wrong():
            del self.p.name

        self.assertRaises(AttributeError, wrong)
            



