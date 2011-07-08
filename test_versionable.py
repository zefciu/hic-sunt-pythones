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
            title = Field(name = 'title', default = 'Pan/Pani')
            name = Field(name = 'name')
            wage = Numeric(name = 'wage')

        self.Person = Person
        self.p = Person()
        self.p.title = 'Panna'
        self.p.name = 'Anna Kowalska'
        self.p.wage = 2500.0
        self.maiden_v = self.p.commit()

        self.p.title = 'Pani'
        self.p.name = 'Anna Nowak'
        self.p.wage = 3100
        self.married_v = self.p.commit()

    def test_checkout(self):


        self.p.checkout(self.maiden_v)
        self.assertEqual(self.p.name, 'Anna Kowalska')
        self.p.checkout(self.married_v)
        self.assertEqual(self.p.name, 'Anna Nowak')

        self.p.wage = 3200

        def wrong():
            self.p.checkout(self.maiden_v)
        self.assertRaises(Exception, wrong)

    def test_revert(self):

        self.p.name = 'Anna Wisniewska'
        self.p.revert()

        self.assertEqual(self.p.name, 'Anna Nowak')

    def test_multiple(self):
        self.q = self.Person()
        self.q.name = 'Jan Zawadzki'
        self.assertEqual(self.p.name, 'Anna Nowak')
        self.assertEqual(self.q.name, 'Jan Zawadzki')
        
