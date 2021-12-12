import unittest
from calculations.holiday_payment import HolidayPayment

class TestHolidayPayment(unittest.TestCase):

    def setUp(self):

        self.holidays = 26                    
        self.monthly_salary = 1000
        self.paid_holiday_days = 2
        self.days_withdrawn_from_payment = None
        self.holiday_payment = None
        self.daily_salary = 200
        u_x = type('', (), {})()
        u_x.holidays = self.holidays
        u_x.monthly_salary = 1000
        u_x.paid_holiday_days = 20
        u_x.daily_salary = 50

    def test_holiday_payment_days(self):
        hdp = HolidayPayment.holiday_payment_days(self)
        self.assertEqual(hdp, self.holidays - (self.holidays//6 ))

    def test_calculate_holiday_money(self):
        self.paid_holiday_days = 22
        self.daily_salary = self.monthly_salary/22
        self.assertEqual(HolidayPayment.calculate_holiday_money(self), 500)        

    def test_withdrawn_days_from_payment(self):
        self.assertEqual(HolidayPayment.withdrawn_days_from_payment(self),self.holidays//6)

    def test_calculate_holiday_money_part_time(self):
        self.assertEqual(HolidayPayment.calculate_holiday_money_part_time(self, 50), 100)   
    

    def test_class_init_value(u_x):
        o = HolidayPayment(u_x)
        #self.assertEqual(o.paid_holiday_days,20)