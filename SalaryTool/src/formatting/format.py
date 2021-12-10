# This class reformats the given information, fills the empty months, for easier printout
# Order in new_order is as follows
# Month abreavation, Net salary, gross salary, full-/part-time percentage,
# earned holiday payment net, earned holiday payment gross
import calendar

from calculations.part_time_calculation import PartTimeCalculator
from calculations.tax_calculation import TaxCalculator
from calculations.holiday_payment import HolidayPayment
from calculations.montly_salary_to_daily import MonthlyToDaily
from calculations.yearly_holidays_to_monthly import YearlyHolidaysToMonthly
class Format:
    """Formatoi datan helpommin käsiteltävään muotoon dictionary muuttujaan  
        
    Attributes:
        u_x: käyttäjän syöttämät arvot UI luokassa 
    """

    def __init__(self, u_x):
        """Luokan konstruktori, määritellään muuttujat

        Args:
            u_x (object): UI luokassa syötetyt tiedot
        """

        self.monthly_salary = u_x.monthly_salary
        self.caclulation_salary = 0
        self.m_div = u_x.m_div
        self.tax_percentage = u_x.tax_percentage
        self.holidays = u_x.holidays
        self.paid_holiday_days = float()
        self.gathered_holiday_per_month = int()
        self.net = 0
        self.gross = 0
        self.diff = 0
        self.hol_mon = 0
        self.cal = calendar
        self.months = [1,2,3,4,5,6,7,8,9,10,11,12]
        self.new_order = {}
        self.tax_calculation = TaxCalculator(self)
        self.p_t_c = PartTimeCalculator(self.monthly_salary)
        self.daily_salary = MonthlyToDaily(self.monthly_salary).monthly_salary_to_daily()
        self.paid_holiday_days = YearlyHolidaysToMonthly(self.holidays,\
        self.m_div).year_to_monthly()
        self.h_p = HolidayPayment(self)

    def re_format(self):
        """Tehdään datan uudelleen formatointi new_order dictionariin, samalla tehdään laskutoimenpiteitä lomarahoihin ja lomapäiviin sekä
        verot lasketaan palkalle ja lomarahoille
        """

        for m_m in self.months:                               #months in string
            self.new_order[m_m] = calendar.month_abbr[m_m]
        inputed_months = []
        for key in self.m_div.keys():
            for month in self.m_div[key]:
                inputed_months.append(month)

                if key == 100:
                    s_s = self.new_order[month]
                    s_s += ": Veroton >>" + str(self.monthly_salary) #net salary per month
                    #gross salary per month
                    s_s += ": VEROTETTU >>" + str(round(self.tax_calculation.\
                        calculate_income_after_tax(),2))
                    s_s += ": Työaikaosuus >>" + str(key)     #full time/part time
                    s_s += ": lomaraha veroton >>" + str(self.h_p.calculate_holiday_money())
                    #holiday money per month
                    s_s += ": lomaraha VEROTETTU>>" + str(round(self.tax_calculation.\
                    calculate_holiday_money_after_tax(self.h_p.calculate_holiday_money()),2))
                    self.new_order[month] = s_s
                    self.net += self.monthly_salary                 #net salary whole period
                    #gross salary whole period
                    self.gross += self.tax_calculation.calculate_income_after_tax()
                    self.hol_mon += self.h_p.calculate_holiday_money()

                else:
                    s_s = self.new_order[month]
                    #net salary per month
                    s_s += ": Veroton >> " + str(round(self.p_t_c.calculate_part_time_salary(key)\
                    ,2))
                    temp = self.monthly_salary
                    self.monthly_salary = self.p_t_c.calculate_part_time_salary(key)
                    self.net += self.monthly_salary
                    self.part_time_tax_calculation = TaxCalculator(self)
                    #gross salary per month
                    s_s += ": VEROTETTU >> " + str(round(self.part_time_tax_calculation.\
                    calculate_income_after_tax(),2))
                    self.gross += self.part_time_tax_calculation.calculate_income_after_tax()
                    s_s += ": työaikaosuus >> " + str(key)  #full time/part time
                    s_s += ": lomaraha veroton >>" + str(round(self.h_p.\
                    calculate_holiday_money_part_time(key),2))
                    self.monthly_salary = self.h_p.calculate_holiday_money_part_time(key)
                    s_s += ": lomaraha VEROTETTU >>" + str(round(self.part_time_tax_calculation.\
                    calculate_holiday_money_after_tax(self.h_p.calculate_holiday_money_part_time\
                    (key)),2))
                    self.monthly_salary = temp
                    self.new_order[month] = s_s

        zero_months = set(self.months) - set(inputed_months)
        if len(zero_months) > 0:                         # zero fill for none inserted months
            for z_m in zero_months:
                s_s = self.new_order[z_m]
                s_s += ":0:0:0:0"
                self.new_order[z_m] = s_s

        for n_n in self.new_order.keys():                # temp print before next step
            print(self.new_order[n_n])
