from fpdf import FPDF
from datetime import datetime

class PdfOutput:

    def __init__(self):
        self.pdf = FPDF()
        self.line = 0 
        self.save_as = "SalaryCalculation " + str(datetime.now()) + ".pdf"

    def _pdf_create_new(self):
        self.pdf.add_page()
        self.pdf.set_author("Auto Generated By SalaryTools")
        self.pdf.set_title("Salary Calculation")
        self.pdf.set_font("Helvetica", size = 12.5)

    def _pdf_do_insert(self,text):
        self.line += 1
        self.pdf.cell(200, 10, txt = text, ln = self.line, align = "L")

    def _pdf_add_page(self):
        self.pdf.add_page()

    def pdf_create(self, text:list):
        self._pdf_create_new()

        for t in text:
            if t == "NewPage":
                self._pdf_add_page()
                continue
            self._pdf_do_insert(t)
        
        self.pdf.output(self.save_as)

        print("\n\n\nPDF saved to project root flder")
 