#from ui.ui import UI
class TaxCalculator():

    def __init__(self, u_x):
        #user_input = UI()
        user_input = u_x

        self.mo_salary = user_input.monthly_salary
        self.tax = user_input.tax_percentage
        

    def print_me(self):
        print(self.mo_salary, "kuukausipalkka siirtynyt tax calculatoriin")

# income - tax
    def calculate_income_after_tax(self):
        if self.tax == 0:
            return self.mo_salary
#            sum = self.mo_salary * ((100 - self.tax)/100)
        return self.mo_salary * ((100 - self.tax)/100)
