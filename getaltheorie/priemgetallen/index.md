# Priemgetallen

Implementeer een programma dat op verzoek het $$N$$-de priemgetal genereert.

    Naar het hoeveelste priemgetal bent u op zoek? 1000
    7919

## Achtergrond

Zoals gezegd is een computer geweldig in het snel uitvoeren van een heleboel "domme" stappen. Een voorbeeld waar een computer zó veel effectiever is dan een enkele persoon, is het uitrekenen van priemgetallen. De definitie van een priemgetal is niet al te ingewikkeld. Maar bepalen hoeveel delers een willekeurig getal heeft kan ontzettend veel tijd kosten. Python to the rescue!

## Specificatie

- Vraag de gebruiker om de rangorde van het priemgetal (het hoeveelste) in te voeren. Dit moet natuurlijk een geheel en positief getal zijn.

- Als de gebruiker een rangorde invult die niet toegestaan is, dan vraag je de gebruiker opnieuw naar de rangorde. En herhalen tot de gebruiker een geldige rangorde invult. Omdat je niet weet hoe vaak dat zal zijn, moet het een `while`-loop worden!

- Ofschoon je moet controleren of het om een positief getal gaat, mag je er wel vanuit gaan dat een geheel getal wordt ingevoerd (en geen kommagetal). Dat hoef je dus niet te controleren.

- Zodra de rangorde bekend is, bereken het juiste priemgetal en rapporteer dit terug aan de gebruiker.

- Zorg dat het programma niets anders uitvoert dan dit getal, zoals in het voorbeeld bovenaan de opdracht!

- Het programma moet drie functies met de gegeven namen bevatten die alle stappen zoals onder beschreven uitvoeren.

## Probleemanalyse

Neem vóór je gaat programmeren eerst een paar minuten om met **pen en papier** te schetsen hoe je zelf het probleem aan zou pakken, hoe je het probleem kunt opdelen in overzichtelijke stappen. De specificatie hierboven geeft al wat hints daarvoor!

Bij deze opdracht nemen we je aan de hand door een aantal stappen te geven om te doorlopen tijdens het ontwikkelen van de juiste oplossing.

## Stap 1: priem-check

Een belangrijk deel van de omschrijving hierboven is dat het om priemgetallen gaat. Wat is een priemgetal? Dat moeten we in Python zien uit te drukken.

Definieer dus eerst een functie `priem_of_niet()` met één argument die van een bepaald getal, het argument, onderzoekt of het een priemgetal is of niet. De functie moet `True`/`False` returnen als het argument wel/niet een priemgetal is.

Begin zo simpel mogelijk. Gebruik een `for`-loop en `%` (modulo) om te bepalen hoeveel getallen een deler zijn van het argument. Als je dit bijhoudt in de loop (tellen!), kun je na afloop van de loop bepalen of het getal een priemgetal is of niet. Als rekenen met `%` nog wat nieuw voor je is, kijk dan nog eens [hier](/python/basiselementen) bij het stukje over operatoren en [hier](/python/functies) bij het stukje over even getallen aan het eind.

## Stap 2: check een hele partij getallen

We gaan een stap verder. We kunnen bovenstaand stukje code nu hergebruiken (i.e. de functie aanroepen) en voor *elk* getal onder de 100 bepalen of het een priemgetal is of niet.

Definieer een functie `alle_priem_tot()` met één argument, `N`. Maak in deze functie een `for`-loop om alle getallen onder de `N` langs te loopen en bepaal voor elk van deze "kandidaat-priemgetallen" of het wel of niet een priemgetal is door de functie `priem_of_niet` aan te roepen.

Schrijf dus bovenstaande procedure en maak deze goed werkend. De functie hoeft vervolgens niets te returnen, maar moet wel ieder gevonden priemgetal printen.

Klopt je antwoord? Check het op internet!

## Stap 3: het zoveelste priemgetal

We gaan nu terug naar de opdracht: op zoek naar het $$N$$-de priemgetal. We geven een voorzetje voor de strategie van het programma:

- Nu zoeken we het `N`-de priemgetal; we willen niet weten of `N` een priemgetal is (zie je het verschil met stap 2?) Je kunt nu niet meer met een `for`-loop simpelweg tot `N` loopen. Immers, bij een `for`-loop weet je van tevoren hoe vaak er geïtereerd wordt en dat weten we nu niet. Je moet dus in je programma gaan bijhouden *hoeveel* priemgetallen je al gevonden hebt. Gebruik hiervoor een variabele, net als bij het bijhouden van de hoeveelheid delers in Stap 1. Merk op dat dit bijhouden van informatie in een variabele (bv. een 'teller') nu al een paar keer handig blijkt. We zullen dit meerdere keren terug zien komen bij de rest van het vak, dus oefen er goed mee!

- Definieer een functie `zoveelste_priem()`, met één argument: `N`. De functie moet vervolgens het `N`ste priemgetal returnen.

- Zoals bovenaan beschreven moet bij het runnen van je programma de gebruiker om input worden gevraagd tot een geheel getal wordt gegeven. Doe dit opvragen buiten de functie en geef de input als argument aan je functie.

- Begin klein. Zorg dat je programma eerst de priemgetallen tot 10 kan vinden. Dat is klein genoeg om te zien of het programma precies doet wat de bedoeling is, en kun al snel ontdekken wat er mis gaat.

- Problemen? Print bij elke kandidaat-priem wat informatie, zodat je weet waar je bent in de berekening en je ziet of de computer ook echt jouw bedoelde strategie volgt.

> Misschien is het raar of vervelend om een programma in te tikken, waarna je ontdekt dat het niet goed werkt. Dat is het lot van de programmeur: het is gewoon heel moeilijk om een precies algoritme te formuleren en dan helemaal correct om te zetten naar programmacode. Soms ben je een uitzondering vergeten, maar net zo goed heb je ergens een tikfout gemaakt. Bedenk dan dat de beste programmeurs op deze manier werken!

## Stap 4: werkt het echt?

Loop nu de specificatie bovenaan de opdracht goed door en zorg dat je programma precies zo werkt als daar beschreven is.

Dan ben je klaar om te testen:

    checkpy priemgetal

## Stap 5: kleine optimalisaties

Deze stap is volledig optioneel, dus hoeft niet ingeleverd te worden. Wel goed om over na te denken en te proberen als je tijd over hebt.

We zijn hierboven zo simpel mogelijk begonnen, zodat we snel tot een *correct* programma zijn gekomen (gecontroleerd door `checkpy`). Maar met behulp van wat wiskundig inzicht kunnen we kleine optimalisaties doen, waardoor het programma sneller wordt. 

- Behalve 2 zijn *even* getallen nooit een priemgetal (dit vraagt slechts een hele kleine aanpassing van je code).

- Als je een deler vindt hoef je niet verder te zoeken omdat je dan gelijk weet dat het geen priemgetal is.

## Stap 6: grote optimalisaties

Deze stap is volledig optioneel, dus hoeft niet ingeleverd te worden.

Bovenstaande optimalisaties geven een beperkte snelheidswinst, in die zin dat je daarmee geen veel grotere priemgetallen gaat vinden dan mogelijk is met het basisalgoritme. Je kunt wel overstappen naar een fundamenteel ander algoritme.

Als je wilt bepalen of 137 een priemgetal is, welke kandidaat-delers bekijk je dan voordat je zeker weet dat het een priemgetal is? Doe dit op pen en papier. Delen door 2 en alle oneven getallen tot het getal is een beetje teveel van het goede. Een wiskundige deelt bijvoorbeeld alleen door 2, 3, 5, 7, 11. Bedenk waarom (dit vraagt waarschijnlijk een flinke aanpassing van je code).

Om dit idee in een algoritme te implementeren heb je hulp nodig van lijsten (lijsten van priemgetallen in dit geval). Bestudeer [hier](/python/lijsten) hoe ze werken in Python.

Als je deze versie maakt zal `checkpy` klagen dat je lijsten gebruikt. Dat is geen probleem, je mag het gewoon inleveren.

## Hints

Je kunt dit programma schrijven met alleen de Python-onderdelen die je tot nu toe hebt geleerd!

## Testen

Test voor de zekerheid nog een keer of je programma werkt volgens `checkpy`:

    checkpy priemgetal
