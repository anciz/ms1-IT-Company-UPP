# IT-Company-UPP


## Meni

<details>
  <summary> Kontrolisanje verzija </summary> <br/>
  
Da bi preuzeli aktivnu verziju projekta, potrebno je da u sekciji **File** izaberete opciju **Import** a potom **BOS archive** i da nadjete **.bos** fajl na vasem racunaru koji predstavlja ovaj projekat. 
  
Kada ste izabrali projekat i importovali ga, verovatno cete imate neke errore. Razlog tome moze da bude vise razloga. Prvo sto bi trebalo uraditi je da u sekciji **Development** izabere opciju **Business Data Model** a onda i **Define**. Tada se otvara deo sa modelima nase baze, prvo je potrebno to deployovati. Naravno, nakog toga probajte kompletno aplikaciju da deplojujete. Nakon toga i da refresujete projekat. Takodje Process diagrams u sebi zadrzi procese, ako neki od njih ima error, desni klik i validate. Sada bi trebalo da je sve uredu.
  
  
  </details> <br/>
  
  
  ## FYI
  
  Bonita app comunicate with external Django app. You need to start that app locally at port 8000 ie. your beginning URL path of the external app should start as http://127.0.0.1:8000
  
eg. we use exactly this URL for payment http://127.0.0.1:8000/payment/payment/
