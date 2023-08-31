# Monte-Carlo

Schrijf een functie die middels de Monte-Carlo-methode de integraal berekent van een willekeurige wiskundige functie  met gespecificeerde integratiegrenzen. Zorg dat zowel de functie zelf als de gegooide punten (zowel de 'goede' als de 'foute') op het scherm weergegeven worden.

## Achtergrond

Het is mogelijk een integraal te benaderen door gebruik te maken van random getallen.

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_rouef2qo&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_er3r5kip)

Voor *positieve* integratiegebieden gebruik je het volgende stappenplan.

1.  Definieer een rechthoek die het integratiegebied omsluit

    Definieer een gebied (vaak een rechthoek) die de integraalregio omsluit. Kies dus 
    een  $$x_{min}$$, $$x_{max}$$, $$y_{min}$$ en $$y_{max}$$ zodanig dat geldt 

      - voorwaarde 1: $$x_{min} \leq a$$ en $$x_{max} \geq b$$

      - voorwaarde 2: voor $$a \leq x \leq b: ~ y_{min} \leq f(x)  \leq y_{max}$$

    Kies de meest smalle rechthoek met $$x_{min} = a$$ en $$x_{max} = b$$.

2.  Gooi random punten in de rechthoek

    Gooi een groot aantal random punten $$(x_i, y_i)$$ in de rechthoek die het integratiegebied om sluit en 
    bekijk voor elk punt of het binnen het integratiegebied valt ('goed') of erbuiten ('fout'). Hou bij welke 
    fractie van de punten in het integratiegebied valt: $$f_{goed}$$.

3.  Bepaal de integraal

    De integraal is de fractie punten die binnen de grafiek vallen keer de oppervlakte van de totale rechthoek. 
    In het geval van een rechthoek wordt die waarde gegeven door:

    $$
        \int_a^b f(x)~\text{d}x = f_{goed}~~\cdot~(x_{max}-x_{min})\cdot(y_{max}-y_{min})
    $$

### Voorbeeld

Van de functie $$\sin(x)$$ weten we dat het op het domein $$0 < x < \pi$$ tussen de 0 en de 1 ingesloten ligt. We 
definiëren dan ook een rechthoek om het integratiegebied heen en 2000 random punten gegooid. Daarvan bleek 63.15% 
(1263/2000) binnen het integratiegebied te vallen. De schatting die we maken van de integraal met behulp van 
deze 2000 punten is dan ook: 0.6315 $$\pi \approx$$ 1.984. Zodra dit werkt kunnen we natuurlijk ook 1 miljoen 
punten gooien in plaats van 2000. 

![](MonteCarloExample.png)



## Specificatie

- Maak een nieuw bestand genaamd `montecarlo.py`.

- Schrijf een functie `montecarlo()` die integralen kan berekenen met behulp van een Monte-Carlo-simulatie. 

- De functie `montecarlo()` moet vijf argumenten accepteren:

	- `func` een functie waarvan we de integraal gaan bepalen
	- `x1` de eerste x waarde
	- `y1` de eerste y waarde
	- `x2` de tweede x waarde
	- `y2` de tweede y waarde

- De functie `montecarlo()` moet de integraal van de gegeven functie teruggeven als resultaat.

- De functie `montecarlo()` moet de functie plotten en de punten *in* het integratiegebied (de 'goede' punten) in groen en de 'foute' punten in rood tekenen.


## Tests

Test je procedure met de volgende functie, die je makkelijk analytisch kunt controleren:

	def functie1(x):
		return x**2

Test ook met de volgende functies. Sommige daarvan zijn "integreerbaar", andere kun je alleen numeriek benaderen.

$$\int_{0}^{1}x^2 \text{d}x$$

$$\int_{0}^{1}x^{x+\frac{1}{2}} ~\text{d}x$$

$$\int_{0}^{\pi}\sin(x) \text{d}x$$

$$\int_{0.2}^{2.2} \tan(\cos(\sin(x))) ~\text{d}x$$

$$\int_{0}^{\pi} \sin(x^2) ~\text{d}x$$

Zet deze functies in je eigen programma en zorg dat je onderaan een aantal keer je `montecarlo()`-functie aanroept, om deze voorbeelden te controleren.

## Hints

- Kijk goed naar de grafiek van de rode en groene punten die je maakt zodat je duidelijk ziet welk gebied je aan het integreren bent. Mocht je een fout gemaakt hebben in je logica dan zie je dat in een plaatje in één keer terwijl je daar anders uren naar moet zoeken in de code zelf.

- Als je ook negatieve integratieregio's hebt, moet je die niet gewoon bij de positieve regio's optellen (waarom ook alweer niet?) maar is het handig om de integratiegebieden splitsen. Hoe verandert voorwaarde 2 uit stap 1 van het stappenplan voor positieve integratieregio's? Hoe verandert de waarde van de integraal uit stap 3?

- In onderzoekstoepassingen wordt voor maximalisatie van de efficiëntie de rechthoek zo gekozen dat hij de integraal zo nauw mogelijk omsluit.

- Test je functie altijd eerst op een integraal waarvan je de uitkomst kent. Dit is het geval voor een aantal van de functies die hierboven staan weergegeven. Pas als jouw functie die integralen goed uitrekent kan je met vertrouwen de onbekende nieuwe integraal aanpakken.

## Testen

**Let op! Zorg dat je checkpy meerdere keren gebruikt om te kijken of montecarlo elke keer het zelfde antwoord geeft. Dit ligt namelijk aan de verhouding tussen je gekozen integratiegebied en het aantal keer dat je punten "gooit". Tegelijk moet je wel zorgen dat het aantal punten niet veel te groot is, anders riskeer je een time-out.**

	checkpy montecarlo
