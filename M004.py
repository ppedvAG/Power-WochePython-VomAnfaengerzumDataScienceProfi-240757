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

# Übung 1:
# FizzBuzz
# 1. Schleife schreiben, die von 1 bis inklusive 100 hochzählt
# 2. Wir müssen in der Schleife jede Zahl auf ihre Teilbarkeit prüfen:
# Falls sie durch 3 teilbar ist, soll in der Konsole "Fizz" ausgegeben werden
# Falls sie durch 5 teilbar ist, soll in der Konsole "Buzz" ausgegeben werden
# Falls sie sowohl durch 3 als auch 5 teilbar ist, soll in der Konsole "FizzBuzz" ausgegeben werden
# Falls sie weder durch 3 noch 5 teilbar ist, soll die Zahl selbst in der Konsole ausgegeben werden
# 1, 2, Fizz, 4, Buzz, ..., 14, FizzBuzz

# Übung 2:
# Schreibe eine Schleife die dir alle Zahlen von 1 bis 200 zur Verfügung stellt
# Lass dir jede Zahl erst in der kardinalen und dann daneben in der ordinalen Schreibweise darstellen
# Der Modulo Operator ist hier sehr nützlich
# Zahl + Endung 'st', 'nd', 'rd' oder 'th'
# 1st, 2nd, 3rd, 4th, ..., 21st, 22nd, 23rd, 24th
# Bonus: Berücksichtige alle Zahlen die mit 11, 12 oder 13 enden

# Übung 3:
# Stoppuhr
# Bevor die Minute hochtickt, müssen die Sekunden einmal eine vollkommene Umdrehung hinter sich gebracht haben
# time.sleep(Float) Funktion hier nützlich

# Übung 4:
# Erstelle eine Schleife die das kleine Einmaleins von 1 bis 10 berechnet, und jeden einzelnen
# Schritt in der Konsole ausgibt
# "1 x 1 = 1"
# "1 x 2 = 2"
# ...
# "5 x 5 = 25"
# ...
# "7 x 4 = 28"
# ...
# "10 x 10 = 100"