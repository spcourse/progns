# Bouwsteen 3: Functies

Nu we logica en loops hebben gezien komen we aan bij _functies_. Een functie is een stukje code (met een eigen naam) die een specifieke taak uitvoert en steeds herbruikt kan worden. Functies worden bij het programmeren veel gebruikt omdat het je code overzichtelijker maakt en het is daarom belangrijk goed te begrijpen hoe ze wel (en niet) werken.

Belangrijk om te onthouden is dat functies _input_ hebben en _output_ (wordt ook wel return waarde genoemd).

# De snelle introductie


## Functies: van wiskunde naar programmeren 
Op de middelbare school heb je bij wiskunde veel functies gezien in de vorm van _y = f(x)_. Het is een 'voorschrift' dat de waarde van y berekent voor een specifieke input-waarde *x*. 

Voorbeeld vanuit de wiskunde:
    _f(x) = x^2 + 4x - 5_
Input is hier de waarde van _x_ en de return-waarde is _y_.

In een computerprogramma 'vang' je deze functionaloiteit in de functie _f_. Je definieert deze als volgt:

    def f(x):
        y = x*x + 4*x - 5
        return y

Dit is dus een stukje code (functionaliteit) die je programma kunt gebruiken, bijvoorbeeld in het volgende stukje code waarin je de functie als input de waarde 3 meegeeft en het resultaat op het scherm print.

    a =  3
    resultaat = f(a)
    print("het resultaat = ", resultaat)

Een paar dingen die hier belangrijk zijn om op te merken:
  - in de definitie van de functie gebruikten we als naam voor de input-variabele _x_ en als de variabele _y_ als resultaat. Deze variabelen 'bestaan' alleen *in* de functie zelf. Zoals je ziet roepen wij de functie aan met de variabel _a_. 
  - De functie 'geeft het resultaat terug' aan de user (via het als return statement). In het hoofdprogramma kun je deze variabele in een variabele stoppen - wij noemen dat in ons stukte code _resultaat_ en daar kun je dan weer verder mee rekenen, bijvoorbeeld op het scherm printen. Dat doen we in ons voorbeeld.

Je hoeft niet per se de output-waarde in een nieuwe variabele op te slaan. Je had het voorbeeld ook zo kunnen op schrijven:

    a =  3
    print("het resultaat = ", f(a))

In de voorbeelden in de video's worden de functies aangeroepen binnen ene print-statement, net zoals hierboven, maar het is gebruikelijker om de functie gewoon in de code zelf aan te roepen en vervolgens de output te printen.

## Functies: complexere input en output
In het bovenstaande voorbeeld is de link met de wiskundige formule vrij eenvoudig, maar je kunt zowel de input als output veel complexer maken. Je zou bijvoorbeeld een functie kunnen schrijven die voor een specifiek input-getal een lijst met alle priemgetallen onder dat getal teruggeeft. Of alleen True of False. De input kan ook bestaan uit meerdere parameters in de functie.

Twee voorbeelden:

(1) dezelfde functie als hierboven, maar waarmee je ook de parameters van de kwadratische functie mee kunt geven:

    def f(x,a,b,c):
        y = a*x*x + b*x - c
        return y

(2) een functie die het grootste getal bepaalt van twee input-getallen:

    def grootste(a,b):
        if(a>b):
           grootste = a
        else:
           grootste = b
        return grootste


Laatste opmerking over input en output: Je functie hoeft niet per se een input-waarde en return-waarde te hebben. Het kan bijvoorbeeld ook alleen maar iets printen. Ook als je geen return waarde  bestaan ook functies die geen return waarde hebben. Het is goed om dan toch je functie af te sluiten met _return_

### meerdere return waardes

Een functie kan ook meerdere output waardes teruggeven in een return-statement. Kijk bijvoorbeeld naar dit voorbeeld waarbij de functie zowel de omtreek als de oppervlakte van een vierkant uitrekent als het de lenbte van een zijde als input krijgt.

    def vierkant(a):
        omt = 4*a
        opp = a*a
        return omt,opp


    zijde = 5
    omtrek, oppervlakte = vierkant(zijde)
    print("omtrek vierkant = ", omtrek)
    print("oppervlakte vierkant = ", oppervlakte)

In dit voorbeeld hebben de namen van de parameters in de functie en die in het hoofdprogramma een andere naam. Dat hebben we expres gedaan om jullie te laten zien dat het 'verschillende werelden' zijn. Dit zullen we later op deze pagina nog extra benadrukken.

### conclusies

Functies zijn een manier om een stuk code 'los' te zetten van de rest van je programma. Daarmee wordt niet alleen je code overzichtelijk, maar kun je ook op een meer gestructureerde manier naar de werking/logica van je programma kijken. De voorbeelden hierboven zijn kleine stukjes code, maar functies kunnen ook vrij uitgebreid zijn

Je kunt in je programma gebruik maken van je eigen functies, maar  natuurlijk ook de functies die door andere mensen geschreven zijn. Deze functies zijn in lzogenaamde bibliotheken opgeslagen en die staan ook tot je beschikking - dat leren we later. Een voorbeeld is bijvoorbeeld de _sqrt()_ functie in de wiskunde bibliotheek (hoe zou je dat zelf programmeren?) of de _plot()_ functies om grafieken te maken uit de Matplotlib bibliotheek.

<br>
<br>


# De wat langere introductie 

Leren om bestaande functies te gebruiken en zelf functies te maken zijn een belangrijk aspect van leren programmeren. Je kunt heel eenvoudig zelf functies maken. Om in je code een functie te definiëren start je met `def`, daarna komt de functienaam (die je zelf mag kiezen), en vervolgens komen de haakjes met daartussen mogelijke input parameters.

Voorbeeld:

    def zeg_hallo():
        print("Hallo, Python!")

Dit is een functie die de string `Hallo, Python!` op het scherm print. Als je bovenstaande *definitie* (vandaar "def") in een Python-bestand zet weet de computer dat er nu een functie is
met de naam `zeg_hallo`. Maar de functie is nog niet *uitgevoerd*! Dit moet je zelf nog doen door
de functie expliciet *aan te roepen*. Dit doe je zo:

    zeg_hallo()

## Functies: input-output machines!

Een functie kan geen, één of meerdere parameters als input nemen en/of als output geven.

Bekijk de video's hieronder, waarin wordt uitgelegd hoe dit werkt.

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_hkab4t85&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_1czpky81)


![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_747kicts&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_s2jo0x4e)

Laten we om te oefen eens proberen om de code van _rekenwonder_ in een functie te schrijven. Maak een nieuw bestand `functies_oefenen.py` en neem daarin de volgende code over.

    def product(getal_1, getal_2):
        output = getal_1 * getal_2
        return output

    antwoord = product(17, 13)
    print(antwoord)

Door de code in een functie te zetten kunnen we de producten van verschillende getallen berekenen. In een functie kun je printen, zoals gedaan werd hierboven in `zeg_hallo`, maar een functie kan ook
output geven via het commando `return`. Na `return` kun je één of meerdere (gescheiden door een komma, net als bij input) output variabelen meegeven. Als een functie eenmaal iets returnt, stopt
de functie. Alles wat onder `return` staat, wordt niet meer uitgevoerd door het programma.

Merk ook op dat we de output van de functie _product_ opslaan in een variabele, zodat we er later in ons programma nog iets mee kunnen doen.

Als je verder niets met de output doet zou je je code zo kunnen schijven in je 'hoofdprogramma':

    print(product(17, 13))


Het is goed om op te merken dat als je doel was om het resultaat alleen maar op het scherm te printen je het ook anders had kunnen oplossen. Je had bijvoorbeeld de print() ook _in_ de functie zelf kunnen opnemen. Hoe je je functie precies implementeert is aan jou.

Laten we met wat oefenen met functies.

**Oefening 1:** Laat de functie eens iets printen ná het return statement. Wordt deze regel uitgevoerd?

**Oefening 2:** Hernoem de functie naar `product_en_som` en return niet alleen het product maar ook de som van de twee getallen. Wat moet je doen als je de antwoorden wil printen op de tweede manier?


## Globaal en lokaal

Een functie kun je dus zien als een machine die input neemt en output geeft. De informatie
(variabelen) die binnen en buiten de functie bestaat komen alleen niet altijd overeen.

**Oefening 3:** Voeg boven `print(product(29, 11))` de code `print(output)` toe.
Wat betekent de error die je krijgt?

**Oefening 4:** Haal `getal_2` weg uit de input van je functie (zodat alleen nog `getal_1` de input
is) en definieer boven de definitie van de functie de variabele `getal_2 = 2`. Roep nu onder de
definitie van de functie de functie aan met één ingevuld argument en print het resultaat. Krijg je
een error?

Je hebt zojuist het verschil gezien tussen *lokale* en *globale* variabelen. De variabelen die
buiten een functie staan gedefinieerd kun je binnen een functie gebruiken (globale variabelen),
maar buiten de functie is het niet bekend wat er binnen de functie gebeurt is of wat voor
variabelen er zijn gedefinieerd (lokale variabelen). Alleen met `return` of met globale variabelen
kun je informatie van binnen de functie naar buiten brengen. Het is als een huis met een grote hal
en kamers waarin je wel alle gereedschappen van de grote hal in en uit de kamers mag brengen, maar
je de gereedschappen van de kamers niet naar de hal mag brengen.

**Oefening 5:** Herstel de functie zodat deze weer twee inputs `getal_1` en `getal_2` heeft.
Definieer nu onder de functie `getal_1 = 17` en `getal_2 = 29` en roep de functie aan met
`product(getal_1, getal_2)`. Je ziet dat er geen probleem optreedt, ondanks dat we de variabelen
zowel globaal definiëren als lokaal in de functie als argument gebruiken. Dit kan dus.

## Modulariteit

Net als loops zijn functies handig als je stukken code hergebruikt: op die manier hoef je die code
niet opnieuw te typen. Het gebruik van functies bevordert ook de leesbaarheid van je code. Met goed
gekozen namen voor deze functies kun je snel een overzicht krijgen van wat het geheel doet. Je
leest dan bijvoorbeeld eerst alleen even snel de functienamen in een programma.

Het is vaak handig om bijna al je code in een programma in functies te schrijven. Het komt ook voor dat je programma globale variabelen bevat die essentieel zijn voor het programma en makkelijk aangepast moeten kunnen worden. Die definieer je het beste bovenaan onder het importeren van de bibliotheken, dus ook buiten functies. Het programma noemen we dan *modulair* want het bestaat uit losse *modules* (namelijk de functies). Dit soort programma's leest vaak prettig en ze zijn fijn om mee te werken.

**Oefening 6:** Neem de onderstaande code over in je bestand.

    # check of getal even is
    def even(getal):
        if getal % 2 == 0:
            return True
        else:
            return False

We gebruiken hier de in "Algoritmen en logica" geïntroduceerde booleans en modulo-rekenen.
Schrijf nu boven deze functie `N = 20` en onder deze functie definiëren we een nieuwe:

    # print de even getallen onder N
    def vind_even(N):
        for getal in range(N):
            is_het_getal_even = even(getal)
            if is_het_getal_even:
                print(f"{getal} is even")

Roep nu de functie aan met `vind_even(N)`. Kijk eens aan! We hebben nu een programma geschreven
waarin alles in functies staat, afgezien van globale variabelen en het aanroepen van sommige
functies. Je kunt de code zelfs nog compacter maken door de variabele `is_het_getal_even` weg te
halen. Het is opnieuw een keuze hier of je de data direct wil gebruiken of hem eerst wil opslaan
in een variabele voor eventueel later gebruik.
