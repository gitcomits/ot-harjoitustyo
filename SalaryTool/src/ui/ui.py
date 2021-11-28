
if(__name__ == "__main__"):                                    # suora suoritus 
    from ui_defs  import UIDefs

else:                                                           # index.py suoritus
    from ui.ui_defs  import UIDefs

class UI:

    defs = UIDefs()

    print('\n' * 99)                                            # Clean slate start
    m_div = {}                                                  # monthly division of %
    empty = []                                                  # always empyt
    months = []                                                 # individual months with salary
    months_r = []                                               # range of months  
    l = []                                                      # for printing purposes
    print(" " *3, "To exit just type Exit\n")

    
                                                        # All required input
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


    while(True):
        while(True):                                                # Full or parttime, fulltime 100% salary, part-time some % of monthly salary
            
            control = ["f","p"]                                    # accepted inputs to be verified
            l = ["f - full time","p - part time"]
                
            if(len(months) > 0 or len(months_r) > 0 or len(m_div) > 0):              # already atleast one period filled    
                full_or_part = input("\t\tC - to continue to next step\n Otherwise Full- or part-time (F/P): ")
                if(full_or_part.lower() == "c"):
                    break
            else:
                full_or_part = input("\t\tFull- or part-time (F/P): ")    
            


            if(defs.is_text(full_or_part, control)):                   # valid input
                if(full_or_part.lower() == "p"):                       # part time part salary
                    defs.info_box("Given as integer without '%'-sign",empty)
                    while(True):
                        prop = input("Part time percentage: ")                             # proportional part of the salary
                        if(defs.is_integer(prop) and defs.is_positive(prop)):
                            prop = defs.integer_conversion(prop)
                            
                            
                            defs.is_cero(prop)
                            if(defs.is_under_limit(100, prop)):
                                break
                                #continue
                            else:
                                print(">>> Value under 100 expected <<<")
                            
                        else:
                            print(">>> Positive integer expected <<<")
                                                            
                    #break
                else:
                    prop = 100                                      # full time full salary 
    #                    break


                while(True):                        
                    l = ["C - Continue program", "Input in numbers", "January = 1, February = 2, ..., December = 12",\
                        "Format firstMonth:lastMonth -, 1:11 --> January thrueout November",\
                        "Format oneMonth --> i.e. 3 for May",\
                        "For full year - 1:12"]

                    defs.info_box("Instructions", l)                    
                    m = input("Month or a range of months: ")

                    defs.exit_called(m)                                     # exit called  

                    if(m.lower() == "c"):                                   # continue called
                        if(len(months) > 0 or len(months_r) > 0):           # has anything bee ninserted
                            if(len(m_div) > 0):                             # tarkastukset

                                
                                print("hello workd")
                            
                            m_div = defs.save_months_to_dictionary(m_div, prop, months, months_r)
                            months_r = []
                            months = []
                            print(m_div, " syötetyt arvot prosenttejen kanssa")

                        break

                    month_or_range = defs.one_or_many_months(m)       # 1 = month 2 = range 

        #                    if(defs.one_or_many_months(m) == 1):              # Validation checks for one month input
                    if(month_or_range == 1):              # Validation checks for one month input    
                        if(defs.is_integer(m) and defs.is_positive(m)):
                            m = defs.integer_conversion(m)
                            print(len(months_r), " months r range")
                            if(defs.is_valid_month_number(m)):
                                
                                if(defs.already_exists_in_range(m,months_r) == False):      # if no overlap in range
                                    if(defs.month_is_in_dictionary(m, m_div) == False):     # if month in dicitonary
                                        months = defs.already_exists(months, m)       # individual month already inserted
                                        print(months, "yksi kuukausi syötetty")
                                    else:
                                        print(">>> overlaping months <<<")    

                                else:
                                    print(">>> overlaping months <<<")
                                    print(f"{m} already exists in {months_r}")    
                            
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
                                check = True
                                n1 = validation[0]
                                n2 = validation[1]

                                for mon in months_r:
                                    t = [] 
                                    t.append(list(range(validation[0],validation[1]+1)))              # range to numbers --> inside list
                
                                    for tt in t:
                                        for e in tt:
                                            if(defs.already_exists_in_range(e,months_r)):           # validation if already exists
                                                check = False
                                
                                
                                while(n1 <= n2):                                                    # Any parto of Range in dictionary
                                    if(defs.month_is_in_dictionary(n1, m_div)):
                                        check = False     
                                        break
                                    n1 += 1        
                                
                                if(check):

                                #    print(validation, " what we gots")
                                    months_r.append(validation)
                                    print(months)
                                else:
                                    print(">>> input already in range <<<")



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
            #    break 
            
            
            elif(defs.is_text(full_or_part, control) == False):                 
                defs.exit_called(full_or_part)
                defs.info_box("Expected input:", l)
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

         
