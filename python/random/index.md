# Random getallen

Een zeer handige bouwsteen in een computer-programma is het *random* getal. In de bibliotheek `random` zit een functie `random()` die een random getal produceert tussen 0 en 1. In Python gebruik je de functie als volgt:

    import random
    x = random.random()
    print(x)

Elke keer dat je de functie aanroept zal het een nieuw getal opleveren. Tien random getallen achter elkaar doe je dus als volgt:

    import random
    for i in range(0, 10):
        getal = random.random()
        print(getal)

> Probeer bovenstaande programma's zelf ook even uit! Pas wel op dat je hiervoor niet een bestand `random.py` maakt. In dat geval zal `import random` proberen jouw eigen bestand te importeren, en dat gaat niet werken.

## Bouwen met bouwstenen

Zodra je een bouwsteen hebt, kun je met behulp van logica en wiskundige manipulaties hier zelf andere objecten van bouwen. Als je weet dat de functie `random.random()` een getal tussen 0 en 1 produceert dan kun je een transformatie verzinnen waardoor we een getal tussen bijvoorbeeld 0 en 3 krijgen.

Voorbeeld: tien random getallen tussen 0 en 3

    import random
    for i in range(10):
        getal_01 = random.random()
        getal_03 = 3 * getal_01
        print(getal_03)

## Een eigen functie

Schrijf als oefening een functie `random_range()` die een getal genereert tussen *a* en *b* waarbij je de waardes van a en b zelf kunt kiezen. Het moet zo werken als hieronder.

    import random

    def random_range(a, b):
        getal_ab = <hier jouw code>
        return getal_ab

    minimum = 2
    maximum = 5
    for i in range(10):
        getal = random_range(minimum, maximum)
        print(getal)

Test je programma uit door het te runnen, en check of elk getal in het juiste bereik zit.
