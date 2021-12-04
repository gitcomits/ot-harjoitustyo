
class PartTimeCalculator:

    def __init__(self, data):
        self.monthly_salary = data

    def calculate_part_time_salary(self,key):
    #    print("this should be 30 protp -->", self.prop)
        return (self.monthly_salary * (key/100))
    #    return (self.monthly_salary * (self.prop/100))

