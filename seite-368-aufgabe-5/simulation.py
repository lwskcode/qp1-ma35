from random import seed, random

# Konfiguration des Pseudozufallszahlengenerators
seed(1)

# Summe aller Wahrscheinlichkeiten
ratio_total = 0

# Array um die Zustände der Zehn Personen zu speichern, 0 = nicht infiziert, 1 = infiziert
infected = []

# Anzahl der Wiederholungen
r = 100000000

#Ausgabe einer Statusmeldung
print("Running simulation...")

# r Mal Wiederholen
for i in range (r):

    # Zehn Zufallszahlen z von 0-1 generieren
    for j in range(10):

        # z Generieren
    	z = random()

    	# 45% Wahrscheinlichkeit einer Infektion
    	if z <= 0.45:
    	    # Hinzufügen zum Array
    	    infected.append(1)
    	else:
    	    # Hinzufügen zum Array
    	    infected.append(0)

    # Berechnen des Verhältnis von infizierten zur Gesamtmannschaft
    ratio = (infected.count(1)/10)

    # Feststellen, ob mehr als die Hälfte infiziert ist
    if ratio >= 0.6:
        # Falls ja, Hinzufügen zur Summe aller Wahrscheinlichkeiten
        ratio_total = (ratio_total + ratio)

    # Array leeren
    infected = []

# Ausgabe des Quotienten aus der SUmme und den Wiederholungen
print(ratio_total/r)
