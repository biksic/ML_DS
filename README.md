# ML_DS


## Uvod

Ovaj projekt sastoji se od tri zadatka koja će vam pomoći da pokažete svoje vještine u analizi satelitskih snimki, obradi prostornih podataka i strojnom učenju. Svaki zadatak fokusira se na različite aspekte rada s podacima i modelima.

## Zadatak 1

Izradite Python skriptu za analizu satelitske snimke Sentinel-2 L2A. Skripta treba izračunati indekse poput NDVI i NDMI, spremiti ih kao .tiff datoteke i prikazati njihove prosječne vrijednosti. Također, prikažite broj bandova u snimci. Opcionalno, možete učitati skriptu na svoj git profil.

**Rješenje s komentarima se nalazi u skripti `zadatak1.py`.**

## Zadatak 2

Razvijte Python skriptu za analizu podataka preuzetih s API-a ili lokalno u .geojson formatu. Skripta treba prikazati ukupan broj zapisa i broj zapisa s određenim tipom objekta te spremiti te objekte u novu .geojson datoteku. Opcionalno, možete učitati skriptu na svoj git profil.

**Rješenje s komentarima se nalazi u skripti `zadatak2.py`.**

## Zadatak 3

Trenirajte ML model koristeći podatke iz .csv datoteke uključene u .zip arhivu. Podijelite podatke u trening, testiranje i validaciju, te prikažite performanse modela kroz statistike kao što su matrica konfuzije. Razvijajte skriptu kao Python skriptu ili Jupyter notebook, a model možete spremiti kao .joblib datoteku ako želite. Ovdje cijenimo vašu kreativnost u odabiru i primjeni modela.

**Rješenje s komentarima se nalazi u Jupyter notebook datoteci `zadatak3.ipynb`.**

**Napomena:** Iako nije bilo zahtjevano čišćenje podataka, primijetio sam da se neki podaci dupliciraju, pa sam ih uklonio. Također, zbog neuravnoteženosti klasa u podacima, koristio sam oversampling i undersampling kako bih poboljšao ravnotežu klasa.
