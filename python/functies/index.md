# Bouwsteen 3: Functies

Nu we logica en loops hebben gezien komen we aan bij _functies_. Een functie is een stukje code (met een eigen naam) die een specifieke taak uitvoert en steeds herbruikt kan worden. Functies worden bij het programmeren veel gebruikt omdat het je code overzichtelijker maakt en het is daarom belangrijk goed te begrijpen hoe ze wel (en niet) werken.


## Functies: van wiskunde naar programmeren 
Op de middelbare school heb je bij wiskunde veel functies gezien in de vorm van _f(x)_. Het is een 'voorschrift' dat de waarde van y berekent voor een specifieke input-waarde _x_. Bijvoorbeeld een parabool:  _f(x) = x<sup>2</sup> + 4x - 5_

In een computerprogramma 'vang' je deze functionaliteit in een functie. Je definieert deze als volgt:

    def f(x):
        y = x*x + 4*x - 5
        return y

Om dicht bij het voorbeeld vanuit de wiskunde te blijven hebben we de functie de naam  _f_ geven. Input is hier _x_ en het resultaat van de functie is  _y_. Dat noemen we de 'return-waarde'.  Als je bovenstaande *definitie* (vandaar "def") in een Python-bestand zet weet de computer dat er nu een functie is met de naam `f`. De functie doet alleen iets als het expliciet wordt *aangeroepen*. Dit doe je zo:

De functie is dus een stukje code die je programma kunt gebruiken, bijvoorbeeld in het volgende stukje code waarin je de functie als input de waarde 3 meegeeft en het resultaat op het scherm print.

    xwaarde =  3
    resultaat = f(xwaarde)
    print("het resultaat = ", resultaat)

Een paar dingen die hier belangrijk zijn om op te merken:

  - in de definitie van de functie gebruikten we als naam voor de input-variabele _x_ en als de variabele _y_ als resultaat. Deze variabelen 'bestaan' alleen *in* de functie zelf. Zoals je ziet roepen wij de functie aan met de variabel _xwaarde_. De werelden binnen en buiten de functie zijn strikt van elkaar gescheiden. Deze variabalen noemen we 'locake' variabelen. Je kunt in het hoofdprograma dan ook niet de waarde van _y_ printen bijvoorbeeld. Extra: er bestaat een speciale klasse van variabelen ('globale' variabelen) die zowel binnen als buiten de functies te gebruiken zijn. Deze zullen we in dit vak niet gebruiken,m maar het is wel goed om de naam te kennen. 	
  - De functie 'geeft het resultaat terug' aan de user (via het als return statement). In het hoofdprogramma kun je deze variabele in een variabele stoppen - wij noemen dat in ons stukte code _resultaat_ en daar kun je dan weer verder mee rekenen, bijvoorbeeld op het scherm printen. Dat doen we in ons voorbeeld.

Je hoeft niet per se de output-waarde in een nieuwe variabele op te slaan. Je had het voorbeeld ook zo kunnen op schrijven:

    a =  3
    print("het resultaat = ", f(a))


<b>Let op:</b> in de voorbeelden in de video's worden de functies aangeroepen binnen een print-statement, net zoals hierboven, maar het is gebruikelijker om de functie in de code aan te roepen en vervolgens de output te printen.

**Oefening 1:** schrijf een programma dat bovenstaande functie aanroept (in een loop) voor waardes van x tussen 0 en 100. 


## Functies: complexere input en output
In het bovenstaande voorbeeld is de link met de wiskundige formule vrij eenvoudig, maar je kunt zowel de input als output veel complexer maken. Je zou bijvoorbeeld een functie kunnen schrijven die voor een specifiek input-getal een lijst met alle priemgetallen onder dat getal teruggeeft. Of alleen True of False. De input kan ook bestaan uit meerdere parameters in de functie. Hieronder bekijken we een paar voorbeelden hiervan.


#### Meerdere input-waardes

Twee voorbeelden:

(1) dezelfde functie als hierboven, maar waarmee je ook de parameters van de kwadratische functie (a,b en c) mee kunt geven:

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



**Oefening 2:** pas de bovenstaande functie _grootste()_ zo aan dat de functie op het scherm print 'Er is geen grootste getal: ze zijn aan elkaar gelijk.' Test dit met aan aantal voorbeelden.


Een functie _hoeft_ trouwens niet per se een input-waarde te hebben. Zie bijvoorbeeld de functie:

    def zeg_hallo():
        print("Hallo, Python!")

Dit is een functie die de string `Hallo, Python!` op het scherm print. Dit soort functies zullen we in dit vak bijna niet gebruiken.


Laatste opmerking over input en output: Je functie hoeft niet per se een input-waarde en return-waarde te hebben. Het kan bijvoorbeeld ook alleen maar iets printen. Ook als je geen return waarde  bestaan ook functies die geen return waarde hebben. Het is goed om dan toch je functie af te sluiten met _return_


#### Meerdere return-waardes

Een functie kan ook meerdere output waardes teruggeven in een return-statement. Kijk bijvoorbeeld naar dit voorbeeld waarbij de functie zowel de omtrek als de oppervlakte van een vierkant uitrekent als het de lengte van een zijde als input krijgt.

    def vierkant(a):
        omt = 4*a
        opp = a*a
        return omt,opp

    zijde = 5
    omtrek, oppervlakte = vierkant(zijde)
    print("omtrek vierkant = ", omtrek)
    print("oppervlakte vierkant = ", oppervlakte)

Ook in dit voorbeeld hebben de namen van de parameters in de functie en die in het hoofdprogramma een andere naam. Dat hebben we expres gedaan om nog een keer te benadrukken dat het 'verschillende werelden' zijn. Dit zullen we later op deze pagina nog extra benadrukken.


### conclusies

Functies zijn een manier om een stuk code 'los' te zetten van de rest van je programma. Daarmee wordt niet alleen je code overzichtelijk, maar kun je ook op een meer gestructureerde manier naar de werking/logica van je programma kijken. De voorbeelden hierboven zijn kleine stukjes code, maar functies kunnen ook vrij uitgebreid zijn

Je kunt in je programma gebruik maken van je eigen functies, maar  natuurlijk ook de functies die door andere mensen geschreven zijn. Deze functies zijn in lzogenaamde bibliotheken opgeslagen en die staan ook tot je beschikking - dat leren we later. Een voorbeeld is bijvoorbeeld de _sqrt()_ functie in de wiskunde bibliotheek (hoe zou je dat zelf programmeren?) of de _plot()_ functies om grafieken te maken uit de Matplotlib bibliotheek.


<br>
<br>








## kleine oefeningen

**Oefening 1:** schrijf een functie 


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





## Voorbeelden: input-output machines

Een functie kan geen, één of meerdere parameters als input nemen en/of als output geven.

Bekijk de video's hieronder, waarin wordt uitgelegd hoe dit werkt.

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_hkab4t85&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_1czpky81)


![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_747kicts&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_s2jo0x4e)



