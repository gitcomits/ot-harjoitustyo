import sys

class UIDefs:

    """Luokka joka tekee tarkastuksia käyttäjän antamiin syötteisiin luokassa UI

    """
    def info_box(self,message:str,c_group:list):
        """Tulostaa ruudulle saamansa viestin, yhdenmukaistaa formatoinnin

        Args:
            message (str): tekstistring joka tulostetaan
            c_group (list): tekstiä lista muodossa, jokainen alkio tulostuu omalle rivilleen
        """

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
        """Tarkistetaan onko saatu syöte numeerinen ja positiivinen

        Args:
            digit (int/float/str): tarkistetaan onko saatu syöte numeerinen 

        Returns:
            Boolean: True/False riippuen onko arvo positiivinen luku vai ei
        """

        if(isinstance(digit, int)): 
            if(int(digit) < 0): 
                return False
        if(isinstance(digit, float)):
            if(digit < 0): 
                return False
        return True

    def is_cero(self, digit):
        """Jos saatu syöte on 0 niin poistutaan ohjelmasta

        Args:
            digit (int): syötetty palkka
        """

        if(isinstance(digit, int)):
            if(int(digit) == 0):
                print("\n" * 99)
                print("Nothing to do with 0 salary")
                sys.exit("Program terminated due to misuse")

    
    def is_over_hundred(self, digit):
        """Tarkistetaan onko saatu syöte yli 100, jos on niin poistutaan ohjelmasta

        Args:
            digit (int): syötetty veroprosentti
        """
        if(int(digit) > 99):
            print("\n" * 99)
            print(f"Nothing to be had with do with {digit}% tax")
            sys.exit("Program terminated due to misuse")


    def is_integer(self, digit):                                       
        """Tarkisteaan onko kuukaudet ja päivät syötetty numeroisina

        Args:
            digit (int): syötetty kuukausi tai päivien lukumäärä

        Returns:
            Boolean: True jos integer, False jos jotain muuta
        """

        try:
            i = int(digit)
            return True
        except:
            return(isinstance(digit,int))    

    def integer_conversion(self,digit):                                 
        """Annettu arvo muunnetaan integeriksi

        Args:
            digit (str): kuukausi tai päivienlukumäärä

        Returns:
            integer: muutetaan string muoto integeriksi
        """

        return int(digit) 

    def is_numeric(self,input_salary):                                   
        """Onko syötetty palkka numeerisessa muodossa

        Args:
            input_salary (string): käyttäjän syöttämä palkkatulo

        Returns:
            Boolean: Ture jos float, False 
        """

        try:
            i = float(input_salary)
            return True 
        except:
            return(input_salary.isnumeric())    
            
    
    def float_conversion(self,to_float):                               
        """Veroprosentti ja kuukausipalkka muunnettaan floatiksi 

        Args:
            to_float (int): [description]

        Returns:
            Float: input converted to float
        """

        converted = round(float(to_float),2)        
        return converted

    def exit_called(self, string:str):                                   
        """Tarkistaa kaikki syötteet jos on haluttu pois ohjelmasta

        Args:
            string (str): Jos syötteenä annettu 'exit' niin ohjelmasta poistutaan
        """

        if(string.lower() == 'exit'):
            print("\n" * 99)
            sys.exit('Termination requested by user')


    def is_text(self, string:str, control_group: list):                   
        """control_group sisältää hyväksytyt arvot, string on käyttäjän syöte
            tarkistetaan onko käyttäjän syöte hyväksytty arvo 

        Args:
            string (str): käyttäjän syöte
            control_group (list): hyväksytyt arvot syötteelle

        Returns:
            Boolean: True jos syöte on oikea, False jos käyttäjän syöte on väärä
        """

        if(string.isalpha()):
            if(control_group.count(string.lower()) != 0):
                return True
            else:
                return False
        else: 
            return False

    def one_or_many_months(self, string:str):                   
        """Onko syötetty yksi kuukausi vai kuukausi joukko
           Virhetilanteessa myös huomautetaan virheestä

        Args:
            string (str): Arvona joko 1 kuukausi tai kuukausi joukko (2:6)

        Returns:
            int: yksittäinen kuukausi saa paluuarvokseen 1, kuukausijoukko 2 ja virhetilanteessa 0
        """
        
        if(string.count(":") != 0):
            if(string.count(":") != 1):
                print(" " *15, "Too many times >>> : <<< ")
                return 0
            return 2
        return 1

    def already_exists(self, l:list, c:int):                      
        """Tarkstaa että käyttäjän syöttämä kuukausi ei ole jo kertaalleen syötetty 

        Args:
            l (list): Ajemmin syötetyt kuukaudet
            c (int): kuukausi joka halutaan lisätä syötetyiden kuukausien joukkoon

        Returns:
            list: Saatu lista joko syötetyllä kuukaudella lisättynä, tai ilman jos kuukausi oli jo olemassa listalla
        """

        if(l.count(c) == 0):
            l.append(c)
        else:
            print(" " * 15, ">>> Month already exists in input <<<")    
        return l     

    def range_has_inserted_month(self, l:list, c:int):                      
        """Tarkstaa että käyttäjän syöttämä kausi ei sisällä yksittäisi kuukausia 

        Args:
            l (list): Ajemmin syötetyt kuukaudet
            c (int): kuukausi joka halutaan lisätä syötetyiden kuukausien joukkoon

        Returns:
            Boolean: True jos listassa, False jos ei aikaisemmin syötetty
        """

        if(l.count(c) == 0):
            return False
        else:
            print(" " * 15, ">>> A month has already been inserted in the range of months <<<")    
        return True     




    def already_exists_in_range(self,m, r):                  
        """Tarkistetaan onko syötetty kuukausi jo olemassa jossakin syötetyssä kuukausi joukossa

        Args:
            m (int): kuukausi jonka käyttäjä on syöttänyt
            r (list): kuukausi joukko johon tarkistus kohdistuu

        Returns:
            Boolean: True jos kuukausi löytyi olemassa olevasta joukosta, False jos kuukautta ei aikaisemmin ole syötetty
        """

        if(len(r) == 0):
            return False
        
        for mm in r:
            if m in range(mm[0],mm[1]+1):
                print("Alert Alert overlap overlap")
                return True

        return False
    
    def is_valid_month_number(self, n):
        """Tarkistetaan että syöte on oikeasti kuukausi rajojen sisäpuolella

        Args:
            n (int): Käyttäjän syöttämä luku, tulisi olla 1-12 välillä

        Returns:
            Boolean: True jos arvo on kuukausien rajoissa (1-12), False jos jotain muuta
        """

        if(n > 0 and n <= 12):
            return True
        return False    

    def is_valid_month_range(self, n1, n2):
        """Tarkistetaan käyttäjän syöttämä kuukausijoukon muodollinen oikeallisuus
        Ensimmäisen kuukauden tulee olla pienempi kuin toisen kuukauden, sekä suurempi kuin 0
        Tosien kuukauden tulee olla pienempi kuin 13 mutta suurempi kuin ensimmäisen kuukauden

        Args:
            n1 (int): joukon ensimmäinen kuukausi
            n2 (int): joukon viimeinen kuukausi

        Returns:
            Boolean: True jos muodollisuus on oikein, False jos väärin
        """

        if(n1 > 0 and n1 < n2 and n2 <= 12):
            return True
        return False    

    def is_under_limit(self,limit:int, digit:int):
        """Raja-arvo tarkastus, käyttäjän syöttämä osa-aikaisuuden oikeallisuus tarkistetaan näin

        Args:
            limit (int): annettu maximiarvo
            digit (int): Syötetty arvo jotta verrataan maximiarvoon

        Returns:
            Boolean: True jos pienempi kuin raja-arvo, False jos sama tai ylittää
        """

        if(limit > digit):
            return True
        return False    

    def save_months_to_dictionary(self,dic,key, m, m_range):
        """Lisätään dictionaryyn jos ei vielä ole
           

        Args:
            dic (dictionary): sisältää kuukaudet jotka käyttäjä on syöttänyt
            key (int): palkan prosentuaalisuus tallennettaville kuukausille
            m (kuukausi):  
            m_range (kuukausi joukko):  

        Returns:
            dictionary: palautetaan dictionary johon tallennettu kuukaudet jos niitä ei vielä ollut 
        """

        t1 = []
        t2 = []
        if(len(m_range) > 0):
            for mon in m_range: 
                t2.append(list(range(mon[0],mon[1]+1)))              
                
                for t in t2:
                    for e in t:
                        t1.append(e)                                      
                t2 = []

        if(len(m) > 0):
            for n in m:
                t1.append(n)     

        if(key in dic):                                        
            print("has skey :", key)

        else:
            t1.sort()
            dic[key] = t1
            return dic


    def month_is_in_dictionary(self, m, dic):
        """Tarkistaa yksittäisen kuukauden olemassa olon dictionarissä

        Args:
            m (int): yksittäinen kuukausi
            dic (dictionary): pitää sisällään kaikki syötetyt kuukaudet

        Returns:
            Boolean: True jos jo dictionarissä, False jos kuukautta ei vielä tallennettu
        """

        for  di in dic.values():
            for o in di:
                if(o == m):
                    print("Already inserted months:")
                    for pair in dic.items():
                        print(pair)
                    return True

        return False        
