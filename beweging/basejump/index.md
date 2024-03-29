# Basejump

Schrijf een programma waarin de val wordt doorgerekend van een basejumper die van de top van de Burj Khalifa in Dubai (828m) naar beneden springt. Neem hierbij aan dat de basejumper 72 kilo weegt.


## Achtergrond

In de vorige opgave is de luchtwrijving verwaarloosd waardoor je ook met behulp van de natuurkunde van de middelbare school de antwoorden kon controleren. We gaan nu een stuk realisme toevoegen: luchtwrijving.

De luchtweerstand die een vallend voorwerp ondervindt is evenredig met het kwadraat van de snelheid:

$$F = \xi v^2$$, met $$ \xi = 0.24$$

Hoewel de luchtweerstand ook afhankelijkheid is van de oppervlakte en massa van het object en de dichtheid van de lucht zullen we in deze opdracht alleen het effect van de snelheid bestuderen. De wrijving betekent dat er een snelheid is waarbij de zwaartekracht en de wrijving elkaar in evenwicht houden. Deze maximum snelheid die een parachutespringer kan bereiken, ongeveer 196km/u, wordt de [terminale snelheid](https://en.wikipedia.org/wiki/Terminal_velocity) genoemd.

![](Freefall.png)

Zoals altijd heb je ook hier mensen die het [randje opzoeken](https://en.wikipedia.org/wiki/Speed_skydiving). Omdat hij zijn sprong maakte in een gebied waar de luchtdruk enorm laag was is het record met 1357.64 km/u veilig in handen van Felix Baumgartner.


## Specificatie

Maak een bestand `basejump.py` met daarin een functie `basejump()`. Volg dezelfde strategie als in de vorige opdracht met de appel, maar neem nu ook de luchtweerstand mee zoals gegeven in bovenstaande formule.

### Grafieken

De volgende grafieken moet je laten **aftekenen** bij je assistent. Als in een grafiek natuurkundige *grootheden* worden weergegeven, moeten die met hun bijbehorende (SI-)*eenheden* worden aangegeven in een *as-label*. Als bijvoorbeeld snelheid in kilometer per uur wordt weergegeven, zet je bij de correct as *v (km/u)* of *snelheid (km/u)*. Let op de vorm: *grootheid (eenheid)*.

1. Plot een grafiek van de snelheid als functie van de tijd.

    Test je programma door net te doen of de toren 2000 meter hoog is en te kijken of je inderdaad vindt dat de terminale snelheid ongeveer 196km/u is.

2. Plot een grafiek van de hoogte als functie van de tijd. 

    Teken twee lijnen in dezelfde figuur: in groen/blauw de situatie als we de luchtweerstand wel/niet verwaarlozen. Voeg ook een legenda toe (zoek eventueel online hoe dit moet).

### Simulatie

Print de antwoorden op de volgende vragen. Denk er weer aan om precies zijn in je antwoord en alleen de gevraagde waarden te printen op hun eigen regel.

De basejumper is eerst in vrije val, maar op 100 meter van het oppervlak moet deze de parachute opengooien.

- Hoeveel tijd (seconden) heeft de jumper vanaf de afsprong tot dat moment, als we de luchtweerstand buiten beschouwing laten?

- Hoeveel *langer* (seconden) heeft de base-jumper om te genieten van de vrije val dankzij de luchtweerstand?

## Testen

	checkpy basejump
