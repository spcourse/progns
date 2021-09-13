# Nulpunten

Schrijf een **programma** dat de nulpunten berekent van de polynoom $$f(x)=x^2+2x-10$$.

    # python nulpunten.py
    De nulpunten zijn -4.32 en 2.32

![](PolynoomAnalyse.png)

Je **programma** moet gebruik maken van een zelfgeschreven **functie** `nulpunten` die de nulpunten berekent.


## Specificatie

- Noem je programma `nulpunten.py`.

- Maak eerst een functie `nulpunten(a, b, c)` die als taak heeft de nulpunten van de polynoom $$f(x)=ax^2+bx+c$$ te berekenen.

    - Er zijn twee mogelijkheden voor het resultaat van de functie:

        - een lege lijst `[]` als er geen nulpunten zijn
        - een lijst met twee elementen `[n1, n2]` waarin `n1` en `n2` de nulpunten van de polynoom zijn

- Schrijf dan de rest van het programma om de resultaten netjes te presenteren:

    - Roep de functie `nulpunten` aan voor de polynoom $$f(x)=x^2+2x-10$$ en sla het resultaat op in een variabele:

            resultaat = nulpunten(1, 2, -10)

    - Print de uitkomst in nette bewoordingen, en print de volgende uitkomst als er geen nulpunten zijn:

        Deze functie heeft geen nulpunten.

    - Plot sowieso de functie, en geef de nulpunten uit de berekening duidelijk aan in de grafiek.


## Hint

- Bereken de nulpunten met behulp van de $$abc$$-formule.


## Testen

Als je hier `checkpy` gebruikt, dan wordt niet meer getest of je programma de juiste uitvoer geeft, maar of de functie `nulpunten()` het juiste resultaat geeft.

    checkpy nulpunten.py

(Werkt het niet? Update dan nog eens met `checkpy -u`.)
