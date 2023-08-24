# Bestanden inlezen en analyseren

Een veel voorkomende toepassing van computerprogramma’s is het inlezen, verwerken en analyseren van grote databestanden. Big data! We zullen in deze module leren hoe we data inlezen, en we gebruiken onze kennis van Python om de data te rubriceren en grafieken te maken van onze resultaten.

## Van Basten

![](VanBastenKlein.jpg){:.inline}

Net zoals je getallen in het decimale, hexadecimale of binaire formaat weer kan geven wordt ook data in verschillende formaten bewaard in data-bases. Hier zullen we data bekijken die is opgeslagen in het zogenaamde CSV formaat (Comma Separated Values): 'platte tekst', waarbij op elke regel verschillende variabelen gescheiden zijn door een komma. Dit is trouwens ook het formaat dat je krijgt als je je banktransacties download of een Excel-bestand wegschrijft.

We gaan het inlezen en verwerken van data doen aan de hand van een voorbeeld:  de statistieken van voetballer Marco van Basten. Iemand heeft in een [tekstbestand](VanBasten.txt) bijgehouden hoeveel wedstrijden hij gespeeld heeft en hoeveel doelpunten hij gemaakt heeft. Dit is de tekst van het bestand:

    198182, Ajax, 1, 1
    198283, Ajax, 20, 9
    198384, Ajax, 26, 28
    198485, Ajax, 33, 22
    198586, Ajax, 26, 37
    198687, Ajax, 27, 31
    198788, AC Milan, 11, 3
    198889, AC Milan, 33, 19
    198990, AC Milan, 26, 19
    199091, AC Milan, 31, 11
    199192, AC Milan, 31, 25
    199293, AC Milan, 15, 13
    199394, AC Milan, 0, 0
    199495, AC Milan, 0, 0

> Let op: als je het bestand met Windows Kladblok/Notepad opent, dan staat alle data achter elkaar. Dat maakt niet uit voor de goede werking van je programma's.

Hieronder gaan we aan de slag met het beantwoorden van enkele vragen met behulp van dit databestand:

- wat zijn de voetbalseizoenen waarin Van Basten meer dan 20 keer gescoord heeft?
- wat is het totaal aantal doelpunten dat Van Basten heeft gescoord voor al zijn clubs?

## Stap 1: openen van het bestand, inlezen van de regels

Omdat het doorlopen van bestanden in een computertaal een standaard procedure is, zijn er een aantal gemakkelijke commando's beschikbaar. Het `open` commando bijvoorbeeld dat vervolgens gebruikt kan worden om dingen uit dat bestand te lezen of juist in weg te schrijven. Het volgende codefragment opent het bestand en gebruikt een `for`-loop om steeds de volgende regel in te lezen. De informatie in een regel van het bestand wordt opgeslagen in de variable `regel`. Dit korte programma voert verder geen analyse uit maar print simpelweg `regel` naar het scherm. Wanneer alles wat geïndenteerd staat onder het `with`-commando is uitgevoerd wordt het bestand automatisch weer gesloten door achterliggende code behorend bij het `with`-commando.

    with open('VanBasten.txt', 'r') as input_bestand:
        for regel in input_bestand:
            print(regel)

> Tip: zorg dat het bestand `VanBasten.txt` in dezelfde directory staan als waar je Python programma staat zodat je programma hem altijd kan vinden. 

De `'r'` bij de functie `open()` betekent 'read', lezen dus. Als je dit programma uitvoert zal je zien dat bijvoorbeeld de regel van 1988 zo op het scherm verschijnt:

    198889, AC Milan, 33, 19

## Stap 2: splitsen van de regel en in een lijst opslaan

Elke regel bestaat uit verschillende elementen die gescheiden zijn door komma's. Toegang tot die verschillende parameters in de regel krijg je door de regel in stukken te ’knippen’. Dit doe je met het Python commando `split()`. Als parameter kan je aan split meegeven waar hij moet knippen. Wij willen dat hij bij elke komma (`,`) knipt, dus we voeren het volgende commando uit: `regel.split(',')`. Dit commando produceert een lijst met elementen die de losse stukken bevatten. Hierop kun je afzonderlijke bewerkingen uitvoeren.

    with open('VanBasten.txt', 'r') as input_bestand:
        for regel in input_bestand:
            print(regel)
            data_opgeknipt = regel.split(',')
            print(data_opgeknipt)

De regel met 1988 is nu in stukken geknipt en in een lijst gezet:

    ['198889', ' AC Milan', ' 33', ' 19\t\n']

De karakters `"\t"` (tab) en `"\n"` (return aan eind van de regel) zijn ook zichtbaar, hoewel we daar niet zoveel aan hebben.

## Stap 3: opslaan van de informatie in variabelen

In deze opgave zijn we alleen geïnteresseerd in het seizoen en het aantal doelpunten. Zoals je ziet is die informatie opgeslagen in respectievelijk element 0 en 2 van de lijst.

Die informatie kunnen we nu dus opslaan in een variabele:

    seizoen = data_opgeknipt[0]
    doelpunten = data_opgeknipt[2]

### Probleem 1: uitpakken van variabelen

Zoals je ziet hebben de makers van het bestand het seizoen 1988-1889 in 1 getal
weergegeven: 198889. Slim van ze, maar wij zijn alleen geïnteresseerd in het
jaar dat het seizoen is gestart.

Het handige voor ons is dat alle data nog als `string` in de lijst staat. Hoewel `198889` gezien kan worden als getal, behandelen we het nu als stuk tekst. Het eerste jaartal (1988) is verpakt in de eerste 4 karakters van die string. Om alleen die op te vragen kan je dus van element 0 in de lijst alleen de eerste 4 karakters selecteren.

    seizoen = data_opgeknipt[0][0:4]
    doelpunten = data_opgeknipt[2]

### Probleem 2: getallen versus tekst

Vanaf nu is het handig om de gegevens juist als getal te zien, zodat we ermee kunnen rekenen. Om te zorgen dat het jaartal en het aantal doelpunten een getal worden moet je ze expliciet omzetten.

    seizoen = int(data_opgeknipt[0][0:4])
    doelpunten = int(data_opgeknipt[2])

Je hebt nu dus de informatie tot je beschikking in een variabele. Vervolgens kun je met alle Python die je eerder hebt geleerd, de analyse uitvoeren.

## Stap 4: het analyseren van de data

We wilden het aantal totaal aantal doelpunten uitrekenen dat Van Basten voor zijn clubs heeft gescoord en ook aangeven in welke seizoenen hij meer dan 20 doelpunten maakte.

    with open('VanBasten.txt', 'r') as input_bestand:
        totaal_doelpunten = 0

        for regel in input_bestand:
            data_opgeknipt = regel.split(',')

            seizoen = int(data_opgeknipt[0][0:4])
            doelpunten = int(data_opgeknipt[2])

            totaal_doelpunten = totaal_doelpunten + doelpunten   

            if(doelpunten > 20):
                print(f"In {seizoen} scoorde Van Basten > 20 doelpunten, nl. {doelpunten}")

    print(f"TOTAAL: In totaal scoorde Van Basten {totaal_doelpunten} clubdoelpunten")

## Oefening

Download het bestand met de doelpunten statistiek van Van Basten en probeer de bovenstaande resultaten te reproduceren.

## Schrijven naar een bestand

Hoewel we dat in deze cursus niet tegen zullen komen is het belangrijk dat je weet hoe je gegevens naar een bestand schrijft in plaats van ze alleen maar in te lezen. Het is vrij eenvoudig zoals je in de volgende 2 voorbeelden zult zien. Belangrijkste is dat je bij het gebruik van het `open()` commando nu de extra parameter `'w'` (write) meegeeft.

### Voorbeeld: tekst schrijven naar een bestand

Dit stuk code opent een bestand 'output_bestand.txt', schrijft daar 1 regel tekst in weg en sluit het bestand weer.

    with open('output_bestand', 'w') as output_bestand:
        output_bestand.write("Het vak Inleiding Programmeren is bere-interessant")

### Voorbeeld: extra tekst achter bestaande regel plakken

Dit stuk code opent het bestand input_bestand, plakt voor elke regel de letters "XXX" en schrijft deze nieuwe regel vervolgens weg in een output-bestand.

    with open('input_bestand.txt', 'r') as input_bestand:
        with open('output_bestand.txt', 'w') as output_bestand:
            for regel in input_bestand:
                nieuwe_regel = "XXX " + regel
                output_bestand.write(nieuwe_regel)
