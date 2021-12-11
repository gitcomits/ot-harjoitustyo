class OutPut:

    def __init__(self):
        self.holiday_payment = 0
        self.net = 0
        self.gross = 0


    def to_screen(self, new_order):
        print("\n\nPayment information:\n")
        print("Month".center(12), "Gross".center(12), "Net".center(12), "Holiday Gross".center(20), "Holiday net".center(20), "Worktime %".center(10))

        for month in new_order: 
            li = new_order[month].split(":")
            print(li[0].center(12), li[1].center(12),li[2].center(12), li[4].center(20), li[5].center(20),li[3].center(10))
            self.holiday_payment += float(li[5])
            self.gross += float(li[1])
            self.net += float(li[2])
            
        print("\n\nActual payemnt:\n")
        print("Month".center(12), "Net".center(12), "Holiday payment part".center(12))

        for month in new_order: 
            li = new_order[month].split(":")
            if(month == 6):
                tot = float(li[2]) + round(self.holiday_payment,2)
                print(li[0].center(12), str(tot).center(12), str(round(self.holiday_payment,2)).center(12))    
            else:
                if(li[2] != str(0)):
                    print(li[0].center(12), li[2].center(12))


        print("\n\nYearly Summary\n")
        print("Gross".center(12), "Net ex. holiday".center(12), "Holiday payment".center(12))
        print(str(self.gross).center(12), str(self.net).center(12), str(self.holiday_payment).center(12))   

