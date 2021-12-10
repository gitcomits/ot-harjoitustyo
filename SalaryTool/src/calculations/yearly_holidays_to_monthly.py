class YearlyHolidaysToMonthly:
    """Jakaa syötetyn vuosiloman niille kuukausille joille töitä on tehty  
        
    Attributes:
        holidays: syötetyt lomapäivät
        worked months: lista jossa kuukaudet joina tehty töitä  
    """

    def __init__(self, holidays, worked_months):
        """Luodaan muuttujat alla oleville funktioille

        Args:
            holidays (int): vuosiloma päivät
            worked_months (dict): dictionary jossa kuukaudet joilla tehty töitä
        """

        self.holidays = holidays
        self.worked_months = worked_months

    def year_to_monthly(self):
        """Lasketaan vuosilomista kuukausikohtaiset päivät

        Returns:
            float: vuosilomapäivät per työtä tehty kuukausi
        """

        cnt = 0
        for k in self.worked_months.keys():
            for m_m in self.worked_months[k]:
                cnt += 1
        return self.holidays/cnt
