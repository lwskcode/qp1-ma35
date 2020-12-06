import random, collections

# Konfiguration des Pseudozufallszahlengenerators
random.seed(1)

# Eingabe: Integer, Ausgabe: korresondierender Monat
class Switch(dict):
    def __getitem__(self, item):
        for key in self.keys():
            if item in key:
                return super().__getitem__(key)
        raise KeyError(item)

# Konfiguration der Liste mit der die Monate zugeordnet werden
switch = Switch(
    {
        range(1, 32): 1,
        range(32, 60): 2,
        range(60, 91): 3,
        range(90, 121): 4,
        range(121, 152): 5,
        range(152, 182): 6,
        range(182, 213): 7,
        range(213, 244): 8,
        range(244, 274): 9,
        range(274, 305): 10,
        range(305, 335): 11,
        range(335, 366): 12
        }
)

# Summe aller Wahrscheinlichkeiten
ratio_total = 0

# Array um die Geburtsmonate der sechs Personen zu speichern
birthdays = []

# Array um zu speichern, ob ein Duplikat vorkommt
has_duplicate = []

# Anzahl der Wiederholungen
r = 100000000

# Ausgabe einer Statusmeldung
print("Running simulation...")

# r Mal Wiederholen
for i in range(r):

    # Sechs Zufallszahlen z von 1-365 generieren
    for j in range(6):

        # z Generieren
        z = random.randint(1, 365)

        # z einem Monat zuornden
        month_of_z = switch[z]

        # Monat zum Array hinzufügen
        birthdays.append(month_of_z)

    # Auflisten, wie oft ein Element (Monat) vorkommt
    c = collections.Counter(birthdays)

    # Für jeden Monat überprüfen, ob ein Duplikat vorliegt
    for i in range (13):
        if i == 0:
            continue;
        if c[i] >= 2:
            # Falls ja, füge einen Eintrag zum Array hinzu
            has_duplicate.append(1)
            break;

    # Array leeren
    birthdays = []

# Ausgabe des Quotienten aus der Anzahl und den Wiederholungen
print((len(has_duplicate))/r)
