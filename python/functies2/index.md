# Functies als argumenten

Het kan nuttig zijn om functies mee te geven als een argument aan een andere functie. Dit kan er, in eerste instantie, wat verwarrend uitzien. Neem het volgende voorbeeld:

    def optellen(a, b):
        return a + b

    def vermenigvuldig(a, b):
        return a * b

    def herhaal(mijn_functie, x, y, z):
        totaal = mijn_functie(x, y)
        totaal = mijn_functie(totaal, z)
        return totaal

    opgeteld = herhaal(optellen, 4, 3, 2)
    print(opgeteld)

    vermenigvuldigd = herhaal(vermenigvuldig, 4, 3, 2)
    print(vermenigvuldigd)

Dit geeft de volgende output:

    9
    24

Hier wordt de functie `herhaal()` gebruikt voor twee verschillende doeleindes. In de eerste aanroep worden alle getallen opgeteld. In de tweede aanroep worden ze vermenigvuldigd.

Het verschil in gedrag wordt bepaald door de parameter `mijn_functie`. Deze specificeert een functie de twee keer wordt aangeroepen in `herhaal`. Bij het aanroepen van `herhaal` specificeren we wat `mijn_functie` precies moet zijn. In het eerste geval is dat `optellen`. In het tweede geval `vermenigvuldig`.

In het voorbeeld worden alleen de functies `optellen` en `vermenigvuldig` gebruikt. Maar in principe zou je hier elke functie kunnen meegeven die twee getallen met elkaar combineert. Probeer zelf je eigen functies te definiëren om te gebruiken als input voor `herhaal()`.

Het bovenstaande voorbeeld is een beetje kunstmatig, maar het geeft een volledig sjabloon voor het gebruik van functies als argumenten.
