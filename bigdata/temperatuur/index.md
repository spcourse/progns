# Temperatuur

![](../assets/KaartNederlandKlein.png){:.inline}

Laten we een steentje bijdragen aan de klimaatdiscussie en data analyseren die  door de ECA (European Climate Assessment) [beschikbaar](https://www.ecad.eu/dailydata/predefinedseries.php) wordt gemaakt in grote data-bestanden. We beperken ons tot data die de maximum- en minimumtemperatuur beschrijft voor elke dag in De Bilt sinds 1901.

Bestanden: 

- [DeBiltTempMinSUMMER2023.txt](../data/DeBiltTempMinSUMMER2023.txt)
- [DeBiltTempMaxSUMMER2023.txt](../data/DeBiltTempMaxSUMMER2023.txt)

Download de bestanden, open ze en lees bovenin hoe de data gecodeerd is. We zien dat de maximum(minimum)-temperatuur op 1 januari 1901 -3.1(-6.8) graden Celsius was.

> Let op! De data-bestanden bevatten ook allerlei uitleg. De bedoeling is dat je deze laat staan in het bestand. Je Python-programma moet zo geschreven zijn dat je deze regels netjes overslaat bij het verwerken!

Schrijf een programma **temperatuur.py** die het bestand regel voor regel inleest
en beantwoord de volgende vragen.

### Opdracht 1: Extreme temperaturen

Wat waren de hoogste en laagste temperatuur die in De Bilt zijn gemeten sinds het begin van de 20e eeuw? Op welke dagen was dat? Zorg dat je programma de datum netjes op het scherm print. Zeg dus niet: 

     Max 34.5 op 19670513

maar

     De hoogste temperatuur was 34.5 graden Celsius en werd gemeten op 13 mei 1967.

Tip: maak een aparte functie die een getal als `19670513` kan omzetten naar een goed leesbare beschrijving als `13 mei 1967`. Je mag de datum ook in het Engels geven, maar let op dat maanden dan met hoofdletter worden geschreven.

### Opdracht 2: De kleine ijstijd

Wat is de langste periode dat het aaneengesloten heeft gevroren (**max**imumtemperatuur onder 0°C)? Print op één regel het aantal dagen en de datum van de laatste dag van deze periode.

### Opdracht 3: Zomerse en tropische dagen

We spreken van een zomerse dag als de maximumtemperatuur meer dan 25 graden Celsius was. Op een tropische dag is het in De Bilt zelfs 30 graden. Maak een grafiek waarin voor elk jaar zowel het aantal zomerse als het aantal tropische dagen weergegeven wordt. Zorg dat duidelijk is wat de data betekent: vergeet niet de juiste assenlabels en een legenda toe te voegen.

### Opdracht 4: Eerste hittegolf

We spreken in Nederland van een hittegolf als de maximumtemperatuur ten minste vijf dagen achtereen minstens 25.0°C was (zomerse dagen) waarvan ten minste op drie dagen 30.0°C of meer (tropische dagen). Print het *eerste* jaartal uit de dataset waarin er sprake was van een hittegolf volgens deze regels.

### Nette code en nette uitvoer

Zorg dat de code van alle opdrachten in een functie of in functies staat. Gebruik geen globale variabelen (vraag indien nodig wat dit is)!

Je ziet hierboven dat je een aantal dingen moet uitprinten en één grafiek maken. Zorg dat de gevraagde informatie op losse regels wordt uitgeprint, in de juiste volgorde.
