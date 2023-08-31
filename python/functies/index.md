# Bouwsteen 3: Functies

Nu we logica en loops hebben gezien komen we aan bij functies. Een *functie* is een stukje code
waar je een naam aan geeft, zodat het hergebruikt kan worden. Functies die je eerder al gebruikt
hebt zijn `print()` en `input()`.

Je kunt ook zelf functies definiëren. Als je bijvoorbeeld een stuk code hebt geschreven om data
mooi te plotten, wil je niet telkens opnieuw de hele code kopiëren als je nieuwe data hebt.
Bovendien bieden functies een handige manier om stukken code die andere dingen doen van elkaar te
scheiden. Door je code in functies te zetten wordt je werk dus overzichtelijk en dat is fijn om
 te gebruiken en om naar te kijken!

Functies zijn dus een belangrijk aspect van leren programmeren. Het begin van een functie wordt
aangegeven met `def`, daarna komt de functienaam (die je zelf mag kiezen), en vervolgens komen de
haakjes met daartussen mogelijke parameters:

    def zeg_hallo():
        print("Hallo, Python!")

Dit is een functie die de string `Hallo, Python!` naar je terminal print. Als je bovenstaande
*definitie* (vandaar "def") in een Python-bestand zet weet de computer dat er nu een functie is
met de naam `zeg_hallo`. Maar de functie is nog niet *uitgevoerd*! Dit moet je zelf nog doen door
de functie expliciet *aan te roepen*. Dit doe je zo:

    zeg_hallo()

## Functies: input-output machines!

Een functie kan geen, één of meerdere parameters als input nemen en/of als output geven.
Bekijk de video's hieronder, waarin wordt uitgelegd hoe dit werkt.

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_hkab4t85&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_1czpky81)


![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_747kicts&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_s2jo0x4e)

We zagen al eerder hoe we van onze code van `hello.py` in een functie kunnen zetten. Laten we dat
ook eens met de code van rekenwonder doen. Maak een nieuw bestand `functies_oefenen.py` en neem
daarin de volgende code over.

    def product(getal_1, getal_2):
        output = getal_1 * getal_2
        return output

    print(product(29, 11))
    antwoord = product(17, 13)
    print(antwoord)

Door de code in een functie te zetten kunnen we de producten van verschillende getallen berekenen.
In een functie kun je printen, zoals gedaan werd hierboven in `zeg_hallo`, maar een functie kan ook
output geven via het commando `return`. Na `return` kun je één of meerdere (gescheiden door een
komma, net als bij input) output variabelen meegeven. Als een functie eenmaal iets returnt, stopt
de functie. Alles wat dus onder `return` zou staan, wordt niet meer uitgevoerd door het programma.

Merk ook op dat we op twee manieren het product printen: in het eerste geval printen we het
resultaat direct en bij de tweede manier slaan we wat de functie returnt eerst op als variabele
en daarna printen we die variabele. Op die manier blijft wat de functie aan informatie heeft
gegenereerd beschikbaar in de variabele waar we later nog wat mee kunnen doen, ipv. dat we die
informatie alleen maar printen.

**Oefening 1:** Laat de functie eens iets printen ná het return statement.
Wordt deze regel uitgevoerd?

**Oefening 2:** Hernoem de functie naar `product_en_som` en return niet alleen het product maar ook
de som van de twee getallen. Wat moet je doen als je de antwoorden wil printen op de tweede manier?


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

Het is vaak handig om bijna al je code in een programma in functies te schrijven. Er zijn wel
uitzonderingen: packages importeren en het definiëren van andere functies doe je niet in een
functie. Het komt ook voor dat je programma globale variabelen bevat die essentieel zijn voor
het programma en makkelijk aangepast moeten kunnen worden. Die definieer je het beste bovenaan
onder het importeren van de packages, dus ook buiten functies. Het programma noemen we dan
*modulair* want het bestaat uit losse *modules* (namelijk de functies). Dit soort programma's
lezen vaak prettig en zijn fijn om mee te werken.

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
