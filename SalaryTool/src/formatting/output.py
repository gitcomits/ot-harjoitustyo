
from formatting.pdf_output import PdfOutput

class OutPut:

    def __init__(self):
        self.holiday_net = 0
        self.holiday_gross = 0
        self.net = 0
        self.gross = 0
        self.pdf_text = [] 
        self.pdf_output = PdfOutput()
        
    def _print_to_screen(self):
        print("\n\n")
        for t in self.pdf_text:
            if t == "NewPage":
                print("\n")
                continue
            print(t)
            if(t[-1] == ":"):
                print("\n")        
        



    def to_screen(self, new_order):
        text = " Payment information:"
        self.pdf_text.append(text)
        text = "Month".center(12) + "Gross".center(12) +"Net".center(12) + "Holiday Gross".center(20) + "Holiday net".center(20) + "Worktime %".center(10)
        self.pdf_text.append(text)

        for month in new_order: 
            li = new_order[month].split(":")
            text = li[0].center(12) + li[1].center(12) + li[2].center(12) + li[4].center(20) + li[5].center(20) + li[3].center(10)
            self.pdf_text.append(text)
            self.holiday_net += float(li[5])
            self.holiday_gross += float(li[4])
            self.gross += float(li[1])
            self.net += float(li[2])
            

   
        self.pdf_text.append("NewPage")
        text = " Actual payment:"
        self.pdf_text.append(text) 
   
        text = "Month".center(12) + "Net".center(12) + "HP".center(12) 
        self.pdf_text.append(text)

        for month in new_order: 
            li = new_order[month].split(":")
            if(month == 6):
                tot = float(li[2]) + round(self.holiday_net,2)
                text = li[0].center(12) + str(round(tot,2)).center(12) + str(round(self.holiday_net,2)).center(12)
                
                self.pdf_text.append(text)
                
            else:
                if(li[2] != str(0)):
                    text = li[0].center(12) + li[2].center(12)
                    self.pdf_text.append(text)

        self.pdf_text.append("NewPage")
        text = " Yearly Summary:"
        self.pdf_text.append(text)
        
        text = "Gross".center(12) + "Net".center(12) + "HP".center(12)
        self.pdf_text.append(text) 
        year_gross = self.gross + self.holiday_gross
        year_net = self.net + self.holiday_net
        text = str(round(year_gross,2)).center(12) + str(round(year_net,2)).center(12) + str(round(self.holiday_net,2)).center(12) 
        self.pdf_text.append(text)

        self._print_to_screen()

        self.pdf_output.pdf_create(self.pdf_text)    
    