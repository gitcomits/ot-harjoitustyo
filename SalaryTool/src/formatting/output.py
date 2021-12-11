from fpdf import FPDF

class OutPut:

    def __init__(self):
        self.holiday_payment = 0
        self.net = 0
        self.gross = 0
        self.pdf = FPDF()
        self.line = 0 


    def _pdf_formating(self):
        self._pdf_new_page()
        self.pdf.set_author("Auto Generated By SalartToos")
        self.pdf.set_title("Salary Calculation")
        self.pdf.set_font("Arial", size = 12.5)

    def _pdf_insert_cell(self, text:str, line:int):
        self.pdf.cell(200, 10, txt = text, ln = line, align = "L")

    def _pdf_do_insert(self,text):
        self.line += 1
        self._pdf_insert_cell(text, self.line)

    def _pdf_new_page(self):
        self.pdf.add_page()

    def to_screen(self, new_order):
        
        self._pdf_formating()
        text = "Payment information:"
        self._pdf_do_insert(text)
        print("\n\n", text,"\n")
        text = "Month".center(12) + "Gross".center(12) +"Net".center(12) + "Holiday Gross".center(20) + "Holiday net".center(20) + "Worktime %".center(10)
        
        self._pdf_do_insert(text)
        
    
    #    print("Month".center(12), "Gross".center(12), "Net".center(12), "Holiday Gross".center(20), "Holiday net".center(20), "Worktime %".center(10))
        print(text)

        for month in new_order: 
            li = new_order[month].split(":")
            text = li[0].center(12) + li[1].center(12) + li[2].center(12) + li[4].center(20) + li[5].center(20) + li[3].center(10)
            self._pdf_do_insert(text)
        #    print(li[0].center(12), li[1].center(12),li[2].center(12), li[4].center(20), li[5].center(20),li[3].center(10))
            print(text)
            self.holiday_payment += float(li[5])
            self.gross += float(li[1])
            self.net += float(li[2])

        self._pdf_new_page()
        text = "Actual payment:" 
        self._pdf_do_insert(text)   
        print("\n\n" + text + "\n")
        text = "Month".center(12) + "Net".center(12) + "Holiday payment part".center(12) 
        self._pdf_do_insert(text)
        print(text)

        for month in new_order: 
            li = new_order[month].split(":")
            if(month == 6):
                tot = float(li[2]) + round(self.holiday_payment,2)
                text = li[0].center(12) + str(tot).center(12) + str(round(self.holiday_payment,2)).center(12)
                self._pdf_do_insert(text)
                print(text) 
            #    print(li[0].center(12), str(tot).center(12), str(round(self.holiday_payment,2)).center(12))    
            else:
                if(li[2] != str(0)):
                    text = li[0].center(12) + li[2].center(12)
                    self._pdf_do_insert(text) 
                #    print(li[0].center(12), li[2].center(12))
                    print(text)

        self._pdf_new_page()
        text = "Yearly Summary:"
        print("\n\n"+ text + "\n")
        self._pdf_do_insert(text)
        text = "Gross".center(12) + "Net ex. holiday".center(12) + "Holiday payment".center(12) 
        self._pdf_do_insert(text)    
        #print("Gross".center(12), "Net ex. holiday".center(12), "Holiday payment".center(12))
        print(text)
        text = str(self.gross).center(12) + str(self.net).center(12) + str(self.holiday_payment).center(12) 
        self._pdf_do_insert(text)
    #    print(str(self.gross).center(12), str(self.net).center(12), str(self.holiday_payment).center(12))   
        print(text)
        
        print("Save as pdf? Enter name for file, without extencion. Empty for default. Type ""No"" for no save")
        save = input("Name for pdf:")
        if(save.lower() != "no"):
            if(len(save) == 0):
                self.pdf.output("SalaryTool.pdf")
                save = "SalaryTool"
            else:
                self.pdf.output(save + ".pdf")
            print(str(save) + ".pdf can be found in the root direcotry!")

