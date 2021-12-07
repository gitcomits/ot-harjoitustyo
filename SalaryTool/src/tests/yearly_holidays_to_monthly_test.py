import unittest
from calculations.yearly_holidays_to_monthly import YearlyHolidaysToMonthly

class TestYearlyHolidaysToMonthly(unittest.TestCase):

    def setUp(self):
        self.holidays = 24
        self.worked_months = {1:"t",2:"t",3:"t",4:"t",5:"t",6:"t",7:"t",8:"t",9:"t",10:"t",11:"t",12:"t"}
 

#    def test__init__(self):
#        yhtm = YearlyHolidaysToMonthly(self.holidays,self.worked_months)
#        self.assertEqual(yhtm.holidays, self.holidays) 
    
    def test_year_to_monthly(self):
        self.assertEqual(YearlyHolidaysToMonthly(self.holidays,self.worked_months).year_to_monthly(),2)