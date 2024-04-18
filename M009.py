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