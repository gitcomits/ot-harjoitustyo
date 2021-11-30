from calculations.tax_calculation import TaxCalculator
from calculations.holiday_payment import HolidayPayment
from ui.ui import UI




def main():

    u_x = UI()

    holiday_money = HolidayPayment(u_x)

#    holiday_money.holiday_payment_days()

    holiday_money.calculate_holiday_money()

#    print("look at tat")
    print(u_x.tax_percentage)
#    print(ux.monthly_salary, " monthly salary finds its way here")

    tax = TaxCalculator(u_x)


    tax.print_me()

    print(tax.calculate_income_after_tax())


if __name__ == "__main__":

    main()
