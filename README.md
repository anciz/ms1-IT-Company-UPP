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
  
  
   </details> <br/>
    <details>
   <summary> Flow sa kredencijalima Posao  </summary> <br/>
   </details> <br/>

  
