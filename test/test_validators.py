#!/usr/bin/env python

import unittest
from qav.validators import CompactListValidator, DateValidator, \
    DomainNameValidator, EmailValidator, HashValidator, IntegerValidator, \
    YesNoValidator, CompactListValidator


class TestValidators(unittest.TestCase):

    def setUp(self):
        pass

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
#        self.assertFalse(v.validate(100.12))
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
#        self.assertFalse(v.validate(0))

    def test_compact_list_validator(self):
        choices = ['a', 'b', 'c', 'd']
        v = CompactListValidator(choices) 
        self.assertTrue(v.validate('a'))    
        self.assertFalse(v.validate('f'))    
#        self.assertFalse(v.validate(1))    
        
        
    def test_date_validator(self):
        pass

    def test_domain_name_validator(self):
        v = DomainNameValidator()
        self.assertFalse('google')
        self.assertFalse('google')
        self.assertTrue('google.co.jp')
        pass

    def test_mac_address_validator(self):
        pass
if __name__ == "__main__":
    unittest.main()
