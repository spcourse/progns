# Riemann

Schrijf een functie die met behulp van een Riemann-som de integraal berekent van een willekeurige wiskundige functie met gespecificeerde integratiegrenzen. De wiskundige functie moet ook op het scherm weergeven worden.

## Achtergrond

Een van de manieren om een integraal te evalueren is door het te schrijven als de som van de oppervlakte van kleine rechthoekjes, de Riemannsom. Stel, het gaat om de volgende integraal:

$$ \int_a^b f(x)~\text{d}x $$

Dit gaat als volgt: verdeel het interval $$(a,b)$$ in $$N$$ intervallen van gelijke lengte $$\Delta x$$ en schrijf de integraal als de som (aangegeven met $$\Sigma$$)van de deel-integralen op elk van deze intervallen:

$$ \int_a^b f(x)~\text{d}x = \sum_{i=0}^{N-1} \int_{x_i}^{x_{i+1}} f(x)~\text{d}x$$

Hierbij zijn $$x_i$$ en $$x_{i+1}$$ de hoekpunten van een van de intervallen. Er zijn $$N+1$$ hoekpunten die lopen van $$x_0 = a$$ tot en met $$x_{N} = b$$. Iedere $$x_i$$ is dus simpelweg de waarde op de x-as die je krijgt door vanaf $$a$$ precies $$i$$ stapjes van grootte $$\Delta x$$ naar rechts te lopen. Zie de grafiek in het plaatje hieronder.

![](RiemannExample.png)

Nu we weten dat we op zoek zijn naar een flink aantal deel-integralen, gaan we ons verdere probleem flink versimpelen, door de deel-integralen te *benaderen*.

We stellen ze voor als een rechthoek, zoals te zien in de afbeelding. De breedte van de rechthoeken is overal hetzelfde en is natuurlijk gelijk aan $$\Delta x = (x_{i+1} - x_{i})$$. Een (simpele) schatting van de hoogte van de rechthoek die het best de integraal op dit kleine interval weergeeft vind je door simpelweg het gemiddelde te nemen van de waarde van $$f(x)$$ op de linkerkant, $$f_i := f(x_i)$$, en de rechterkant, $$f_{i+1} := f(x_{i+1})$$, van het interval. De integraal op het deelinterval is dan te schrijven als:

$$\int_{x_i}^{x_{i+1}} f(x)~\text{d}x = \frac{f_{i+1}+f_i}{2}~\Delta x$$

De volledige integraal is dan te schrijven als:

$$\int_a^b f(x)~\text{d}x = \frac{\Delta x}{2} (f_0 + 2 f_1 + 2 f_2 + ... +  2 f_{N-1} + f_N)~+~\mathcal{O}((\Delta x)^2)\\
                       ~~ \approx \Delta x~(f_1 + f_2 + ... +  f_{N-1}) ~+~ \frac{\Delta x}{2}(f_0+f_N) $$

In de evaluatie van de integraal $$\int_{0}^{\pi}\sin(x)~\text{d}x$$ hebben we het integratiegebied in $$x$$ opgedeeld in 13 gebieden van gelijke grootte. We hebben dan dus in totaal 14 $$x$$-waardes. De hoogte van elk van de 13 rechthoeken is het gemiddelde van de waarde aan de linkerkant en de rechterkant van het kleine integratiegebied.

De truc is de volgende: de uiteindelijke integraal kunnen we evalueren door de oppervlaktes van alle rechthoeken op te tellen. Let op dat bij de berekening van de integraal de 'oppervlaktes' van de rechthoeken onder de y-as als **negatief** geteld worden. Als we de intervallen steeds kleiner maken, wordt de benadering van de integraal steeds preciezer! Daarom komt het goed van pas dat we met een computer werken.

## Specificatie

- Maak een nieuw bestand genaamd `riemann.py`.

- Schrijf een functie `riemann()` die integralen kan berekenen met behulp van de Riemannsom. 

- De functie `riemann()` moet vier argumenten accepteren:

	- `func` een functie waarvan we de integraal gaan bepalen
	- `a` het begin van het gebied
	- `b` het einde van het gebied
	- `N` hoeveel rechthoeken we gebruiken om de integraal te bepalen.

- De functie `riemann()` moet de juiste waarde van de integraal teruggeven als resultaat.



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

Zet deze functies in je eigen programma en zorg dat je onderaan een aantal keer je `riemann()`-functie aanroept, om deze voorbeelden te controleren. Zo kun je `functie1()` van hierboven meegeven aan `riemann()` door aan te roepen:

    riemann(functie1, 0, 1, 10000)

## Hints

- Als je de functie `riemann()` de argumenten `a`, `b` en `N` meegeeft kun je direct de constante $$\Delta x$$ definiëren (het interval $$(a,b)$$ opgedeeld in $$N$$ stukjes). Hoe?

- Het is niet verplicht, maar het is ontzettend handig om een plot te maken van de grafiek zodat je duidelijk ziet welk gebied je aan het integreren bent. Dat kan in een apart programmaatje, maar je zou ook een stukje code op kunnen nemen in de `riemann()`-functie zelf.

- Test je functie altijd eerst op een integraal waarvan je de uitkomst kent. Dit is het geval voor een aantal van de functies die hierboven staan weergegeven. Pas als jouw functie die integralen goed uitrekent kan je met vertrouwen de onbekende nieuwe integraal aanpakken.


## Debuggen

Lijkt het niet te werken? 

- Check "op het oog" met een grafiek of de integraal überhaupt in de buurt komt van wat je mag verwachten.

- Als dat wel goed zit, kan het zijn dat het aantal stappen te klein is om tot een precies genoeg antwoord te komen. Probeer het aantal te verhogen en bekijk ook hoe dit de uitkomsten beïnvloedt.


## Testen

	checkpy riemann
