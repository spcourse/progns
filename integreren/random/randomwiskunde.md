# Feitje over de som van random getallen 

Schrijf een functie die het gemiddeld aantal random getallen (uniform verdeeld tussen 0 en 1) bepaalt die je moet trekken om te zorgen dat de som van die getallen groter is dan 1.00.

Gebruik de volgende strategie:

  - Genereer telkens verschillende random getallen en stop wanneer de som ervan groter is dan 1. (Bv.: 0.1, 0.62, 0.45. In dit geval waren
    er drie worpen nodig.) Gebruik hiervoor de `while()`-constructie
  
  - Doe dit bovenstaande een groot aantal keer (N = 1 miljoen)

  - Bepaal het gemiddeld aantal benodigde worpen en print dat naar het scherm
  
### Specificatie

- Maak een nieuw bestand genaamd `randomwiskunde.py`.

- Definieer in dit bestand een functie `randomwiskunde()` die geen parameters accepteert en die het gemiddeld aantal random getallen bepaalt dat getrokken moet zorgen om te zorgen dat de som ervan groter is dan 1.

- De output op het scherm (op 4 decimalen nauwkeurig) is als volgt:

	   Het gemiddeld aantal worpen (op basis van 1 miljoen trials) is: x.xxxx 


## Hints

- Denk weer goed na of het nuttig is om informatie bij te houden in variabelen. Als je die variabelen bijhoudt en/of 'reset' (terug op hun startwaarde zet), denk dan goed na in (of buiten) welke loop je dat wil doen. Print-statements kunnen helpen om te achterhalen of dit goed gaat.

### Testen

	checkpy randomwiskunde
	


#### bron: `@fermatslibrary`