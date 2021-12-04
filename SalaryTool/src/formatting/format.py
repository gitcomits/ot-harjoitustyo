# This class reformats the given information, fills the empty months, for easier printout
# Order in new_order is as follows
# Net salary, gross salary, full-/part-time percentage 
import calendar

from calculations.part_time_calculation import PartTimeCalculator
from calculations.tax_calculation import TaxCalculator

class Format:

    def __init__(self, u_x):

        self.monthly_salary = u_x.monthly_salary
        self.caclulation_salary = 0
        self.m_div = u_x.m_div
        self.tax_percentage = u_x.tax_percentage
        #self.prop = u_x.prop
        self.net = 0
        self.gross = 0
        self.diff = 0
        self.cal = calendar
        self.months = [1,2,3,4,5,6,7,8,9,10,11,12]
        self.new_order = {}
        self.tax_calculation = TaxCalculator(self)
        self.p_t_c = PartTimeCalculator(self.monthly_salary)

    def re_format(self):
        print(self.tax_percentage, "tax percentage")
        
        for m in self.months:                               #months in string
            self.new_order[m] = calendar.month_abbr[m]

 
        for key in self.m_div.keys():
            for month in self.m_div[key]:

                if key == 100:
                    s = self.new_order[month] 
                    s += ":" + str(self.monthly_salary)                                 #net salary per month
                    s += ":" + str(self.tax_calculation.calculate_income_after_tax())   #gross salary per month
                    s += ":" + str(key)                                                 #full time/part time
                    self.new_order[month] = s                    
                    
                    self.net += self.monthly_salary                                          #net salary whole period   
                    self.gross += self.tax_calculation.calculate_income_after_tax()            #gross salary whole period

                else: 
                    s = self.new_order[month] 
                    s += ":" + str(self.p_t_c.calculate_part_time_salary(key))                  #net salary per month
                     
                    temp = self.monthly_salary 
                    self.monthly_salary = self.p_t_c.calculate_part_time_salary(key)
                    self.net += self.monthly_salary
                    self.part_time_tax_calculation = TaxCalculator(self)
                    s += ":" + str(self.part_time_tax_calculation.calculate_income_after_tax())   #gross salary per month    
                    self.gross += self.part_time_tax_calculation.calculate_income_after_tax()
                    self.monthly_salary = temp
                    s += ":" + str(key)                                                 #full time/part time
                    self.new_order[month] = s
 
        
        print(self.new_order)

