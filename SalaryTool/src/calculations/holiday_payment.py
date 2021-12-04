
class HolidayPayment:

    def __init__(self, u_x):
        self.holidays = u_x.holidays                    # user input
        self.monthly_salary = u_x.monthly_salary
        self.paid_holiday_days = None
        self.days_withdrawn_from_payment = None
        self.holiday_payment = None
        self.daily_salary = None

    def holiday_payment_days(self):
        self.paid_holiday_days = self.holidays - (self.holidays//6)  # saturdays withdrawn from days
        return self.paid_holiday_days

    def withdrawn_days_from_payment(self):
        self.days_withdrawn_from_payment = self.holidays//6            # how many days were didacted
        return self.days_withdrawn_from_payment

    def monthly_salary_to_daily(self):
        self.daily_salary = self.monthly_salary/22                   # TES dependent, needs checking
        return self.daily_salary

    def calculate_holiday_money(self):
    #    self.holiday_payment_days()
    #    self.monthly_salary_to_daily()
        self.holiday_payment = (self.paid_holiday_days * self.daily_salary) * 0.5
        return self.holiday_payment
    