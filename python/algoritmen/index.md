# Algoritmen en logica

Computers laten pas echt zien wat ze kunnen als de oplossing van een probleem niet goed uitgedrukt kan worden door een formule. Bij programmeren werken we aan het verzinnen en uitschrijven van *algoritmen*, die precies specificeren hoe een probleem stap-voor-stap opgelost moet worden. Een belangrijk aspect van algoritmen is dat ze werken voor verschillende invoer. In het filmpje hieronder moet het algoritme het juiste antwoord opleveren als er 0, 1, 2, 3, 4, enz. mensen in de kamer zijn.

![embed](https://www.youtube.com/embed/6hfOvs8pY1k)

In het hoofdstuk [basiselementen](/python/basiselementen) heb je een aantal **instructies** (**statements**) geleerd waar Python mee om kan gaan:

- de `print`-instructie, om boodschappen aan de gebruiker door te geven
- de `input`-instructie, om informatie van de gebruiker op te vragen
- de `=`-operator, om variabelen te definiëren of te wijzigen

Daarnaast heb je kennis gemaakt met operatoren die gebruikt worden om expressies samen te stellen. Dit was al genoeg om een werkend, maar niet zo krachtig programma te schrijven. Aan het eind van dit subonderdeel gaan we een opdracht over **priemgetallen** maken, die een stuk meer kan dan alleen getallen vermenigvuldigen en printen. Om deze te kunnen maken gaan we drie belangrijke onderdelen van programmeren in Python leren:

1. Logica
2. Loops
3. Functies

Deze drie bouwstenen maken voorwaardelijke instructies en herhaling en hergebruik van code mogelijk. Het leren ervan zal de komende uren even wat tijd kosten, maar als je ze goed begrijpt wordt programmeren een stuk makkelijker en leuker!


## Bouwsteen 1: Logica (voorwaardelijke instructies)

In de voorgaande programma's schreven we scriptjes die regel voor regel van boven naar beneden werden uitgevoerd. Een soort stapsgewijze handleiding. Programma's worden interessanter als we *uitzonderingen* willen beschrijven.

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_c3agfme9&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_ll4p0wzx)

### Details

Een `if`-statement in Python kent de volgende structuur:

    if conditie:
        code

Een stukje voorbeeldcode met een if-statement kan zijn:

    balans = 100
    uitgave = 75

    if uitgave < balans:
        balans = balans - uitgave
        print(f"Transactie van bedrag €{uitgave} voltooid.")

Een **voorwaarde (condition)** kent uiteindelijk maar twee mogelijke opties. In Python zijn dit `True` en `False` (dit noemen we "boolean" waardes, naar [George Boole](https://en.wikipedia.org/wiki/Boolean_algebra#Values)). In de code hierboven is deze boolean het resultaat de expressie `balans - uitgave > 0`. Hier wordt gebruik gemaakt van de vergelijkingsoperator `>`. Deze operator vergelijkt twee waarden, in dit geval de uitkomst van `balans - uitgave` en `0`, en produceert een boolean. Afhankelijk van de uitkomst, dat kan dus zijn `True` of `False`, wordt de code die bij de `if`-statement hoort uitgevoerd.

De `:` op regel 4 hierboven laat zien dat bij de `if` een **codeblok** hoort. Dat is dus precies het deel van de code dat slechts wordt uitgevoerd als aan de voorwaarde is voldaan. Zo'n blok bestaat vaak uit meerdere regels code, en om duidelijk te maken welke regels dat zijn, gebruik je **indentatie**. Dat is een aantal spaties of tabs van de kantlijn af. In de code hierboven hebben we vier spaties gebruikt om aan te geven dat regel 6 bij het `if`-statement hoort. Omdat regel 8 weer meer naar links staat, is die regel niet meer afhankelijk van de uitkomst van de conditie op regel 5. Die regel wordt dus *onvoorwaardelijk* uitgevoerd.

### Meer operatoren

Mocht je meer nodig hebben dan de vergelijkingsoperatoren hierboven:

- `==`  gelijk aan (let op: een enkele = is toekennen, een dubbele vergelijken!)
- `!=`  ongelijk aan
- `>` 	groter dan
- `>=`	groter of gelijk aan
- `<` 	kleiner dan
- `<=`	kleiner dan of gelijk aan

### Combinaties van voorwaarden

Je kunt verschillende voorwaarden combineren. Als je wilt weten of een getal zich in een bepaald bereik bevindt (bijvoorbeeld tussen de 3 en de 39) dan kun je dat doen met `and`:

    getal = 15
    getal_min = 3
    getal_max = 39
    if getal > getal_min and getal < getal_max:
        print(f"het getal {getal} bevindt zich tussen {getal_min} en {getal_max}")

Hier zijn de drie operatoren om voorwaarden te combineren:

- `not` ontkenning
- `and` combinatie (allebei moeten `True` zijn)
- `or` combinatie (één van beide moet `True` zijn)
