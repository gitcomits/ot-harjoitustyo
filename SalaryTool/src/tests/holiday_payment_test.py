import unittest
from calculations.holiday_payment import HolidayPayment

class TestHolidayPayment(unittest.TestCase):

    def setUp(self):

        self.holidays = 26                    
        self.monthly_salary = 1000
        self.paid_holiday_days = None
        self.days_withdrawn_from_payment = None
        self.holiday_payment = None
        self.daily_salary = None
        u_x = type('', (), {})()
        u_x.holidays = self.holidays
    #    self.u_x = UI()
    #    self.u_x.holidays = self.holidays
    #    self.u_x.holidays = self.holidays

#    def test_init_constructor(self,u_x):
#        self.assertEqual(HolidayPayment.__init__(self,u_x),self.holidays)


    def test_holiday_payment_days(self):
        hdp = HolidayPayment.holiday_payment_days(self)
        self.assertEqual(hdp, self.holidays - (self.holidays//6 ))

    def test_calculate_holiday_money(self):
        self.paid_holiday_days = 22
        self.daily_salary = self.monthly_salary/22
        self.assertEqual(HolidayPayment.calculate_holiday_money(self), 500)        

    def test_withdrawn_days_from_payment(self):
        self.assertEqual(HolidayPayment.withdrawn_days_from_payment(self),self.holidays//6)

    