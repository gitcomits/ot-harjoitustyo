class TaxCalculator():
    """Laskee veron kuukausipalkasta sekä lomarahasta

    Attributes:
        u_x: käyttäjän syöttämät arvot UI luokassa
    """

    def __init__(self, u_x):
        """Luokan konstruktori, luodaan muuttujat funktioille

        Args:
            u_x ([type]): [description]
        """
        self.mo_salary = u_x.monthly_salary
        self.tax = u_x.tax_percentage


    def calculate_income_after_tax(self):
        """lasketan ja vähennetään veron osuus palkasta

        Returns:
            float: palkka - verot
        """

        if self.tax == 0:
            return self.mo_salary
        return self.mo_salary * ((100 - self.tax)/100)


    def calculate_holiday_money_after_tax(self, holiday_money):
        """lasketaan ja vähennetään vero lomarahasta

        Args:
            holiday_money (float): lomaraha

        Returns:
            float: lomaraha - verot
        """

        if self.tax == 0:
            return holiday_money
        return holiday_money * ((100 - self.tax)/100)
