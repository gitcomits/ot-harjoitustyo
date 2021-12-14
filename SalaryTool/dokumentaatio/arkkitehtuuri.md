# Arkkitehtuuri

## Ohjelman rakenne

Rakenteeltaan ohjelman sydän on `Format` luokka, jossa käsitellään `UI` luokassa saatu syöte.
Syötteen tarkistukset tapahtuu `UIDefs` luokassa joka varmentaa syötteen muodollisen oikeellisuuden.
`Format` luokka myös kutsuu useampaa eri luokkaa tarvittaviin laskutoimituksiin, `HolidayPayment`, `MonthlyToDaily`, `PartTimeCalculator`, `TaxCalculator`, `YearlyHolidaysToMonthly` 
`MonthlyToDaily` käyttää config.cfg tiedostoa laskennassa.
Tulostus ruudulle tapahtuu luokassa `OutPut` ja pdf tallennus luokassa `PdfOutput`

## Käyttöliittymä

Käyttöliittymä on toteutettu terminaali pohjaisesti. Käyttöruudulla pyydetään käyttäjää antamaan yksi tieto kerrallaan. 
Tiedon formaalisen oikeellisuus tarkistuksen jälkeen ohjelma etenee seuraavaan syötteeseen. 
Syötettäviä tietoja ovat 

- kuukausipalkka
- työssäolo kuukaudet
- osa tai kokoaikaisuus
- osa-aikaisuus määrä (jos osa-aikaisuus valittu)
- veroprosentti
- lomapäivien määrä 

Käyttöliittymä on oma luokkansa, `UI`, jonka muodolliset tarkastukset tehdään luokassa `UIDefs`

## Ohjelma logiikka 

Logiikka on pääosin ratkaistu kutusmalla erinäisiä luokkia `Format` luokasta.
Luokat jotka tekevät laskutoimituksia ovat

- HolidayPayment (laskee lomarahan osuuden)
- MonthlyToDaily (laskee kuukausipalkasta päiväkohtaisen palkan, summaa käytetään lomarahan laskennassa)
- PartTimeCalculator (laskee kuukausipalkan ja osa-aikaisuuden avulla osa-aikaisuus palkan)
- TaxCalculator (vähentää veron kuukausipalkasta ja lomarahoista)
- YearlyHolidaysToMonthly (syötetty vuosiloma jaotetaan palkkaa saaduille kuukausille)

## Tulostus ja tallennus

Luokka `Output` saa luokassa `Format` tehdyt laskennat ja järjestää nämä ruudulle luoettavaan formaattiin.
PDF tallennus tapahtuu luokassa `PdfOutput` mikä saa saman syötteen `OutPut` luokasta kuin ruudulle tulostetun.
PDF tiedostot tallennetaan muodossa `SC + timestamp() + .pdf`. 
Tallennuskansion polku on `/SalaryTool/src/output`.


## Luokkakaavio

![Luokkakaavio](./kuvat/luokkakaavio.png)


## Sekvenssikaavio

Kun ohjelma käynnistetään mainissä ohjelman kontrolli siirtyy Format luokan kautta UI:hin. UI:ssä käyttäjää pyydetään syöttämään 
	- kk palkka
	- onko työaika laatua kokoaika vai osa aika
	- kuukaudet joilta palkkaa tulee (joko osaikaisesti tai kokoaikaisesti)
	- veroprosentti
	- lomapäivät 
	
Jokaisen syötteen kohdalla `UI` kutsuu `UIDefs`iä jossa tarkastetaan syötteen oikeellisuus. 
Kun kaikki tarvittava on syötetty palauttaa `UI` datan `Format` luokalle. 
`Format` luokka formatoi datan muotoon josta se voidaan helpommin tulostaa ruudulle ja/tai tiedostoon,
`Format` luokka myös kutsuu seuraavia luokkia joissa tehdään erinäisiä laskutoimituksia

	- PartTimeCalculator 
	- TaxCalculator
	- HolidayPayment
	- MonthlyToDaily
	- YearlyHolidaysToMonthly
	 
Laskutuoimituksien jälkeen luokka `Output` tulostaa formatoidun datan ruudulle ja kutsuu `PdfOutput` luokkaa 
tallentaen saman datan pdf tiedostona.

![Sekvenssikaavio](./kuvat/sekvenssikaavio.png)


## Parantamiset 

Tekstipohjainen käyttöliittymä tuskin tekee vaikutuksen kehenkään ja tässä kohtaa olisi parantamisen varaa. 
