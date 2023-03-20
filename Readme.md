

**Sveučilište Jurja Dobrile u Puli**

  

**Fakultet informatike u Puli**

  

<img  src="https://cdn.discordapp.com/attachments/931310318687236126/1064306501977645076/Unipu-logo-lat.png"  style="height:200px"  />


  

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

<img  src="https://cdn.discordapp.com/attachments/935643353792532571/1080526113413005342/image.png">  <br>

<p>

Naš programski kôd koristi *Pandas* knjižnicu za Python da bismo mogli efikasno učitati podatke iz Excel tablice i dodijeliti ih u Python liste. <br>

Varijabla podaci se pomoću *Pandas* knjižice spaja na Excel datoteku i sprema ih u svoju strukturu podataka *dataframe*. Pozivom **print** funkcije prikazujemo podatke na ekranu nakon čega ih pozivom funkcije **.tolist()** prebacujemo u strukturu podataka python liste u varijablu *podaci_u_listu*. <br>

Komentirana funkcija **print** služi za provjeru prebačenih *dataframe* podataka te za pronalaženje istih u slučaju daljnjeg korištenja liste.

</p><br>

  

<img  src="https://cdn.discordapp.com/attachments/935643353792532571/1080787935672156170/image.png">

<p>

U sam kôd je implementiran jednostavan izbornik kako bi se prikazalo trenutne funkcije implementirane u program te da se rastereti korisnika od postepenog korištenja cijeloga kôda u slučaju da to nije željeno.

</p><br>

  

#### Prvi izbor - Računanje porasta iskorištene poljoprivredne površine

<p>
Prvom opcijom učitavamo podatke koji prikazuju iskorištenu poljoprivrednu površinu 2013. i 2016. godine. Nakon učitavanja proizvoljno zadajemo "kamatnu stopu" rasta u decimalnom obliku **float(input())** funkcijom.<br>
U kôdu se ističu sljedeće varijable:

- **PV** - prošla vrijednost
- **r** - kamatna stopa rasta (proizvoljna varijabla)
- **n** - broj razdoblja
- **FV** - buduća vrijednost

</p>

<img src="https://cdn.discordapp.com/attachments/935643353792532571/1080532927995187310/image.png">

<p>

Buduća predviđena vrijednost se računa formulom: *FV = PV x (1 + r) ^2* nakon čega izračunavamo porast oduzimanjem prošle vrijednosti od buduće vrijednosti.<br>

Na kraju, izračunavamo vjerojatnost povećanja iskorištene poljoprivredne površine dijeljenjem porasta sa prošlom vrijednosti te ispisujemo rezultate na ekran.

</p>
<br>

#### Drugi izbor - predviđanje količine goveda unaprijed tri godine

<p>

Druga opcija preuzima podatke količine goveda u Republici Hrvatskoj 2016. godine te proizvoljno unosimo broj rođenog i uginulog goveda.<br>U ovoj opciji su predstavljene sljedeće varijable:
- **PVgov** - ukupan broj goveda u RH 2016. godine
- **rođeno** - broj rođenog goveda (proizvoljna varijabla)
- **uginulo** - broj uginulog goveda (proizvoljna varijabla)
- **FVgov1** - predviđen broj goveda nakon jedne godine
- **FVgov2** - predviđen broj goveda nakon dvije godine
- **FVgov3** - predviđen broj goveda nakon tri godine

</p>
<img src="https://cdn.discordapp.com/attachments/935643353792532571/1080788723047862332/image.png">
<br>

<p>

Nakon unosa broja rođenog i uginulog goveda predviđanja kroz tri godine računamo formulama *FVgov1 = PVgov + rođeno - uginulo*, *FVgov2 = FVgov1 + rođeno - uginulo* i *FVgov3 = FVgov2 + rođeno - uginulo*  uzastopno te se varijabla **FVgov3** zaokružuje na cijeli broj.<br>Na kraju se na ekranu ispisuje konačna predviđena količina goveda nakon tri godine. 

</p>
<br>

#### Treći izbor - Predviđanje količine uroda nekog trajnog nasada za sljedeću godinu

<p>

Treći izbor nam služi za pregled uroda nekog trajnog nasada za sljedeću godinu.
U ovoj opciji su deklarirane sljedeće varijable:

- **trajni_nasad** - naziv trajnog nasada za koji želimo izračunati predviđanje
- **postotak** - broj našeg predviđanja (u decimalnom obliku)
- **urod** - broj uroda prošle godine (broj izražen u tonama)
- **prinos** - rezultat uroda za iduću godinu

</p>

<img src="https://cdn.discordapp.com/attachments/935643353792532571/1080844323714777198/image.png"><br>

Upisuje se naziv trajnog nasada za koji želimo napraviti predviđanje, zatim se upisuje postotak koji želimo, u glavnom upisujemo onoliko koliko mislim da će se povećati ili smanjiti urod za sljedeću godinu, te na kraju upisujmo koliko je bilo uroda prošle godine (izražen u tonama).

Imamo formulu **Urod * (postotak / 100) ** preko koje računamo naše očekivanje

<p>

</p>
<br>


#### Četvrti izbor - Usporedba poljoprivredne površine za 2013. i 2016 godinu

<p>

Četvrti izbor nam služi za usporedbu poljoprivredne površine za svaku od županija između 2013. i 2016. godine.

U ovoj opciji smo deklarirali slijedeće varijable:

- **odabir** - izbor županije iz liste **zupanije**
- **zemlja** - broj poljoprivredne površine (izražena u km^2)
- **prvooc** - predviđanje rasta ili pada za 2014. godinu
- **drugooc** - predviđanje rasta ili pada za 2015. godinu
- **treceoc** - predviđanje rasta ili pada za 2016. godinu
- **ukupnopost** - ukupni postotak za sva tri postotka za svaku godinu
- **rezul** - ukupni izračun predviđanja poljoprivredne površine

</p>

<img src="https://media.discordapp.net/attachments/935643353792532571/1080844481789698158/image.png?width=611&height=676"><br>

<p>
Imamo listu sa svim županijama, što praktički želimo jer nam treba izbornik za županije. Izaberemo županiju za koju želimo napraviti predviđanje, zatim upisujemo poljoprivrednu površinu zemlje od 2013. godine, pa upisujemo naše predviđanje za 2014, 2015 i 2016. godinu. Program na kraju zbraja predviđanje od sve tri godine u ukupni postotak i onda se pomnoži sa površinom zemlje koju smo upisali.

</p>

----

#### Sigurnosna petlja

<p>

U izbornik programa je ugrađen uvjet koji osigurava da se nepostojeća funkcija <u>ne može odabrati</u>.<br>

</p>

<p>

<img src="https://cdn.discordapp.com/attachments/935643353792532571/1080844539549450381/image.png"><br>

U trenutku kada je nepostojeća funkcija (selekcijski broj van dosega izbornika) odabrana, program nas upozorava na to te nas preskok imenovan **natrag** vraća na vrh programa, odnosno na početak izbornika gdje ponovno odabiremo željenu funkciju.

</p>

---

<br>