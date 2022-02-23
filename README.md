# IT-Company-UPP


## Meni

<details>
  <summary> Pokretanje Bonita aplikacije </summary> <br/>
  
Da bi pokrenuli aktivnu verziju projekta, potrebno je da u sekciji **File** izaberete opciju **Import** a potom **BOS archive** i da nadjete **.bos** fajl na vasem racunaru koji predstavlja ovaj projekat. 
  
Kada ste izabrali projekat i importovali ga, verovatno cete imate neke errore. Razlog tome moze da bude vise razloga. Prvo sto bi trebalo uraditi je da odradite "Refresh" projekta 

  ![image](https://user-images.githubusercontent.com/49925421/155209125-8eb0045a-783a-4530-95e0-182b20c7139d.png)

  nakon toga "Deploy"
  
  ![image](https://user-images.githubusercontent.com/49925421/155209347-36088727-29dc-4ab3-8257-bcb8f4c3e3b5.png)

  i nakon toga "Validate"

![image](https://user-images.githubusercontent.com/49925421/155209439-b9bc3e2c-f913-4f7c-b52d-9247711aada9.png)

 Sada bi trebalo da je sve uredu.
  
  
  </details> <br/>
  
  <details>
   <summary> Pokretanje eksterne Django aplikacije </summary> <br/>

  
  Bonita app comunicate with external Django app. You need to start that app locally at port 8000 ie. your beginning URL path of the external app should start as http://127.0.0.1:8000
  eg. we use exactly this URL for payment http://127.0.0.1:8000/payment/payment/
  
  Before you start Django app install all from requirements.txt
  
  To start Django app:
  
  1. cd to /uppPaymentApp
  2. run command "python manage.py runserver"
  
  

 </details> <br/>
 
   <details>
   <summary> Pokretanje Fake SMTP Servera </summary> <br/>
  
- Download link: http://nilhcem.com/FakeSMTP/download.html
  
- Unesite port 2525 i izaberite folder u kom zelite da cuvate mailove
  
- Nakon toga idite na "Server start"
  
![image](https://user-images.githubusercontent.com/49925421/155211546-826b27f6-5413-41e9-9035-658e72fa2770.png)

  
 
 </details> <br/>
 
 
 <details>
   <summary> Flow sa kredencijalima Edukacija </summary> <br/>
  - Lozinka za svakog korisnika je nepromenjena, odnosno bpm.

  *****Slucaj da izaberemo da je kurs online*****
  - Ulogujemo se kao zaposleni <b>marko.hraric</b> i saljemo zahtev za edukaciju.
  - Ulogujemo se kao direktni nadredjeni od marko.hraric, a to je <b>zorica.shraric</b> i vrsimo prihvatanje ili odbijanje zahteva.
  - Ukoliko je odobrena edukacija, ulogujemo se kao sef finansija, <b>vladislav.sfinansic</b>. Vrsimo pregledanje zahteva i izbor kome ce se u opstoj sluzbi proslediti taj zahtev. Moguce opcije su zaposleni u opstoj sluzbi, <b>katja.opstic</b> ili <b>nadja.opstic</b>. Izaberemo npr. katja.opstic.
  - Ulogujemo se kao <b>katja.opstic</b>, vrsimo analizu zahteva i izvrsavanje placanja kursa. Tada se marko.hraric obavestava da je kurs uplacen.
  - Ulogujemo se kao <b>marko.hraric</b> i potvrdimo edukaciju.

   *****Slucaj da izaberemo da je kurs uzivo*****
  - Ulogujemo se kao zaposleni <b>marko.hraric</b> i saljemo zahtev za edukaciju.
  - Ulogujemo se kao direktni nadredjeni od marko.hraric, a to je <b>zorica.shraric</b> i vrsimo prihvatanje ili odbijanje zahteva. Ukoliko smo prihvatili zahtev, navodimo dozvoljeni budzet.
  - Ukoliko je odobrena edukacija, ulogujemo se kao sef finansija, <b>vladislav.sfinansic</b>. Vrsimo pregledanje zahteva i izbor kome ce se u opstoj sluzbi proslediti taj zahtev. Moguce opcije su zaposleni u opstoj sluzbi, <b>katja.opstic</b> ili <b>nadja.opstic</b>. Izaberemo npr. katja.opstic.
  - Ulogujemo se kao agent smestaja, odnosno <b>braco.asmestic</b> i biramo ponudu smestaja.
  - Ulogujemo se kao agent prevoza, odnosno <b>danica.aprevozic</b> i biramo prevoz.

   *Ukoliko su opcije u okviru budzeta*
  - Uogujemo se kao <b>marko.hraric</b> i biramo jednu od njih.
  - Ulogujemo se kao clan opste sluzbe <b>katja.opstic</b> i vrsimo placanje. Zatim se marko.hraric obavestava o izvrsenoj rezervaciji.
  - Ulogujemo se kao <b>marko.hraric</b> i potvrdimo rezervaciju, a potom edukaciju.

   *Ukoliko opcije nisu u okviru budzeta*
  -  Ulogujemo se kao sef zaposlenog, <b>zorica.shraric</b> i vrsimo prihvatanje ili odbijanje.
  -  Ulogujemo se kao clan opste sluzbe <b>katja.opstic</b> i vrsimo placanje. Zatim se marko.hraric obavestava o izvrsenoj rezervaciji.
  -  Ulogujemo se kao <b>marko.hraric</b> i potvrdimo rezervaciju, a potom edukaciju.

  
   </details> <br/>
    <details>
   <summary> Flow sa kredencijalima Oprema  </summary> <br/>
  
 - Ulogujemo se kao zaposleni u HR sluzbi. Kredencijali: username: goran.hraric password: bpm
  
 - Startujemo proces Nabavke, nakon toga dodamo stavke i submitujemo zahtev 
  
 - Ulogujemo se kao direktni nadredjeni tj. sef zaposlenog. Kredencijali: username: zorica.shraric password: bpm
  
 - Direktni nadredjeni ima mogucnost da odobri ili ne odobri zahtev, ukoliko odbije pristize mu proces u kom unosi obrazlozenje i nakon toga se obavestava zaposleni i proces terminira, ukoliko je preliminarno odobrio zahtev on unosi i maksimalni budzet za nabavku.
  
 - Ulogujemo se kao sef sluzbe nabavke. Kredencijali: username: marko.snabavic password: bpm
  
 - Sef sluzbe nabavke pregleda i prosledjuje nabavke. 

 - Ulogujemo se kao zaposleni u sluzbi nabavke. Kredencijali: username: drago.nabavic password: bpm
 
 - Zaposleni u sluzbi nabavke analizira zahtev i odredjuje da li trazena oprema/materijal postoji u lokalnom magacinu u dovoljnoj kolicini, i po potrebi kontaktira i trazi ponude od dobavljaca.
  
 - Ulogujemo se kao dobavljac.  Kredencijali: username: boban.dobavljacic password: bpm
  
 - Dobavljac unosi ponude i jedinicnu cenu za ponude 

 - Kada istekne vreme(5 dana) ulogujemo se kao zaposleni u sluzbi nabavke. Kredencijali: username: drago.nabavic password: bpm (Radi testiranja mozemo smanjiti time boundary na minute)
  
 - Zaposleni u sluzbi nabavke pregleda pristigle ponude i salje sefu nabavke na odobrenje najbolju ponudu.
  
 - Ulogujemo se kao sef sluzbe nabavke. Kredencijali: username: marko.snabavic password: bpm

 - Sef sluzbe nabavke pregleda ponudu i potencijalno je odobrava.
 
 - Ukoliko je ponuda bila skuplja za 15% zatrazena je dodatna saglasnost od sefa zaposlenog koji je trazio opremu. To mozemo proveriti tako sto se ulogujemo se kao direktni nadredjeni tj. sef zaposlenog. Kredencijali: username: zorica.shraric password: bpm
  
 - Ukoliko je ponuda bila za vevi procenat skuplja od ocekivane cene zaposleni i njegov sef su obavesteni da nabavka nece biti obavljena. To mozemo proveriti ulogujemo se kao direktni nadredjeni tj. sef zaposlenog. Kredencijali: username: zorica.shraric password: bpm. I tako sto se ulogujemo se kao zaposleni u HR sluzbi. Kredencijali: username: goran.hraric password: bpm 
  
- Ukoliko je nabavka odobrena pokrece se servis placanja 
  
- Ulogujemo se kao zaposleni u sluzbi nabavke. Kredencijali: username: drago.nabavic password: bpm
  
- Zaposleni u sluzbi nabavke kreira dokument porudzbenice
  
- Ulogujemo se kao sef sluzbe nabavke. Kredencijali: username: marko.snabavic password: bpm
  
- Sef sluzbe nabavke subpotpisuje placanje 
  
- Ulogujemo se kao direktni nadredjeni tj. sef zaposlenog. Kredencijali: username: zorica.shraric password: bpm.
  
- Sef zaposlenog subpotpisuje placanje 

- Ulogujemo se kao zaposleni u HR sluzbi. Kredencijali: username: goran.hraric password: bpm

- Zaposleni prima robu 
  
   </details> <br/>
    <details>
   <summary> Flow sa kredencijalima Posao  </summary> <br/>
  - Lozinka za svakog korisnika je nepromenjena, odnosno bpm.
- Kandidati su: <b>ivana.kandidatic</b>, <b>mima.kandidatic</b>.
- Ulogujemo se kao kandidat, npr. <b>ivana.kandidatic</b> i saljemo zahtev.
- Ulogujemo se kao HR zaposleni, odnosno <b>marko.hraric</b>. Inicijalno se task za analizu i odlucivanje o prihvatanju zahteva za posao dodeljuje marko.hraric. Nakon sto istekne prijava, task se dodeljuje HR zaposlenom, odnosno <b>goran.hraric</b>.
- Moguce je imati uvid u statistiku gde je potrebno potvrditi ukoliko zelimo da je pogledamo. Ako odbijemo, pregled statistike nam nece biti omogucen.

   *Slucaj da je zahtev odbijen*
  - Ulogujemo se kao sef HR sluzbe, <b>zorica.shraric</b> gde mozemo da prihvatimo odbijanje zahteva. Ukoliko prihvatimo odbijanje zahteva, ivana.kandidatic se obavestava da vise nije u krugu za zaposlenje i proces se terminira. Ukoliko se ne prihvati odbijanje, proces se nastavlja.

   *Slucaj da zahtev nije odbijen*
  - Ukoliko je prijava prihvacena, ulogujemo se kao HR sef, <b>zorica.shraric</b>.
  - Prilikom izbora intervjuera, bira se jedan od HR zaposlenih (goran.hraric, marko.hraric), senior (dragan.protsenioric, savo.protsenioric), osoba koja poznaje bar 1 jezi (angela.intervjuic, bergela.sintervjuic).
  - Ulogujemo se kao npr. <b>goran.hraric</b> i izaberemo 3 termina za intervju.
  - Ulogujemo se kao npr. <b>dragan.protsenioric</b> i izaberemo 3 termina za intervju.
  - Ulogujemo se kao npr. <b>angela.intervjuic</b> i izaberemo 3 termina za intervju.

   *Slucaj da kandidat prihvati neki od termina*
  - Ulogujemo se kao kandidat <b>ivana.kandidatic</b> i izaberemo 1 od ponudjenih termina.
  - Ulogujemo se kao <b>goran.hraric</b> i ocenimo kandidata.
  - Ulogujemo se kao <b>dragan.protsenioric</b> i ocenimo kandidata.
  - Ulogujemo se kao <b>angela.intervjuic</b> i ocenimo kandidata.

   *Slucaj da kandidat ne prodje eliminaciju*
  - Proces se zavrsava.

   *Slucaj da kandidat prodje eliminaciju*
  - Ulogujemo kao sef HR sluzbe, <b>zorica.shraric</b> i donosimo konacnu odluku o zaposlenju.

   *Slucaj da kandidat ne prihvati neki od termina*
  - Ukoliko zeli da odustane od prijave, potrebno je da izaberemo 0 u izboru termina i time se obradjivac zahteva, marko.hraric obavestava o odustanku.


   </details> <br/>

  
