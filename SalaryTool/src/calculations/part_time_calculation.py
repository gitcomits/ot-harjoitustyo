class PartTimeCalculator:
    """Laskee kuukausipalkasta osa-aikaisen palkan osa-aikaisuus coefficientin avulla 
        
    Attributes:
        monthly_salary: kuukausipalkka 
    """


    def __init__(self, monthly_salary):
        """Luokan konstruktori jossa määritellään muuttujat tuleville funktioille
        
        Args:
            monthly_salary (float): käyttäjän syöttämä kuukausipalkka
        """

        self.monthly_salary = monthly_salary

    def calculate_part_time_salary(self,coefficient):
        """Lasketaan osa-aikainen palkka coefficientin avulla

        Args:
            coefficient (int): käyttäjän syöttämä osa-aikaisuus prosentti

        Returns:
            float: osa-aika palkka
        """

        return self.monthly_salary * (coefficient/100)
