import sys

class UI:

#    def __init__(self):

#       self.monthly_salary = 0
#       self.tax_percentage = 0        
#       self.full_or_part = 0
#       self.holidays = 0 

    
    def info_box(message:str):

        print()
        print("*" * 20)
        print("*", message, " " * 3, "*")
        print("*" * 20) 



   
    def is_positive(digit):

        if(int(digit) < 0):
            UI.info_box("Input should be a postive number")
            return False
        return True

    def is_cero(digit):
        if(int(digit) == 0):
            print("\n" * 99)
            print("Nothing to do with 0 salary")
            sys.exit("Program terminated due to misuse")

    
    def is_over_hundred(digit):
        if(int(digit) > 99):
            print("\n" * 99)
            print(f"Nothing to be had with do with {digit}% tax")
            sys.exit("Program terminated due to misuse")


    def is_integer(digit):                                       # Is input integer

        try:
            i = int(digit)
            return True
        except:
            print("Input type should be integer")
            return(isinstance(digit,int))    

    def integer_conversion(digit):                                  # Converse string to integer 
        return int(digit) 

    def is_numeric(input_salary):                                   # Is the input valid, integer or float
        try:
            i = float(input_salary)
            return True 
        except:
            print("Input type should be numeric")
            return(input_salary.isnumeric())    
            
    def float_conversion(to_float):                                 # Conversion to float
        converted = round(float(to_float),2)        
        return converted

    def exit_called(string:str):                                    # Exit called by user
        if(string.lower() == 'exit'):
            print("\n" * 99)
            sys.exit('Termination requested by user')

    def is_text(string:str, control_group: list):                   # Comparisson between text input and expected value
        if(string.isalpha()):
            if(control_group.count(string.lower()) != 0):
                return True
            else:
                print("\nExpected input:")
                for c in control_group:
                    print("\t",c)
                return False
        else:
            print("Input type should be alphabetical")
            return False    

    


###############################################################################
#                             Input starts here                               #
###############################################################################
    print('\n' * 99)                                            # Clean slate start
    print("To exit just type Exit")
    print()
      
    while(True):                                                    # All required input
        while(True):                                                # Salary
            
            monthly_salary = input("\t\tMonthly salary: ")              # Monthly salary, should be as stated in the contract

            if(is_numeric(monthly_salary) == False):
                exit_called(monthly_salary)
                
            else:
                if(is_positive(monthly_salary) != True):
                    continue

                is_cero(monthly_salary) 
                monthly_salary = float_conversion(monthly_salary)
                break

            
        while(True):                                                # Tax percentage
            
            tax_percentage = input("\t\tTax percentage (0 for net calculation): ")    
            
            if(is_numeric(tax_percentage) == False):                # Acquired from www.vero.fi/laskurit
                exit_called(tax_percentage)
            
            else: 
                if(is_positive(tax_percentage) != True):
                    continue 
                is_over_hundred(tax_percentage)
                tax_percentage = float_conversion(tax_percentage)
                break


        while(True):                                                # Full or parttime, fulltime 100% salary, part-time
            
            control = ["f","p"]
            full_or_part = input("\t\tFull- or part-time (F/P): ")    
            
            if(is_text(full_or_part, control) == False):                 
                exit_called(full_or_part)

            else:                                                   # Part time logic still missing, which months wich %
                print("input was valid")

                break 

        while(True):                                                # holidays    

            holidays = input("\t\tPaid vacation days: ")                  # Used to calulate holiday payment 

            if(is_integer(holidays)):
                if(is_positive(holidays) != True):
                    continue 
                holidays = integer_conversion(holidays)
                break

            else:
                exit_called(holidays)    


        break        

 
