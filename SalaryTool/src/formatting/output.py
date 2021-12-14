
from formatting.pdf_output import PdfOutput

class OutPut:
    """Luodaan otsikot sekä tulostetaan kasattu dataa ruudulle sekä kutsuu
    PdfOutput luokkaa pdf tallennusta varten

        Attributes:

        """

    def __init__(self):
        """Luokan konstruktori, määritellään muuttujat sekä PdfOutput

        Args:
        """

        self.holiday_net = 0
        self.holiday_gross = 0
        self.net = 0
        self.gross = 0
        self.pdf_text = []
        self.pdf_output = PdfOutput()

    def _print_to_screen(self):
        """Rivi riviltä tulostus ruudulle
        """

        print("\n\n")
        for t_o in self.pdf_text:
            if t_o == "NewPage":
                print("\n")
                continue
            print(t_o)
            if t_o[-1] == ":":
                print("\n")

    def to_screen(self, new_order):
        """UI:ssa syötetty dataa formatoidaan vielä vähän ennen ruudulle
        tulostusta sekä tallennetaan muotoon josta helposti luodaan pdf tiedosto

        Args:
            new_order (dictionary): sisältää käyttäjän syöttämän datan helposti
            tulostettavassa järjestyksess
        """

        text = " Payment information:"
        self.pdf_text.append(text)
        text = "Month".center(12) + "Gross".center(12) +"Net".center(12)\
        + "Holiday Gross".center(20)\
        + "Holiday net".center(20) + "Worktime %".center(10)
        self.pdf_text.append(text)

        for month in new_order:
            l_i = new_order[month].split(":")
            text = l_i[0].center(12) + l_i[1].center(12) + l_i[2].center(12) + l_i[4].center(20)\
            + l_i[5].center(20) + l_i[3].center(10)
            self.pdf_text.append(text)
            self.holiday_net += float(l_i[5])
            self.holiday_gross += float(l_i[4])
            self.gross += float(l_i[1])
            self.net += float(l_i[2])

        self.pdf_text.append("NewPage")
        text = " Actual payment:"
        self.pdf_text.append(text)
        text = "Month".center(12) + "Net".center(12) + "HP".center(12)
        self.pdf_text.append(text)

        for month in new_order:
            l_i = new_order[month].split(":")
            if month == 6:
                tot = float(l_i[2]) + round(self.holiday_net,2)
                text = l_i[0].center(12) + str(round(tot,2)).center(12)\
                    + str(round(self.holiday_net,2)).center(12)
                self.pdf_text.append(text)

            else:
                if l_i[2] != str(0):
                    text = l_i[0].center(12) + l_i[2].center(12)
                    self.pdf_text.append(text)

    #    self.pdf_text.append("NewPage")
        text = " Yearly Summary:"
        self.pdf_text.append(text)
        text = "Gross".center(12) + "Net".center(12) + "HP".center(12)
        self.pdf_text.append(text)
        year_gross = self.gross + self.holiday_gross
        year_net = self.net + self.holiday_net
        text = str(round(year_gross,2)).center(12) + str(round(year_net,2)).center(12)\
        + str(round(self.holiday_net,2)).center(12)
        self.pdf_text.append(text)

        self._print_to_screen()

        self.pdf_output.pdf_create(self.pdf_text)
