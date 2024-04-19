# Klassen und Objekte

# Klasse
# Bauplan für Objekte
# Wird verwendet, um komplexe Datentypen darzustellen
# Klassen haben keine konkreten Werte

class Person:
	"""
	Die Person Klasse
	"""

	# Globale Variable
	# Variablen die auf der Klasse hängen und nicht am Objekt
	# WICHTIG: Hier sollten keine Objektbasierten Variablen angelegt werden
	x = 100

	def __init__(self, vorname = "", nachname = "", alter = 0):
		"""
		__init__

		Startmethode, wird aufgerufen bei Erstellung des Objekts (Konstruktor)

		Bei __init__ können auch Parameter definiert werden, dieser muss der Benutzer übergeben
		"""
		# self: Bezieht sich auf das konkrete Objekt, welches aus der Klasse erzeugt wird
		# Muss bei jeder Methode innerhalb einer Klasse vorhanden sein

		# Objekt Variablen müssen in __init__ definiert werden
		self.vorname = vorname
		self.nachname = nachname
		self.alter = alter

	# Funktion definieren
	# Diese Funktion kann von jedem Objekt verwendet werden
	def sprechen(self, text: str):
		"""
		Gibt die Möglichkeit, beliebigen Text auszugeben
		:param text: Der Text als string
		:return: None (None: Äquivalent zu null aus anderen Sprachen)
		"""
		print(f"{self.vorname} {self.nachname} sagt: {text}")

	def __str__(self):
		return f"Person: {self.vorname}, {self.nachname}, {self.alter}"

	def __gt__(self, other):
		return self.alter > other.alter

# Objekt
# Das Resultat des Bauplans (der Klasse)
# Hier werden konkrete Werte eingetragen
# Von der Klasse können beliebig viele Objekte erstellt werden
p1 = Person()  # Person Objekt erstellen
p1.vorname = "Max"
p1.nachname = "Mustermann"
p1.alter = 30

p1.sprechen("Hallo")  # Objekt benutzen

# Attribute zur Laufzeit hinzufügen
# Ist möglich, sollte vermieden werden
p1.neuesAttribut = "Hallo"
print(p1.neuesAttribut)
del p1.neuesAttribut

# Typvergleiche
# In einer Variable in Python kann alles mögliche enthalten sein
# Mithilfe von type(...) kann der Typ der Variable eingesehen werden
print(type(p1))

if type(p1) == Person:
	print("p1 ist eine Person")

# Alles in Python ist ein Objekt
if type(p1) == object:
	print("p1 ist ein object")

# type(...) == <Typ> prüft genau ob zwei Objekte denselben Typen haben

if isinstance(p1, object):
	print("p1 ist eine Unterklasse von object")

# __str__
# Erzeugt eine Stringrepräsentation des Objekts
# Wird in anderen Sprachen als ToString() bezeichnet
print(p1)  # <__main__.Person object at 0x0000027C5B8E17F0>, Typ + Speicheradresse
print(p1)  # Person: Max, Mustermann, 30

p2 = Person("Max", "Mustermann2", 20)
print(p1 > p2)

print(p1.x)
print(p2.x)
p1.x = 50
print(p1.x)
print(p2.x)

# Übung 1:
# 1. Erstelle eine Fahrzeug-Klasse
# 2. Diese Klasse soll typische Eigenschaften eines Fahrzeuges enthalten: (in __init__)
#     - Fahrzeug-Name
#     - Preis
#     - Maximale Geschwindigkeit
#     - Derzeitige Geschwindigkeit
#     - Motorzustand (An/Aus)
# 3. Die Klasse soll auch folgende Methoden enthalten:
#     - Beschleunigen (Erhöhe bzw Verringere die Derzeitige Geschwindigkeit aber übersteige nicht das Maximum) -> Parameter int (Wieviel soll beschleunigt werden)
#     - StarteMotor (Setze Motorzustand auf True, funktioniert nur wenn das Auto noch nicht gestartet ist)
#     - StoppeMotor (Motor kann nur gestoppt werden, wenn das Auto nicht fährt)
#     - Beschreibung (Gibt alle Informationen über die Klasse wieder)
# 4. Erstelle eine Instanz der Klasse und nutze die Beschreibungs Funktion (Konkrete Werte)

class Fahrzeug:
	def __init__(self, name: str, preis: int, maxV: int):
		self.name = name
		self.preis = preis
		self.maxV = maxV
		self.aktV = 0
		self.motorzustand = False

	def beschleunigen(self, a: int):
		if not self.motorzustand:
			print("Motor aus")
		elif self.aktV + a < 0:
			print("Kann nicht unter 0km/h bremsen")
		elif self.aktV + a < self.maxV:
			self.aktV += a
			print(f"Das Fahrzeug beschleunigt auf {self.aktV}km/h")
		else:
			raise OverflowError()

	def starteMotor(self):
		if not self.motorzustand:
			self.motorzustand = True
		else:
			print("Motor ist bereits an")

	def stoppeMotor(self):
		if self.motorzustand and self.aktV == 0:
			self.motorzustand = False
		else:
			print("Motor ist bereits aus, oder die Geschwindigkeit ist nicht 0")

	def beschreibung(self) -> str:
		return f"Das Fahrzeug {self.name} fährt {self.aktV}km/h und kostet {self.preis}€..."

fzg = Fahrzeug("VW", 20000, 250)
fzg.starteMotor()
fzg.beschleunigen(50)
fzg.stoppeMotor()
fzg.beschleunigen(-50)
fzg.stoppeMotor()
print(fzg.beschreibung())