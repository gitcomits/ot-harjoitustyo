import configparser
import os
import sys
class ConfigChecks:
    """Config.cfg tiedoston arvojen muodollisuus tarkastuksia
    """

    def __init__(self):
        """Luokan konstruktori, paht muuttujassa config tiedoston polku ja tieston nimi
        """

        self.path = os.getcwd() + "/config/config.cfg"
        self.parser = configparser.ConfigParser()
        self.parser.read(self.path)

    def configuration_exists(self,configuration, configuration_name):
        """Tarkistetaan että configuraatio on olemassa

        Args:
            configuration (str): itse configin nimi [config]
            configuration_name (str): muuttujan nimi

        Returns:
            [str]: palautetaan konfiguraatio tiedostosta haluttu arvo
        """

        try:
            days = self.parser.get(configuration, configuration_name)
            return [True, days]
        except:
            print("\n\n")
            print(f"No configuration found for {configuration}/{configuration_name}")
            return [False, ""] 

    def monthly_salary_to_daily(self, days):
        """Tarkistaa config tiedoston MonthlySalaryToDaily arvon muodollisuuden 
        

        Args:
            days (float/int): jakopäivät, tulisi olla joko float tai int

        Returns:
            list: Boolean (True jos hyväksytty arvo, False muuten), int/float/string (laskelmassa käytettävä arvo)
        """

        try:
                i = int(days)
                if(i <= 0): 
                    print(f"Value >>>{i}<<< in config.cfg should be in TES format")    
                    return [False, int(i)]
                return [True, int(i)]    

        except:
                try:
                    i = float(days)
                    if(i <= 0):
                        print(f"Value >>>{i}<<< in config.cfg should be in TES format") 
                        return [False, float(i)]
                    return [True, float(i)]    
                except:
                    print("\n\n")
                    print(f"Value >>>{days}<<< in config.cfg should be a positive integer")
                    return [False, days]
        
    def information_lack(self, configuration_name):
        print(f"Please check the configuration file: {self.path}")
        print("Make sure that the")
        print("                   - path exists")
        print("                   - file exists")
        print(f"                   - file has line for {configuration_name}")
        print("                   - data is in correct format")
        print("Program will terminate, make the required changes in the config.cfg file and then try again.")
        sys.exit()
