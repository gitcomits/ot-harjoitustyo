import sys

class UIDefs:

    def info_box(self,message:str,c_group:list):

        m = 80                      # lengt of start
        e = 15                      # empty spaces

        print()
        print(" " * e, "*" * m)
        print(" " * e, "*", message.center(m-4),"*")

        if(len(c_group) > 0):
            for c in c_group:
                print(" " * e, "*", c.center(m-4),"*")

        print(" " * e, "*" * m)
    
    def is_positive(self,digit):

        if(int(digit) < 0):
            return False
        return True

    def is_cero(self, digit):
        if(int(digit) == 0):
            print("\n" * 99)
            print("Nothing to do with 0 salary")
            sys.exit("Program terminated due to misuse")

    
    def is_over_hundred(self, digit):
        if(int(digit) > 99):
            print("\n" * 99)
            print(f"Nothing to be had with do with {digit}% tax")
            sys.exit("Program terminated due to misuse")


    def is_integer(self, digit):                                       # Is input integer

        try:
            i = int(digit)
            return True
        except:
            return(isinstance(digit,int))    

    def integer_conversion(self,digit):                                  # Converse string to integer 
        return int(digit) 

    def is_numeric(self,input_salary):                                   # Is the input valid, integer or float
        try:
            i = float(input_salary)
            return True 
        except:
            return(input_salary.isnumeric())    
            
    def float_conversion(self,to_float):                                 # Conversion to float
        converted = round(float(to_float),2)        
        return converted

    def exit_called(self, string:str):                                    # Exit called by user
        if(string.lower() == 'exit'):
            print("\n" * 99)
            sys.exit('Termination requested by user')

    def is_text(self, string:str, control_group: list):                   # Comparisson between text input and expected value
        if(string.isalpha()):
            if(control_group.count(string.lower()) != 0):
                return True
            else:
                return False
        else:
    #        print("Input type should be alphabetical")
            return False

    def one_or_many_months(self, string:str):                   # is input one month or a range of months
         
        if(string.count(":") != 0):
            if(string.count(":") != 1):
                print(" " *15, "Too many times >>> : <<< ")
                return 0
            return 2
        return 1

    def already_exists(self, l:list, c:int):                      # individual month
        
        if(l.count(c) == 0):
            l.append(c)
        else:
            print(" " * 15, ">>> Month already exists in input <<<")    
        return l     

    def is_valid_month_number(self, n):
        if(n > 0 and n <= 12):
            return True
        return False    

    def is_valid_month_range(self, n1, n2):
        if(n1 > 0 and n1 < n2 and n2 <= 12):
            return True
        return False    

    def is_under_limit(self,limit:int, digit:int):
        if(limit > digit ):
            return True
        return False    


