# Schleifen

# Führen Code mehrmals aus
# Laufen bis die gegebene Bedingung nicht mehr True ist

# while-Schleife
# Hat eine Bedingung, und läuft solange die Bedingung True ist

a = 0
b = 10

# Hier geht der Code im Kreis
while a < b:
	print(a)  # Einrückungen beachten
	a += 1  # Hier wird a < b nochmal geprüft, und die Schleife wird neu gestartet, wenn a < b
print("Nach der Schleife")

# Endlosschleife, läuft für immer
while True:  # True ist eine Bedingung die immer True ist
	a += 1
	if a > 500:
		break  # Hier wird die Schleife beendet, wenn a > 500 ist

	if a % 2 == 0:
		continue  # Wenn a durch 2 teilbar ist, wird print(a) übersprungen

	print(a)
print("Nach der Schleife")

# break und continue
# Schleifensteuerungsbefehle
# break: Beendet die Schleife
# continue: Führe den Code nach continue nicht mehr aus, und springe zum Kopf zurück



# for-Schleife
# Führt auch Code mehrmals aus, basiert aber auf einer Liste
# Wird als foreach bezeichnet

liste = [1, 2, 3, 4, 5]
for element in liste:  # "Für jedes Element in der Liste"
	print(element)

print("----------")

for element in liste:  # "Für jedes Element in der Liste"
	if element % 2 == 0:
		continue
	print(element)

print("----------")

# for-Schleife repräsentiert als while-Schleife
x = 0
while x < len(liste):
	print(liste[x])
	x += 1

# for-Schleife in Kombination mit Range
print(list(range(-10, 10)))

for zahl in range(-10, 10):  # "Konventielle for-Schleife"
	print(zahl)

# String iterieren
for zeichen in "Das ist ein Text":
	print(zeichen)

# Mit for-Schleife das Dictionary durchgehen
meinAuto = {
	"Marke": "Audi",
	"Modell": "A3",
	"Baujahr": 2019
}

# Hier kann eine Schleife angelegt werden, welche zwei Laufvariablen hat
for k, v in meinAuto.items():
	print(k)
	print(v)

# else bei einer Schleife
# Führt ein Stück Code aus, wenn die Schleife erfolgreich beendet wurde
# Erfolgreich: kein break, return, Fehler

for element in liste:  # "Für jedes Element in der Liste"
	print(element)
else:
	print("Schleife erfolgreich beendet")

c = 0
while c < b:
	print(c)
	c += 1
else:
	print("Schleife erfolgreich beendet")


# fstring
# Formatted String
# Ermöglicht, Code in einen String einzubauen

# Problem: int und str kann nicht addiert werden
# y = "Hallo " + 12

# Lösung: int zu str konvertieren
# str(...)
y = "Hallo " + str(12)
print(y)

# Einfacher mit fstring
z = f"Hallo {12}"  # WICHTIG: Nicht das f vergessen
print(z)

# fstring innerhalb einer Schleife
for i in range(10):
	print("Die Zahl ist " + str(i))
	print(f"Die Zahl ist {i}")

	print("Die Zahl^2 ist " + str(i ** 2))
	print(f"Die Zahl^2 ist {i ** 2}")

	print(str(i) + "^2=" + str(i ** 2))
	print(f"{i}^2={i ** 2}")

# Verschachtelte Schleifen
# Schleifen innerhalb von anderen Schleifen
# Die innere Schleife wird einmal komplett ausgeführt, bevor die äußere Schleife um 1 weiter geht

for i in range(10):  # Die äußere Schleife wird weniger oft ausgeführt
	for j in range(10):  # Die innere Schleife wird oft ausgeführt
		print(i * j)
	print("---------------")




