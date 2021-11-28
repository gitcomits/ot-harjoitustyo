from calculations.tax_calculation import TaxCalculator
from ui.ui import UI


def main():

    u_x = UI()

    print(u_x.tax_percentage)
#    print(ux.monthly_salary, " monthly salary finds its way here")

    tax = TaxCalculator(u_x)


    tax.print_me()

    print(tax.calculate_income_after_tax())


if __name__ == "__main__":

    main()
