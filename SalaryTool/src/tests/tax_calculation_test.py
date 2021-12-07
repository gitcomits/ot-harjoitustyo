import unittest
from calculations.tax_calculation import TaxCalculator


class TestTaxCalculation(unittest.TestCase):

    def setUp(self):

        self.mo_salary = int(1000)
        self.monthly_salary = int(1000)
        self.holiday_money = int(1000)
        self.tax = float(20)
        self.tax_percentage = float(20)
        self.tcalculate = TaxCalculator(self)

    def test_tax_calculation(self):               # income - tax
        income_after_tax = TaxCalculator.calculate_income_after_tax(self)
        self.assertEqual(income_after_tax, 800)

    def test_tax_calculation_with_0_tax(self):             # no tax deducted with 0 tax percentage
        self.tax = float(0)
        income_after_tax = TaxCalculator.calculate_income_after_tax(self)
        self.assertEqual(income_after_tax, 1000)

    def test_calculate_holiday_money_after_tax_with_no_tax(self):
        self.tax = 0
        self.assertEqual(TaxCalculator.calculate_holiday_money_after_tax(self,self.holiday_money),self.holiday_money)

    def test_calculate_holiday_money_after_tax(self):
        self.tax = 20
        self.assertEqual(TaxCalculator.calculate_holiday_money_after_tax(self,self.holiday_money),800)
