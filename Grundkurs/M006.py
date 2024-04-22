# Funktionen
# Code wiederverwenden
# Funktionen sind erst verfügbar, wenn das Skript an der Stelle ausgeführt wird

def hallo():
	print("Hallo Welt")

hallo()

# Funktion mit Parameter
def hallo(name):
	print(f"Hallo {name}")

hallo("Lukas")
hallo(123)  # In Python kann nicht erzwungen werden, was ein Parameter sein muss

# Wie können wir das verhindern?
# 2 Möglichkeiten

# Typvergleich
def halloPlus(name):
	if type(name) == str:
		print(f"Hallo {name}")
	else:
		print("name ist kein string")

halloPlus("Lukas")
halloPlus(123)

# Typ "empfehlen"
def halloPlus2(name: str):
	print(f"Hallo {name}")

halloPlus2("Lukas")
halloPlus2([1, 2, 3])  # : str ist nur eine Empfehlung, User kann trotzdem beliebige Werte eintragen

x: str = "ABC"  # Funktioniert auch bei Variablen

# Rückgabewerte
# Funktionen können auch Ergebnisse haben
# Werte werden mittels dem return Keyword zurückgegeben
def addiere(x: int, y: int):
	return x + y

summe = addiere(4, 5)  # Hier kann das Ergebnis der Funktion in eine Variable geschrieben werden

def dividiere(x: int, y: int) -> float:
	return x / y

quotient = dividiere(4, 9)


# Keyword Arguments
def printPerson(vorname, nachname, alter, adresse):
	print("...")

printPerson(alter=10, adresse="Zuhause", vorname="Max", nachname="Mustermann") # Hier können die Parameter in einer beliebigen Reihenfolge angegeben werden

# Default Arguments
# Ermöglicht, einen Standardwert für Parameter zu setzen
def printPerson(vorname = "", nachname = "", alter = 0, adresse = ""):
	print("...")

printPerson(alter=22, vorname="Max")
printPerson(vorname="Max")
printPerson(adresse="Zuhause")


# Arbitrary Arguments
# Ermöglicht, einen Parameter zu definieren, welcher beliebig viele Werte empfangen kann
# Dieser Parameter hat einen * vor seinem Namen
def Summe(*numbers):
	summe = 0
	for i in numbers:  # numbers ist ein Tupel
		summe += i
	return summe

Summe(1, 2, 3)
Summe(1, 2, 3, 4, 5)
Summe(1)
Summe()
# Summe("Hallo", "ich", "bin", "ein", "Text")

def Summe(*numbers: int):
	pass  # pass: Macht nichts, wird verwendet als Platzhalter


# Arbitrary Keyword Arguments
# Ermöglicht, einen Parameter zu definieren, welcher beliebig viele BENANNTE Werte empfangen kann
# Dieser Parameter hat einen ** vor seinem Namen
def printTeilnehmer(**tn):
	for key, value in tn.items():
		print(f"Der Teilnehmer {key} heißt {value}")

printTeilnehmer(T1 = "", T2 = "", Trainer = "")


# Wie kann ich eine Liste oder ein Dict in einer der beiden Funktion einfügen?
zahlen = [1, 2, 3, 4, 5, 6, 7, 8]
# Summe(zahlen)  # Nicht möglich

meinAuto = {
	"Marke": "Audi",
	"Modell": "A3",
	"Baujahr": 2019
}

# printTeilnehmer(meinAuto)  # Nicht möglich

# Unpacking Operator
# Mit * oder ** können Listen oder Dictionaries in ihre Einzelteile zerlegt werden
# Dadurch können sie in diese Funktion eingefügt werden
Summe(*zahlen)
printTeilnehmer(**meinAuto)

a, b, c, *d = zahlen
print(a)
print(b)
print(c)
print(d)

# Dict zerlegen
m, *n = meinAuto.items()
print(m)
print(n)

# Übung 1:
# Wir wollen eine Funktion erstellen, die beliebig viele Zahlen als Parameter erhalten kann
# Und uns die größte dieser Zahlen zurückgibt
def max(*zahlen):
	m = zahlen[0]
	for z in zahlen:
		if z > m:
			m = z
	return m

print(max(-1, -2, -3))

# Übung 2:
# Wir wollen eine Funktion erstellen, die einen String als Parameter erhält
# Die Funktion soll dann in der Konsole ausgeben, aus wie vielen Klein- und Großbuchstaben der String besteht
# Die Funktion soll zusätzlich zählen wie viele Sonderzeichen (Nummern inkludiert) enthalten sind und das ebenfalls ausgeben
# Sonderzeichen: 4 | Groß: 3 | Klein: 12
def countCase(text: str):
	g, k, s = 0, 0, 0
	for zeichen in text:
		if zeichen.islower():
			k += 1
		elif zeichen.isupper():
			g += 1
		else:
			s += 1
	print(f'Großbuchstaben: {g}, Kleinbuchstaben: {k}, Sonderzeichen: {s}')

countCase("Hallo ich bin ein Text")

# Übung 3
# Schreibe eine Funktion, die eine Liste von Strings als Parameter empfängt
# Diese Funktion soll die Strings als eine Aufzählung zusammenbauen und am Ende zurück geben
# Dabei sollen alle Teilnehmer mit einem Komma und der letzte Teilnehmer mit einem "und" angehängt werden
# Beispiele:
# Parameter: []
# Keine Parameter angegeben
# Parameter: ["Teilnehmer"]
# Teilnehmer
# Parameter: ["Teilnehmer1", "Teilnehmer2"]
# Teilnehmer1 und Teilnehmer2
# Parameter: ["Teilnehmer1", "Teilnehmer2", "Teilnehmer3", "Teilnehmer4"]
# Teilnehmer1, Teilnehmer2, Teilnehmer3 und Teilnehmer4
def printTeilnehmer(*tn):
	if len(tn) == 0:
		print("Keine Teilnehmer")

	if len(tn) == 1:
		print(tn[0])

	if len(tn) == 2:
		print(f'{tn[0]} und {tn[1]}')

	result = ''
	if len(tn) > 2:
		for i in range(0, len(tn) - 1):
			result += tn[i] + ', '
	print(result.rstrip(', ') + ' und ' + tn[-1])

printTeilnehmer("T1", "T2", "T3", "T4")