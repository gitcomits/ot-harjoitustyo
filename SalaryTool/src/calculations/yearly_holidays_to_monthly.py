class YearlyHolidaysToMonthly:

    def __init__(self, holidays, worked_months):

        self.holidays = holidays
        self.worked_months = worked_months

    def year_to_monthly(self):
        cnt = 0
        for k in self.worked_months.keys():
            for m_m in self.worked_months[k]:
                cnt += 1
        return self.holidays/cnt
