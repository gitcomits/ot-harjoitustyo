from calculations.tax_calculation import TaxCalculator
from ui.ui import UI

def main():

    ux = UI()

    print(ux.tax_percentage)
#    print(ux.monthly_salary, " monthly salary finds its way here")


    tax = TaxCalculator(ux)

 
#    tax.printMe()

    print(tax.calculate_income_after_tax())
 
if __name__ == "__main__":

    main()



