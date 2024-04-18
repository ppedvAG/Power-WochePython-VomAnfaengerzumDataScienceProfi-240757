# Input/Output
import json

# print(...)

# input(string): Wartet auf den Benutzer, dass dieser eine Eingabe macht
# Der String-Parameter wird dem Benutzer präsentiert
# name = input("Gib deinen Namen ein: ")
# print(f"Hallo {name}")
#
# alter = int(input("Gib dein Alter ein: "))  # Durch Casting andere Typen erzeugen
# print(f"Du bist {alter} Jahre alt")

# Escape-Sequenzen
# Untippbare Zeichen in einen String einbauen
# \n, \r: Zeilenumbruch
# \t: Tabulator
# \', \", \\
# print(''')  # Einzelnes Hochkomma muss Escaped werden
print('\'')

print('Das ist \n ein Umbruch')
# print('Das ist \r ein Umbruch')

# open
# Ermöglicht, Interaktion mit Dateien (Schreiben und Lesen)
file = open("Test\\Test.txt", "w")
file.writelines("Test1\n")
file.writelines("Test2\n")
file.writelines("Test3\n")
file.flush()  # Schreibe den Inhalt des Buffers in die unterliegende Datei
file.close()  # Streams sollten immer geschlossen werden

readFile = open("Test\\Test.txt", "r")
lines = readFile.readlines()  # Liest das gesamte File ein, jede Zeile wird zu einem Listenelement
print(lines)

# with-Statement
# Öffnet das File, und schließt es am Ende des Blocks automatisch
with open("Test\\Test.txt", "w") as datei:  # Name des Files steht hinter as
	datei.writelines("Test2\n")
# Hier wird automatisch Close gemacht

# raw string (r-string)
# Ein String, welcher Escape Sequenzen ignoriert
# pfad = 'C:\Users\lk3\source\repos\Python_Grundkurs_2024_04_15\venv\Scripts'
rPfad = r'C:\Users\lk3\source\repos\Python_Grundkurs_2024_04_15\venv\Scripts'

# os, os.path Pakete
# Verschiedene Operationen die mit der Umgebung zusammenhängen
import os
import os.path
if os.path.exists("Test\\Test.txt"):
	print("File existiert bereits")

fullPath = os.path.join("Test", "Test.txt")  # Baut Pfade betriebssystemunabhängig zusammen
print(fullPath)

# Json
testList = ["A", "B", "C"]

meinAuto = {
	"Marke": "Audi",
	"Modell": "A3",
	"Baujahr": 2019
}

# dump, dumps: Erzeugt Json
# load, loads: Interpretiert Json zu Objekten
# Funktionen ohne s schreiben direkt in eine Datei
# Funktionen mit s schreiben in eine Variable
print(json.dumps(testList))
jsonStr = json.dumps(meinAuto)

print(json.loads(jsonStr))

# Übung 1:
# Funktion die dem User die Möglichkeiten (w, r, a) gibt
# User soll eine davon auswählen über input()
# Wenn der User keine valide Möglichkeit eingibt, soll die Eingabe wiederholt werden
# Danach soll einfach das File geöffnet werden
# Bonus: Frage den Benutzer nach dem File, welches geöffnet werden soll
def fileLesenSchreiben():
	while True:
		eingabe = input("Wähle zwischen w, r und a aus:")
		if eingabe not in ["w", "r", "a"]:
			continue

		while True:
			pfad = input("Gib einen Pfad ein")
			if not os.path.exists(pfad) and eingabe == "r":
				continue
			else:
				break

		with open(pfad, eingabe) as file:
			pass

# Übung 2:
# Erstelle ein Programm, das zwei Integer oder Floats abfragt
# Gib dem Nutzer die Möglichkeit per Tastendruck zwischen Addition, Subtraktion, Multiplikation und Division zu wählen.
# -> Zahl zwischen 1 und 4 -> Rechenoperation auswählen
# Bei Ungültiger Eingabe soll der Benutzer erneut nach seiner Entscheidung gefragt werden.
# Lasse das Ergebnis inklusive der Berechnung in der Konsole ausgeben
# Frage nach Ende der Operation ob der Benutzer eine neue Berechnung durchführen will
while True:
	z1 = input("Gib eine Zahl ein: ")
	while True:
		if not z1.isnumeric():
			z1 = input("Gib eine Zahl ein: ")
		else:
			break

	z2 = input("Gib eine Zahl ein: ")
	while True:
		if not z2.isnumeric():
			z2 = input("Gib eine Zahl ein: ")
		else:
			break

	operation = input("Gib eine Rechenoperation ein:\n1: Addition\n2: Subtraktion\n3: Multiplikation\n4: Division")
	while True:
		if not operation.isnumeric():
			operation = input("Gib eine Zahl ein: ")
		else:
			break

	z1 = int(z1)
	z2 = int(z2)
	operation = int(operation)

	if operation == 1:
		print(f"{z1} + {z2} = {z1 + z2}")
	if operation == 2:
		print(f"{z1} - {z2} = {z1 - z2}")
	if operation == 3:
		print(f"{z1} * {z2} = {z1 * z2}")
	if operation == 4:
		print(f"{z1} / {z2} = {z1 / z2}")

	# Mit switch
	# match operation:
	# 	case 1:
	# 		print(f"{z1} + {z2} = {z1 + z2}")
	# 	case 2:
	# 		print(f"{z1} - {z2} = {z1 - z2}")
	# 	case 3:
	# 		print(f"{z1} * {z2} = {z1 * z2}")
	# 	case 4:
	# 		print(f"{z1} / {z2} = {z1 / z2}")

	restart = input("Wiederholen? (Y): ")
	if restart.lower() != "y":
		break