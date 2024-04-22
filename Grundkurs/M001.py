# Ich bin ein Kommentar
# Mehrzeilige Kommentare existieren nicht

# Variablen
# name = Wert

x = 123
print(x)

y = "Text mit doppelten Hochkomma"
z = 'Text mit einzelnen Hochkomma'

# Variablen sind dynamisch typisiert -> Jede Variable passt ihren Typen anhand des Inhalts an

# Typen
# Integer (int)
# Ganze Zahl
zahl = 10
grosseZahl = 21975329816523509821375219658429762318095629843  # Zahlen in Python können beliebig groß sein

print(grosseZahl * 2)

# Float (float)
# Kommazahl
kommazahl = 325.321546
grosseKommazahl = 238759832759.2185713927591327401927409214709

print(grosseKommazahl)

# String (str)
# Text mit beliebiger Länge
s = "Hallo"
s2 = "A"

# Strings können mit einzelnen oder doppelten Hochkomma definiert werden

# Boolean (bool)
# Wahr-/Falschwert
t = True
f = False

# Complex
# Komplexe Zahlen (i)
c = 3 + 5j


# Funktionen
# Funktionen = Methoden
# Code der schon existiert, den wir verwenden können

# print(Wert)
# Schreibt den Wert in die Konsole
print(c)

# String Funktionen
meinText = "Ich bin ein Text"
print(meinText.lower())  # Gibt den Text komplett klein zurück
print(meinText.upper())  # Gibt den Text komplett GROß zurück

print(meinText.islower())  # Prüft, ob der gesamte Text lowercase ist
print(meinText.isupper())  # Prüft, ob der gesamte Text UPPERCASE ist

print(meinText.count("e"))

meinText.capitalize()
meinText.title()

# Strings verbinden
str1 = "Hallo"
str2 = "Welt"
halloWelt = str1 + str2  # Berechnet die Summe (baut die Strings zusammen), verändert aber keine Variablen
print(halloWelt)

str1 += str2  # str1 wird verändert

# Index
# Eine Collection an einer bestimmten Stelle angreifen
# Funktioniert bei str, list, dict, ...
# Startet bei 0
print(halloWelt[0])  # Index wird mit [] und einer Stelle angegeben
print(halloWelt[0:4])  # Bereich auswählen (hier 0 bis 3), Obergrenze exkludiert
print(halloWelt[4])
print(halloWelt[-1])  # Index von der anderen Seite starten lassen (von rechts)
print(halloWelt[-4:-1])  # Index von rechter Seite kann auch mit Bereichen arbeiten
# print(halloWelt[-4:0])  # Wel
print(halloWelt[-4:])  # Bei einem Bereich kann auch die Ober-/Untergrenze weggelassen werden
print(halloWelt[:5])  # 0:5
print(halloWelt[:])  # Nimm alles

# len(Objekt)
# Gibt die Länge des Objekts zurück
print(len(halloWelt))  # Anzahl der Zeichen (9)
# print(halloWelt.len)  # Funktioniert nicht


# Arithmetik
# +, -, *, /
# %: Modulo (Rest einer Division)
# **: Potenzierungsoperator
# //: Ganzzahldivision

zahl1 = 5
zahl2 = 8
print(zahl1 + zahl2)  # Zahlen werden nicht verändert, bleiben gleich

zahl1 += zahl2  # Hier wird zahl1 verändert

# Jeder Operator kann mit = kombiniert werden
zahl1 -= 3
zahl1 %= 2
zahl1 **= 2
zahl1 //= 2

# Arithmetik mit Strings
print(meinText + "10")
print(meinText * 10)