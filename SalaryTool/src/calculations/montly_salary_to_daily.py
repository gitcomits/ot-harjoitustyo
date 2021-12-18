from calculations.config_checks import ConfigChecks
class MonthlyToDaily:
    """Laskee kuukausipalkasta päiväpalkan
    käyttäää jakajana config tiedostossa määriteltyä arvoa

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
        self.c_c = ConfigChecks()


    def monthly_salary_to_daily(self):
        """Lasketaan päiväpalkka kuukausipalkasta. Päivien määrä päiväpalkan laskemiseen
        vaihtelee TES:stä riippuen, päivien määrän voi määritellä config tiedostossa
        arvon muodollinen oikeallisuus tarkastetaan ConfigChecks luokassa

        Returns:
            float: päiväpalkka laskettuna kuukausipalkasta
        """

        check_me = self.c_c.configuration_exists("conversion", "MonthlySalaryToDaily")

        if check_me[0]:
            d_d = check_me[1]
            d_d = self.c_c.monthly_salary_to_daily(d_d)
            if d_d[0]:
                days = d_d[1]
            else:
                self.c_c.information_lack("MonthlySalaryToDaily")


        else:
            self.c_c.information_lack("MonthlySalaryToDaily")


        self.daily_salary = self.monthly_salary/days
        return self.daily_salary
