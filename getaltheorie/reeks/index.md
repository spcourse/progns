# Reeks

Schrijf een programma dat de *langste aaneengesloten reeks niet-priemgetallen* bepaalt onder de 10,000 en daar een korte samenvatting van geeft.

	# python reeks.py
	De langste reeks niet-priemgetallen onder de 10,000 begint op ... en eindigt bij ...
	De reeks is ... lang.
	
Lees goed wat er gevraagd wordt: de begin en eindpunten zijn zelf dus *niet* priemgetallen. Onder het getal 100 moet het antwoord zijn:

	De langste reeks niet-priemgetallen onder de 100 begint op 90 en eindigt bij 96
	De reeks is 7 lang.

De opdracht luidt om de langste reeks te vinden onder het getal 10,000.

## Achtergrond

Bepaal altijd met pen en papier je strategie en ga dus niet gelijk tikken. De 5--10 minuten die je hieraan besteedt verdien je dik terug tijdens het omzetten naar programmacode.

Om het idee van de reeks niet-priemgetallen goed te begrijpen, schrijf je bijvoorbeeld de eerste tien priemgetallen op papier en bekijk steeds de onderlinge afstand: tussen 2 en 3 is het verschil maar één, terwijl het verschil tussen 13 en 17 vier is (wat dus betekent dat er 3 opeenvolgende getallen tussen zitten die niet-priem zijn, namelijk 14, 15 en 16).

## Specificatie

- Maak een programma genaamd `reeks.py` en zorg dat het volgens bovenstaand voorbeeld de juiste informatie uitprint. 

- Zorg dat je programma drie functies definieert:
	1. `priem_of_niet()`, de functie die je schreef in `priemgetal.py`
	2. `alle_priems()`, een functie met één argument, `N`, die alle priemgetallen kleiner `N` vindt en in een lijst zet en *twee* outputs returnt: die lijst en de lengte van die lijst.
	3. `reeks_niet_priem()` een functie met als argument het maximale getal waaronder we de reeks moeten vinden. Deze functie output niets, maar print de informatie over de langste reeks in het format zoals bovenaan deze pagina staat.

- Gebruik in de functie `alle_priems()` de functie `priem_of_niet()` om te bepalen of een getal een priemgetal is. Je mag om de lengte van de lijst (met priemgetallen) te bepalen *niet* de functie `len()` gebruiken. Na deze opdracht mag dat voortaan wel.

- Gebruik in de functie `reeks_niet_priem()` de functie `alle_priems()` om een lijst met priemgetallen onder `N` te vinden. Stap (loop) vervolgens door de lijst priemgetallen heen en bepaal telkens hoe lang de reeks niet-priemgetallen is tussen het huidige en het vorige priemgetal. Houd bij wat de langste reeks is in een aparte variabele.

- Roep de functie `reeks_niet_priem` aan met als argument `10000`. Zorg dat je output er netjes uitziet en dat we als gebruiker iets aan de informatie hebben: print eerst de twee niet-priemgetallen die het begin en eind van de reeks vormen en dan op de volgende regel de lengte van de reeks! Zie weer het voorbeeld bovenaan de opdracht.

## Testen

Loop nu de specificatie bovenaan de opdracht goed door en zorg dat je programma precies zo werkt als daar beschreven is. Test zelf met 100 en met 10,000.

Nu ben je klaar om te testen:

	checkpy reeks
