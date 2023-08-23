# Spiraal

Schrijf een programma dat een spiraliserende stip animeert met behulp van Matplotlib. De stip draait met een bepaalde hoeksnelheid rond en met elke stap in de tijd verandert niet alleen de hoek, maar wordt ook de straal steeds kleiner tot hij uiteindelijk precies in het midden stilstaat:

![](../assets/AnimationInspiral.gif)

## Specificatie

Schrijf een programma `spiraal.py` waarin de stip geanimeerd wordt zoals hierboven beschreven.

## Hints

Poolcoördinaten: een punt kan worden beschreven middels de coördinaten $$(x,y)$$, maar je
kunt ook twee andere variabelen gebruiken ($$\alpha$$, R), waarbij $$\alpha$$ de
hoek is met de positieve $$x$$-as en $$R$$ de afstand tot de oorsprong. De
variabelen kunnen in elkaar omgeschreven worden zoals in de volgende grafiek is
aangegeven.

![](../assets/UitlegPolarCoordinates.png)

Details voor de animatie:

- De hoek $$\alpha$$ varieert van $$0$$ tot $$20$$ radialen in stappen van $$0.1$$ (hoeveel radialen is één rondje?)
- De straal $$R$$ hangt af van $$\alpha$$, namelijk $$R=10-0.5\alpha$$
- De y-as en x-as kun je even lang maken (als ze dat niet al zijn) met `gca().set_aspect()`. Dit is niet verplicht, maar als je het leuk vindt, zoek dan online hoe dit werkt.

## Testen

Dit programma is helemaal visueel en kan niet worden getest met `checkpy`. Je moet het laten aftekenen tijdens het practicum. Mocht je nu direct doorgaan met de volgende opdracht (student) wacht dan met aftekenen tot je deze ook gedaan hebt, dan kun je ze zo direct samen laten aftekenen.
