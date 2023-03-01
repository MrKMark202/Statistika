
Sveučilište Jurja Dobrile u Puli

Fakultet informatike u Puli

<img src="https://cdn.discordapp.com/attachments/931310318687236126/1064306501977645076/Unipu-logo-lat.png" style="height:200px" />

Dokumentacija uz projektni zadatak

----

### Programska obrada statistike poljoprivrede u Republici Hrvatskoj
Izradili: Marko Katalinić, Filippo Bubić

Studijski smjer: Informatika

Kolegij: Statistika

<b> Mentor: mr. sc. Darko Brborović </b> 

<br>
<br>

## Uvod
<p>Ova dokumentacija služi za pojašnjenje programskog kôda projektnog zadatka koji obrađuje statističke podatke poljoprivrede u Republici Hrvatskoj. <br>
U projektu smo se služili znanjem iz kolegija Statistika preddiplomskog sveučilišnog smjera Informatike da bi razvili formule za obradu podataka te iste pretvorili u programski kod. </p>

## Obrada kôda
<img src="https://cdn.discordapp.com/attachments/935643353792532571/1080526113413005342/image.png"> <br>
<p>
Naš programski kôd koristi *Pandas* knjižnicu za Python da bismo mogli efikasno učitati podatke iz Excel tablice i dodjeliti ih u Python liste. <br>
Varijabla podaci se pomoću *Pandas* knjižice spaja na Excel datoteku i sprema ih u svoju strukturu podataka *dataframe*. Pozivom **print** funkcije prikazujemo podatke na ekranu nakon čega ih pozivom funkcije **.tolist()** prebacujemo u strukturu podataka python liste u varijablu *podaci_u_listu*. <br>
Komentirana funkcija **print** služi za provjeru prebačenih *dataframe* podataka te za pronalaženje istih u slučaju daljnjeg korištenja liste.
</p><br>

<img src="https://cdn.discordapp.com/attachments/935643353792532571/1080530375559876649/image.png">
<p>
U sam kôd je implementiran jednostavan izbornik kako bi se prikazalo trenutne funkcije implementirane u program te da se rastereti korisnika od postepenog korištenja cijeloga kôda u slučaju da to nije željeno.
</p><br>

#### Prvi izbor - Računanje porasta iskorištene poljoprivredne površine
<p>
Prvom opcijom učitavamo podatke koji prikazuju iskorištenu poljoprivrednu površinu 2013. i 2016. godine. Nakon učitavanja proizvoljno zadajemo "kamatnu stopu" rasta u decimalnom obliku **float(input())** funkcijom. U kôdu se ističu sljedeće varijable:<br>

 - **PV** - prošla vrijednost
 - **r** - kamatna stopa rasta
 - **n** - broj razdoblja
 - **FV** - buduća vrijednost
</p>
<img src="https://cdn.discordapp.com/attachments/935643353792532571/1080532927995187310/image.png">
<p>
Buduća predviđena vrijednost se računa formulom: *FV = PV x (1 + r) ^2* nakon čega izračunavamo porast oduzimanjem prošle vrijednosti od buduće vrijednosti.<br>
Na kraju, izračunavamo vjerojatnost povećanja iskorištene poljoprivredne površine dijeljenjem porasta sa prošlom vrijednosti te ispisujemo rezultate na ekran.
</p>