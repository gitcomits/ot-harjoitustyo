
class HolidayPayment:
    """Laskee --> lomarahan osuuden palkasta, lomarahan osaikaisesta työsta, sekä "aidot" lomapäivät

    Attributes:
        u_x: UI:stä saadut syötteet
    """

    def __init__(self, u_x):
        """Luokan konstruktori jossa määritellään muuttujat tuleville funktioille

        Args:
            u_x (object): sisältää UI luokassa syötteenä annetut tiedot
        """

        self.holidays = u_x.holidays
        self.monthly_salary = u_x.monthly_salary
        self.paid_holiday_days = u_x.paid_holiday_days
        self.days_withdrawn_from_payment = None
        self.holiday_payment = None
        self.daily_salary = u_x.daily_salary

    def holiday_payment_days(self):
        """Poistaa lomapäivistä lauantait, palautta aidon määrän lomapäiviä

        Returns:
            int: oikea määrä päiviä joita voi olla töistä poissa
        """

        self.paid_holiday_days = self.holidays - (self.holidays//6)
        return self.paid_holiday_days

    def withdrawn_days_from_payment(self):
        """Kuinka monta päivää, lauantaita, poistettiin lomapäivien määrästä

        Returns:
            int: määrä päiviä joita ei voi olla poissa töistä vaikka kuuluvatkin lomapäiviin
        """

        self.days_withdrawn_from_payment = self.holidays//6
        return self.days_withdrawn_from_payment

    def calculate_holiday_money(self):
        """Laskee lomarahan ajalta jolloin oli kokopäiväisesti töissä

        Returns:
            float: lomarahan osuus palkasta
        """

        self.holiday_payment = (self.paid_holiday_days * self.daily_salary) * 0.5
        return self.holiday_payment

    def calculate_holiday_money_part_time(self, coefficient):
        """Laskee lomarahan ajalta jolloin oli osa-aikaisesti töissä

        Args:
            coefficient (int): osa-aikaisuus työajasta

        Returns:
            float: lomarahan osuus palkasta
        """

        self.holiday_payment = ((self.paid_holiday_days * self.daily_salary) * 0.5)\
         * (coefficient/100)
        return self.holiday_payment
