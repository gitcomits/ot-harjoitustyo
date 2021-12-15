import calendar

if(__name__ == "__main__"):
    from ui_defs  import UIDefs

else:
    from ui.ui_defs  import UIDefs

class UI:
    """Luokan funktio on tallentaa käyttäjän antamat syötteet, tarkistukset tehdään UIDefs luokassa
    """

    defs = UIDefs()

    print('\n' * 99)                                            
    m_div = {}                                                  
    m_prop = {}
    empty = []                                                  
    months = []                                                 
    months_r = []                                                 
    l = []                                                      
    m = ""

    print(" " *3, "To exit just type Exit\n")    
                                                        
    while(True):
        
        monthly_salary = input("\t\tMonthly salary: ")

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
        while(True):
            
            control = ["f","p"]
            l = ["f - full time","p - part time"]

            if(len(months) > 0 or len(months_r) > 0 or len(m_div) > 0 and (m.lower != "c" or m.lower == "" )):    
                full_or_part = input("\t\tC - to continue to next step\n Otherwise Full- or part-time (F/P): ")
                defs.exit_called(full_or_part)
                if(full_or_part.lower() == "c"):
                    break
            else:
                if(m.lower == "c"):
                    break
                else:
                    full_or_part = input("\t\tFull- or part-time (F/P): ")    
                    defs.exit_called(full_or_part)
            
            if(defs.is_text(full_or_part, control)):
                if(full_or_part.lower() == "p"):
                    defs.exit_called(full_or_part)
                    defs.info_box("Given as integer without '%'-sign",empty)
                    while(True):
                    
                        prop = input("Part time percentage: ")

                        defs.exit_called(prop)
                        if(defs.is_integer(prop) and defs.is_positive(prop)):
                            prop = defs.integer_conversion(prop)                            
                            defs.is_cero(prop)
                            if(defs.is_under_limit(100, prop)):
                                break
                            else:
                                print(">>> Value under 100 expected <<<")
                            
                        else:
                            print(">>> Positive integer expected <<<")
                else:
                    prop = 100
    
                while(True):                        
                    l = ["C - Continue program", "Input in numbers", "January = 1, February = 2, ..., December = 12",\
                        "Format firstMonth:lastMonth -, 1:11 --> January thrueout November",\
                        "Format oneMonth --> i.e. 3 for May",\
                        "For full year - 1:12"]

                    defs.info_box("Instructions", l)                    
                    m = input("Month or a range of months: ")

                    defs.exit_called(m)

                    if(m.lower() == "c"):
    

                        if(len(months) > 0 or len(months_r) > 0):
                            if(len(m_div) > 0):
                                
                                pass

                            m_div = defs.save_months_to_dictionary(m_div, prop, months, months_r)
                            months_r = []
                            months = []
    
                        break

                    month_or_range = defs.one_or_many_months(m)

                    if(month_or_range == 1):
                        if(defs.is_integer(m) and defs.is_positive(m)):
                            m = defs.integer_conversion(m)
                            if(defs.is_valid_month_number(m)):
                                if(defs.already_exists_in_range(m,months_r) == False):
                                    if(defs.month_is_in_dictionary(m, m_div) == False):
                                        months = defs.already_exists(months, m)
                                    else:
                                        print(">>> overlaping months <<<")    
                                else:
                                    print(">>> overlaping months <<<")
                                    print(f"Month {m} ({calendar.month_abbr[m]}) already exists in the range of months >> {months_r}")    
                            else:
                                print(" "*15, f">>> {m} is not a valid month number <<<")
                        else:
                            print(" " * 15,">>> Input should be a positive integer <<<")    
                    

                    if(month_or_range == 2):
                        validation = m.split(":")
                        if(defs.is_integer(validation[0]) and defs.is_positive(validation[0]) 
                        and defs.is_integer(validation[1]) and defs.is_positive(validation[1])):
                            validation[0] = defs.integer_conversion(validation[0])
                            validation[1] = defs.integer_conversion(validation[1])
                            if(defs.is_valid_month_range(validation[0],validation[1])):
                                check = True
                                n1 = validation[0]
                                n2 = validation[1]
                                if(len(months) != 0):        
                                    while(n1 <= n2):
                                        if (defs.range_has_inserted_month(months,n1)):
                                            check = False
                                            break
                                        n1 += 1 
                                for mon in months_r:
                                    t = [] 
                                    t.append(list(range(validation[0],validation[1]+1)))
                                    for tt in t:
                                        for e in tt:
                                            if(defs.already_exists_in_range(e,months_r)):
                                                check = False
                                while(n1 <= n2):
                                    if(defs.month_is_in_dictionary(n1, m_div)):
                                        check = False     
                                        break
                                    n1 += 1        
                                if(check):
                                    months_r.append(validation)

                                else:

                                    print(">>> input already in range <<<")

                            else:
                                print(" " * 15,"<<< inserted range not valid >>>") 
    
                        else:
                            print(" " * 15,">>> Input should be a valid range of months <<<")    
    
                l = [] 
                        
            elif(defs.is_text(full_or_part, control) == False):                 
                defs.exit_called(full_or_part)
                defs.info_box("Expected input:", l)
        break
        
    while(True):                                     
        l = []
        tax_percentage = input("\t\tTax percentage: ")    
        
        if(defs.is_numeric(tax_percentage) == False):
            defs.exit_called(tax_percentage)
            defs.info_box("Input type should be numeric",l)
        
        else: 
            tax_percentage = defs.float_conversion(tax_percentage)
            if(defs.is_positive(tax_percentage) != True):
                defs.info_box("Input should be a postive number",l)
                continue 
            defs.is_over_hundred(tax_percentage)
            tax_percentage = defs.float_conversion(tax_percentage)
            break

    while(True):    

        holidays = input("\t\tPaid vacation days: ")

        if(defs.is_integer(holidays)):
            if(defs.is_positive(holidays) != True):
                defs.info_box("Input should be a postive number", l)
                continue 
            holidays = defs.integer_conversion(holidays)
            break

        else:
            defs.exit_called(holidays)    
            defs.info_box("Input type should be integer",l)
