class MonthlyToDaily:

    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary
        self.daily_salary = float()


    def monthly_salary_to_daily(self):
        self.daily_salary = self.monthly_salary/22                   # TES dependent, needs checking
        return self.daily_salary
        