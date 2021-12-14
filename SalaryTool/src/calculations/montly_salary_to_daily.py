import configparser
import os
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
        """Lasketaan päiväpalkka kuukausipalkasta. Päivien määrä päiväpalkan laskemiseen
        vaihtelee TES:stä riippuen, päivien määrän voi määritellä config tiedostossa

        Returns:
            float: päiväpalkka laskettuna kuukausipalkasta
        """

        path = os.getcwd() + "/config/config.cfg"
        parser = configparser.ConfigParser()

        parser.read(path)
        days =int(parser.get("config", "MonthlySalaryToDaily"))


        self.daily_salary = self.monthly_salary/days
        return self.daily_salary
