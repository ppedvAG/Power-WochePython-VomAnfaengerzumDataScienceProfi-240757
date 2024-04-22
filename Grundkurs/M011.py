# Exceptions
import traceback

print("Test")

# int("ABC")  # Absturz

# try: Führe den Code normal aus, aber mit anschließenden except-Blöcken, können Fehler abgefangen werden
try:
	eingabe = input("Gib eine Zahl ein: ")
	zahl = int(eingabe)  # Absturz
	# Aufgabe: Wenn die Eingabe 0 ist, soll ein Fehler geworfen werden
	if zahl == 0:
		raise ZeroDivisionError()  # raise: Verursache eine Exception, lasse das Programm abstürzen
except ValueError:  # except: Fängt den gegebenen Fehler ab, Programm läuft ohne Absturz weiter
	print("Umwandlung gescheitert")
except TypeError:  # Spezifische Fehlerbehandlung für einen TypeError
	print("Die Eingabe muss ein string oder eine Zahl sein (nicht None)")
except Exception as e:
	# Exception mit as: Fehler einen Namen geben, um auf spezifische Eigenschaften dieses Fehlers zugreifen können
	# z.B.: Name des Fehlers, Nachricht, Typ, Stacktrace, ...
	print("Anderer Fehler")
	print(type(e).__name__)  # EOFError
	print(e)  # EOF when reading a line
	for zeile in traceback.format_exception(e):  # Stacktrace printen
		print(zeile)
except:  # except ohne Error: Allgemeine Fehlerbehandlung (fängt alles)
	print("Anderer Fehler")  # Strg + D: Programm abbrechen (in der Konsole)
else:  # Wird ausgeführt, wenn kein Fehler auftritt
	print("Kein Fehler")
finally:  # Wird ausgeführt bei Erfolg oder Fehler
	print("Wird immer ausgeführt")

print("Test")

# Übung 1
# Erstelle ein Programm, das den User nach zwei Integern fragt
# Falls der User zwei Integer eingibt sollen diese addiert und das Ergebnis in der Konsole ausgegeben werden und das Programm kann beendet werden
# Falls der Benutzer einen falschen Typen eingibt soll das Programm ihn darauf hinweisen, das nur Integer akzeptiert werden und ihn erneut nach den Zahlen fragen
while True:
	try:
		z1 = int(input("int1: "))
		z2 = int(input("int2: "))
		print(z1 + z2)
		break
	except:
		print("Es müssen zwei Zahlen eingegeben werden")


# Übung 2
# Definiere eine beliebige Liste
# Erstelle ein Programm, das den User fragt, das wievielte Element in der Konsole ausgegeben werden soll
# Falls die Zahl außerhalb des Listen-Indexes liegt soll ein Fehler geworfen und der User darauf hingewiesen werden
try:
	list1 = [1, 2, 3]
	index = int(input("Gib eine Stelle ein: "))
	print(list1[index])
except:
	print("Fehler")

# Übung 3
# Füge der beschleunigen Funktion deiner Fahrzeug-Klasse aus Modul 9 eine eigene Exception hinzu:
#    - Sie soll geworfen werden, falls die Höchstgeschwindigkeit überschritten wird

# Übung 4
# Erweitere den Rechner aus Übung 7:
# Erstelle eine Klasse namens Rechner und füge dieser zwei Methoden hinzu: Berechne und InputLesen
# Die Berechne Methode soll drei Parameter empfangen (Zahl 1, Zahl 2, Rechenart) und die Berechnung ausführen
# Die InputLesen Methode soll in einer Endlosschleife vom Benutzer Werte einlesen, bis dieser eine Zahl eingegeben hat
# Prüfe bei dieser Methode mittels try-except, ob die Eingabe des Benutzers valide ist (Exception bei der int(...) Methode abfangen)
# Verwende danach drei mal die InputLesen Methode um die Werte zu erhalten und im Anschluss die Berechne Methode um die Berechnung mit den Werten durchzuführen
class Rechner:
	def InputLesen(self, text: str) -> int:
		while True:
			eingabe = input(text)
			try:
				return int(eingabe)
			except: pass

	def Berechne(self, z1: int, z2: int, operation: int):
		if operation == 1:
			print(f"{z1} + {z2} = {z1 + z2}")
		if operation == 2:
			print(f"{z1} - {z2} = {z1 - z2}")
		if operation == 3:
			print(f"{z1} * {z2} = {z1 * z2}")
		if operation == 4:
			print(f"{z1} / {z2} = {z1 / z2}")

r = Rechner()
while True:
	z1 = r.InputLesen("Gib eine Zahl ein: ")
	z2 = r.InputLesen("Gib eine zweite Zahl ein: ")
	art = r.InputLesen("Gib eine Rechenoperation ein:\n1: Addition\n2: Subtraktion\n3: Multiplikation\n4: Division")
	r.Berechne(z1, z2, art)