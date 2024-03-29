import os
from datetime import datetime
from fpdf import FPDF

class PdfOutput:
    """Tallennus pdf muotoon

        Attributes:

        """


    def __init__(self):
        """Luokan konstruktori, määritellään muuttujat

        Args:

        """

        self.pdf = FPDF()
        self.line = 0
        path = os.getcwd() + "/src/output/"
        name = "SC" + str(datetime.now()) + ".pdf"
        self.save_as = path + name

    def _pdf_create_new(self):
        """Pohjustetaan tyhjä pdf tiedosto pohjaksi tallenteelle
        """

        self.pdf.add_page()
        self.pdf.set_author("Auto Generated By SalaryTools")
        self.pdf.set_title("Salary Calculation")
        self.pdf.set_font("Helvetica", size = 12.5)

    def _pdf_do_insert(self,text):
        """Kirjoittaa pdf:ään rivi riviltä listan sisältämät alkiot

        Args:
            text (list): Listan jokainen alkio tulostuu omalle rivilleen
        """

        self.line += 1
        self.pdf.cell(200, 10, txt = text, ln = self.line, align = "L")

    def _pdf_add_page(self):
        """Uusi sivu pdf:n
        """

        self.pdf.add_page()

    def pdf_create(self, text:list):
        """Kutsutaan Output luokasta, kutsuu muita luokan funktioita jotka
         kirjoittavat text:listan pdf:n tallentaa pdf käyttäjän koneelle

        Args:
            text (list): sisältää Output luokan muokkaman datan
        """

        self._pdf_create_new()

        for t_t in text:
            if t_t == "NewPage":
                self._pdf_add_page()
                continue
            if t_t == "NewLines":
                continue
            self._pdf_do_insert(t_t)

        self.pdf.output(self.save_as)

        print("\n\n\nPDF saved as " + self.save_as)
        print("\n")
