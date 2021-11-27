
if(__name__ == "__main__"):                                    # suora suoritus 
    from ui_defs  import UIDefs

else:                                                           # index.py suoritus
    from ui.ui_defs  import UIDefs

class UI:

    defs = UIDefs()

    print('\n' * 99)                                            # Clean slate start
    empty = []                                                  # always empyt
    months = []                                                 # individual months with salary
    months_r = []                                               # range of months  
    l = []                                                      # for printing purposes
    print(" " *3, "To exit just type Exit\n")

    
    while(True):                                                    # All required input
        while(True):                                                # Salary
            
            monthly_salary = input("\t\tMonthly salary: ")              # Monthly salary, should be as stated in the contract

            if(defs.is_numeric(monthly_salary) == False):
                defs.exit_called(monthly_salary)
                defs.info_box("Input type should be numeric",l)
                
            else:
                if(defs.is_positive(monthly_salary) != True):
                    defs.info_box("Input should be a postive number",l)
                    continue

                defs.is_cero(monthly_salary) 
                monthly_salary = defs.float_conversion(monthly_salary)
                break

        while(True):                                                # Full or parttime, fulltime 100% salary, part-time some % of monthly salary
            
            control = ["f","p"]
            l = ["f - full time","p - part time"]
            full_or_part = input("\t\tFull- or part-time (F/P): ")    
            
            if(defs.is_text(full_or_part, control)):
                if(full_or_part.lower() == "p"):                       # part time part salary
                    defs.info_box("Given as integer without '%'-sign",empty)
                    while(True):
                        prop = input("Part time percentage: ")                             # proportional part of the salary
                        if(defs.is_integer(prop) and defs.is_positive(prop)):
                            prop = defs.integer_conversion(prop)
                            
                            
                            defs.is_cero(prop)
                            if(defs.is_under_limit(100, prop)):
                                break
                            else:
                                print(">>> Value under 100 expected <<<")
                            
                        else:
                            print(">>> Positive integer expected <<<")
                        
                        
                                    
                    break
                else:
                    prop = 100                                      # full time full salary 
                    break

            elif(defs.is_text(full_or_part, control) == False):                 
                defs.exit_called(full_or_part)
                defs.info_box("Expected input:", l)

                
                                                         # Part time logic still missing, which months wich %
        while(True):                        
            l = ["C - Continue program", "Input in numbers", "January = 1, February = 2, ..., December = 12",\
                "Format firstMonth:lastMonth -, 1:11 --> January thrueout November",\
                "Format oneMonth --> i.e. 3 for May",\
                "For full year - 1:12"]

            defs.info_box("Instructions", l)                    
            m = input("Month or a range of months: ")

            if(m.lower() == "c"):                             # continue called
                break

            month_or_range = defs.one_or_many_months(m)       # 1 = month 2 = range 

#                    if(defs.one_or_many_months(m) == 1):              # Validation checks for one month input
            if(month_or_range == 1):              # Validation checks for one month input    
                if(defs.is_integer(m) and defs.is_positive(m)):
                    m = defs.integer_conversion(m)
                    
                    if(defs.is_valid_month_number(m)):
                        
                        months = defs.already_exists(months, m)
                        print(months, "yksi kuukausi syötetty")
                    
                    else:
                        print(" "*15, f">>> {m} is not a valid month number <<<")

                else:
                #    defs.info_box(">>> Input should be integer <<<", l)
                    print()
                    print(" " * 15,">>> Input should be a positive integer <<<")    
            
#                    if(defs.one_or_many_months(m) == 2):
            if(month_or_range == 2):                            # validation for range of months
                print(m, " range")                                               
                validation = m.split(":")
                if(defs.is_integer(validation[0]) and defs.is_positive(validation[0]) 
                and defs.is_integer(validation[1]) and defs.is_positive(validation[1])):
                    
                    
                    validation[0] = defs.integer_conversion(validation[0])
                    validation[1] = defs.integer_conversion(validation[1])

                    if(defs.is_valid_month_range(validation[0],validation[1])):     # valid range of months
                        
                        print("valid as a rain")

                    else:
                        print(" " * 15,"<<< inserted range not valid >>>")
                #    if(defs.is_valid_month_number(m)):
                    
                    print(months_r)
                    print(validation)
                    print(months)

                else:
                    print()
                    print(" " * 15,">>> Input should be a valid range of months <<<")    
        #    defs.month_validation(m)

        l = [] 
        break 

    while(True):                                                # Tax percentage
        
        tax_percentage = input("\t\tTax percentage (0 for net calculation): ")    
        
        if(defs.is_numeric(tax_percentage) == False):           # Acquired from www.vero.fi/laskurit
            defs.exit_called(tax_percentage)
            defs.info_box("Input type should be numeric",l)
        
        else: 
            if(defs.is_positive(tax_percentage) != True):
                defs.info_box("Input should be a postive number",l)
                continue 
            defs.is_over_hundred(tax_percentage)
            tax_percentage = defs.float_conversion(tax_percentage)
            break


        while(True):                                                       # holidays    

            holidays = input("\t\tPaid vacation days: ")                  # Used to calulate holiday payment 

            if(defs.is_integer(holidays)):
                if(defs.is_positive(holidays) != True):
                    defs.info_box("Input should be a postive number", l)
                    continue 
                holidays = defs.integer_conversion(holidays)
                break

            else:
                defs.exit_called(holidays)    
                defs.info_box("Input type should be integer",l)

        break        