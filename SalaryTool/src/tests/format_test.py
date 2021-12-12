import unittest
from formatting.format import Format

class TestFormat(unittest.TestCase):

    def setUp(self):
        
        self.u_x = type('', (), {})()
        self.u_x.monthly_salary = 1000
        self.u_x.tax_percentage   = 50
        self.u_x.m_div = {100: 1}
        self.u_x.holidays = 20
        


    def test_re_format(self):
        pass