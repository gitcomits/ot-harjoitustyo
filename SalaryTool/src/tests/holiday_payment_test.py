import unittest
from calculations.holiday_payment import HolidayPayment


class TestHolidayPayment(unittest.TestCase):

    def setUp(self):
        self.number = 1                           # default validation test value

        self.holidays = 26                    
        self.monthly_salary = 1000
        self.paid_holiday_days = None
        self.days_withdrawn_from_payment = None
        self.holiday_payment = None
        self.daily_salary = None

    def test_holiday_payment_days(self):
        hdp = HolidayPayment.holiday_payment_days(self)
        self.assertEqual(hdp, self.holidays - (self.holidays//6 ))

    def test_monthly_salary_to_daily(self):
        ds = self.monthly_salary/22
        self.assertEqual(HolidayPayment.monthly_salary_to_daily(self),ds)

    def test_calculate_holiday_money(self):
        self.paid_holiday_days = 22
        self.daily_salary = self.monthly_salary/22
        self.assertEqual(HolidayPayment.calculate_holiday_money(self), 500)        

    def test_withdrawn_days_from_payment(self):
        self.assertEqual(HolidayPayment.withdrawn_days_from_payment(self),self.holidays//6)

    def test_validation(self):                    # to validate that something is working
        x = int(self.number)
        self.assertEqual(int(self.number), 1 * x)
    