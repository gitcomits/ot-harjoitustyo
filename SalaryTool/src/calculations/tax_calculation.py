# from ui.ui import UI
class TaxCalculator():

    def __init__(self, ux):
#            user_input = UI()
            user_input = ux

            self.mo_salary = user_input.monthly_salary 
            self.tax = user_input.tax_percentage
            


    def printMe(self):
        print(self.mo_salary, "kuukausipalkka siirtynyt tax calculatoriin")


    def calculate_income_after_tax(self):                   # income - tax
        if(self.tax == 0):
            return self.mo_salary
        else:
            sum = self.mo_salary * ((100 - self.tax)/100)
            return sum
