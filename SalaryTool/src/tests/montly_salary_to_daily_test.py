import unittest
from calculations.montly_salary_to_daily import MonthlyToDaily

class TestMonthlyToDaily(unittest.TestCase):

    def setUp(self):

        self.monthly_salary = 2200
        self.daily_salary = float()

    def test_monthly_salary_to_daily(self):
        ds = self.monthly_salary/22
        self.assertEqual(MonthlyToDaily.monthly_salary_to_daily(self),ds)


    def test_class_init_value(self):
        o = MonthlyToDaily(self.monthly_salary).__init__(333)
        self.assertEqual(MonthlyToDaily(self.monthly_salary).__init__(333),o)
        