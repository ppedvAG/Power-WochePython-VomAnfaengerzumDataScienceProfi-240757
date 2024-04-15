# List
# Variable, welche mehrere Werte halten kann
meineListe = []  # Leere Liste anlegen
meineListe = [1, 2, 3, 4, 5]  # Liste mit Standardwerten anlegen

# Index
print(meineListe[1])
print(meineListe[0:3])
print(meineListe[1:4])
print(meineListe[-1])

# list.append(Element)
# Fügt ein Element am Ende der Liste hinzu
meineListe.append("Hallo")
print(meineListe)

# Typen innerhalb von Collections können gemischt sein
meineListe.append(2.5)

# list.extend(...)
liste2 = [1, 2, 3]
meineListe.extend(liste2)  # Packt den Inhalt von liste2 aus und fügt diesen in meineListe ein
meineListe.append(liste2)  # Hier wird die Liste verschachtelt
print(meineListe)

meineListe += liste2  # Selbiges wie extend, Liste wird zerlegt
print(meineListe)

# list.remove(Element)
meineListe.remove([1, 2, 3])  # Entfernt das Erste Vorkommen des Elements
print(meineListe)

# Länge der Liste
print(len(meineListe))

# Liste sortieren
# meineListe.sort()  # Liste kann nicht sortiert werden, weil nicht alle Typen gleich sind
meineListe.remove("Hallo")
meineListe.remove(2.5)
meineListe.sort()
print(meineListe)


# Tupel
# Funktioniert wie List, kann aber nicht bearbeitet werden
# Wird mit normalen Klammern ( ) definiert
meinTupel = (1, 2, 3, 4)
print(meinTupel)  # Runde Klammern im Output definieren ein Tupel

print(meinTupel[0])
# meinTupel[0] = 10  # Tuples don't support item assignment

# Tupel über Umweg ändern
temp = list(meinTupel)  # Tupel zu Liste konvertieren mit dem List Befehl
temp[0] = 10
meinTupel = tuple(temp)
print(meinTupel)

# Unpacking
# Operation die ermöglicht, eine Liste in ihre Einzelteile zu zerlegen
a, b, c, d = meinTupel  # Hier wird das Tupel zu 4 einzelnen Variablen zerlegt
print(a)
print(b)
print(c)
print(d)

# e, f, g, h = [1, 2, 3, 4]
e, f, g, h = "Text"
print(e, f, g, h)


# Range
# Erzeugt einen Bereich von X bis Y mit einer optionalen Schrittgröße
range(100)  # Bis 100 startend bei 0
range(10, 100)
range(10, 100, 2)  # Optionale Schrittgröße 2

print(range(10, 100))  # Range ist ein Generator, hier werden keine Zahlen erzeugt
print(list(range(10, 100)))  # List befiehlt dem Generator seine Elemente zu erzeugen

print(range(1_000_000_000))  # Dauer: 0s, weil nur Generator
# list(range(1_000_000_000))  # Dauer: Lang, weil Generator ausgeführt wird


# Set
# Wie List, aber filtert Duplikate
meinSet = {1, 2, 3, 4, 5}
print(meinSet)  # Set wird mit { } ausgegeben

meinSet.add(6)
print(meinSet)

meinSet.add(6)  # Nichts passiert
print(meinSet)

# Duplikate entfernen
print(set(meineListe))


# Dictionary
# Liste von Schlüssel-Wert Paaren
meinAuto = {
	"Marke": "Audi",
	"Modell": "A3",
	"Baujahr": 2019
}

print(meinAuto)

# Jahr entnehmen mit einem String-basierten Index
print(meinAuto["Baujahr"])

# Schlüssel anpassen
meinAuto["Marke"] = "BMW"
meinAuto["KM"] = 10000
print(meinAuto)

# Elemente aus einem Dictionary auflisten
print(meinAuto.items())  # Liste von Tupeln
print(meinAuto.keys())
print(meinAuto.values())


# Konvertierungen
# Typen einer Variable in einen anderen Typen konvertieren
# z.B. Kommazahl zu ganzer Zahl
k = int(2.5)
s = str(2.5)
i = int("4")
t = (1, 2, 3)
print(list(t))  # Tupel zu List konvertieren
print(tuple(range(0, 10)))
print(list("Ich bin ein Text"))