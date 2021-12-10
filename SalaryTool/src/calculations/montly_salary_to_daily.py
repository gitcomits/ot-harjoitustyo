class MonthlyToDaily:
    """Laskee kuukausipalkasta päiväpalkan

    Attributes:
        monthly_salary: kuukausipalkka
    """


    def __init__(self, monthly_salary):
        """Luokan konstruktori jossa määritellään muuttujat tuleville funktioille

        Args:
            monthly_salary (float): kuukausipalkka
        """

        self.monthly_salary = monthly_salary
        self.daily_salary = float()


    def monthly_salary_to_daily(self):
        """Lasketaan päiväpalkka kuukausipalkasta

        Returns:
            float: päiväpalkka laskettuna kuukausipalkasta
        """

        self.daily_salary = self.monthly_salary/22
        return self.daily_salary
        