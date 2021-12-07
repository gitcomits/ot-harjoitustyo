
class PartTimeCalculator:

    def __init__(self, data):
        self.monthly_salary = data

    def calculate_part_time_salary(self,key):
        return self.monthly_salary * (key/100)
