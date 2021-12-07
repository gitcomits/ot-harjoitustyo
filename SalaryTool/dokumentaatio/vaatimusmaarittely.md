# Vaatimusmäärittely

## Käyttötarkoitus

Sovelluksen avulla käyttäjä pystyy laskemaan tulonsa haluamaltaan ajalta. Jos käyttäjä tekee esim. 60% työpäivää
vuoden ensimmäiset 4kk ja sen jälkeen 100% työpäivää elokuulle asti ja loppuvuoden 70% työpäivää laskee ohjelma tämän yhdellä kertaa. 

## Käyttäjät

Ohjelman käyttäminen ei vaadi rekisteröitymistä, kaikille käyttäjille toiminnallisuus on sama. 

## Käyttöliittymä

Käyttöliittymissä tulee olemaan mahdollisuus syöttää seuraavat tiedot: 
	
	- [x] kk palkka						 
	- [x] valinta brutto- / netto tuloille
	  	- [x] mahdollistaa veroprosentin syötön 
	- [x] osa-aikaisuus vai kokoaika
	- [x] aika mille tulot lasketaan ja millä aikaisuudella
	- [x] tulostus summista ja niiden jakautumisesta kk tasolla
	- [x] lomapäivien syöttö
	- [ ] ruudulle tulostus luettavaan muotoon
	- [ ] tallennus tiedostoon txt tai pdf	

## Ensimmäisen version toiminnallisuus 

Käyttäjän syötettyä yllämainitut tiedot lasketaan palkkatulot.
Jos käyttäjä on valinnut syötön nettotuloille vähennetään niistä käyttäjän syöttämä veroprosentti.
Käyttäjä voi myös valita sen onko hän töissä kokoaikaisesti vai osa aikaisesti. Jos osa-aikaisuus on valittu
tulee sille myös aikajakso.
Lomarahat lasketaan kokonaisuudessaan maksettavaksi kesäkuussa.


## Jatkokehitys 

Tulevissa kehtiysversioissa voisi mahdollitaa
	
	- tallennus pdf/txt tiedostoksi
	- lomarahojen mahdollinen jakautuma maksettavaksi valituilla kuukausilla
	- ylitöiden syöttö takautuvasti kuukausi palkan lisäksi
	- ylitöiden arviointi kuukausittain
	- lomarahojen vaihto lomapäiviksi joko kokonaan tai vain osittain     
  
