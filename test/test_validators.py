#!/usr/bin/env python

import unittest
from utils import mac_generator
from qav.validators import DateValidator, TupleValidator, \
    EmailValidator, HashValidator, IntegerValidator, \
    YesNoValidator, ListValidator, Validator, MacAddressValidator, \
    IPAddressValidator
from qav.filters import PreFilter


class TestValidators(unittest.TestCase):

    def setUp(self):
        pass

    def test_basic_validation(self):
        v = Validator()
        self.assertFalse(v.validate(''))
        v.blank = True
        self.assertTrue(v.validate(''))
        choice = 'new choice'
        v.validate(choice)
        self.assertEquals(choice, v._choice)

    def test_email_validator(self):
        v = EmailValidator()
        valid_email = 'example@example.com'
        self.assertTrue(v.validate(valid_email))
        self.assertEquals(v._choice, valid_email)
        self.assertTrue(v.validate('example@co.jp'))
        self.assertTrue(v.validate('example@example.student.edu'))
        self.assertFalse(v.validate('example@@example.com'))
        self.assertFalse(v.validate('example@examplecom'))
        self.assertFalse(v.validate('exampleexamplecom'))

    def test_integer_validator(self):
        v = IntegerValidator()
        self.assertTrue(v.validate(100))
        self.assertTrue(isinstance(v._choice, int))
        self.assertTrue(v.validate("100"))
        # string float to casted to int throws ValueError
        self.assertFalse(v.validate("100.12"))
        self.assertFalse(v.validate('letters'))

    def test_yes_no_validator(self):
        v = YesNoValidator()
        self.assertTrue(v.validate('yes'))
        self.assertTrue(v.validate('YES'))
        self.assertTrue(v.validate('YeS'))
        self.assertTrue(v.validate('NO'))
        self.assertTrue(v.validate('no'))
        self.assertTrue(v.validate('nO'))
        self.assertFalse(v.validate('yeah'))
        self.assertFalse(v.validate('nope'))

    def test_list_validator(self):
        choices = ['a', 'b', 'c', 'd']
        v = ListValidator(choices)
        self.assertTrue(v.validate('a'))
        self.assertFalse(v.validate('f'))

    def test_date_validator(self):
        v = DateValidator()
        v2 = DateValidator(blank=True)
        self.assertFalse(v.validate('1991101'))
        with self.assertRaises(ValueError):
            v.validate('19911410')  # invalid month
            v.validate('19911040')  # invalid day
            v.validate('09911040')  # invalid year
        self.assertTrue(v.validate('19911010'))
        self.assertTrue(v2.validate(''))
        self.assertEquals(None, v2._choice)

    def test_mac_address_validator(self):
        v = MacAddressValidator()
        self.assertTrue(v.validate('00:00:00:00:00:00'))
        self.assertFalse(v.validate('00:0g:00:00:00:00'))
        self.assertFalse(v.validate('00:0g:00:00:00:000'))
        mac = mac_generator()
        self.assertTrue(v.validate(mac))

    def test_ip_address_validator(self):
        v = IPAddressValidator()
        self.assertTrue(v.validate('192.168.1.12'))
        self.assertTrue(v.validate('192.168.7.1'))
        self.assertTrue(v.validate('10.10.17.12'))
        self.assertFalse(v.validate('256.10.17.25'))
        self.assertFalse(v.validate('192.256.17.25'))
        self.assertFalse(v.validate('215.10.256.25'))
        self.assertFalse(v.validate('10.10.17.256'))

    def test_ip_netmask_validator(self):
        pass

    def test_ip_uri_validator(self):
        pass

    def test_ip_tuple_validator(self):
        choices = [(1,'first'), (2,'second'), ('a','third')] 
        v = TupleValidator(choices)
        v.print_choices()
        self.assertTrue(v.validate('1'))
        self.assertTrue(v.validate('2'))
    #    v.filters =
        self.assertFalse(v.validate('4'))

    def test_hash_validator(self):
        pass
if __name__ == "__main__":
    unittest.main()