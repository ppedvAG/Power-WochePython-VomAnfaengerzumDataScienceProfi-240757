# Vererbung

# Ermöglicht, Oberklassen zu definieren die als Basis für beliebig viele Unterklassen existiert
# Diese Oberklasse gibt ihren Inhalt (Felder, Methoden) nach unten weiter
# -> Die Unterklassen sind die Oberklasse

# Beispiel:
# Oberklasse: Fahrzeug
# Unterklassen: PKW, LKW, Schiff, Flugzeug, Motorrad, ...
# Fahrzeug-Felder: Name, Preis, MaxV, AktV, MotorZustand
# Fahrzeug-Methoden: __init__, StarteMotor, StoppeMotor, Beschleunige, Beschreibung
# Diese Felder & Methoden werden alle nach unten weitergegeben

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
		# Mit type(self) auf den Typen des Objektes selbst zugreifen
		# Pro Unterklasse der korrekte Name (PKW, LKW, Schiff, ...)
		return f"{type(self).__name__} {self.name} fährt {self.aktV}km/h und kostet {self.preis}€..."

	def __str__(self):
		return f"{self.name}, {self.preis}, {self.maxV}"

# In der Klammer die Oberklasse(n) definieren
# "PKW ist ein Fahrzeug"
# PKW ist eine Spezifizierung von Fahrzeug -> Wir können hier weitere Felder/Methoden hinzufügen, die nicht allgemein für alle Fahrzeug gelten sollen
# z.B. AnzahlSitze
class PKW(Fahrzeug):
	# Hier wird die __init__ Methode von Fahrzeug überschrieben -> expliziter Aufruf der __init__ Methode von oben
	def __init__(self, name: str, preis: int, maxV: int, anzSitze: int):
		super().__init__(name, preis, maxV)  # super(): Greife in die Oberklasse
		self.anzSitze = anzSitze

	# Aufgabe: Bei beschreibung() auch die Sitze ausgeben
	def beschreibung(self) -> str:
		# Mit super() den Text von Fahrzeug holen und einen Text anhängen
		return super().beschreibung() + f" Es hat {self.anzSitze} Sitzplätze."

class LKW(Fahrzeug):
	def __init__(self, name: str, preis: int, maxV: int, laderaum: int):
		super().__init__(name, preis, maxV)
		self.laderaum = laderaum
		self.aktLadung = 0

	# Eigene Funktionen nur für LKW
	def beladen(self, ladung: int):
		if ladung < 0:
			return
		if self.aktLadung + ladung > self.laderaum:
			return
		self.aktLadung += ladung

	def entladen(self, ladung: int):
		self.aktLadung -= ladung
		if self.aktLadung < 0:
			self.aktLadung = 0

	def beschreibung(self) -> str:
		return super().beschreibung() + f" Es hat {self.laderaum}m³ Laderaum beladen mit {self.aktLadung}m³ Ladung."


class Schiff(Fahrzeug):
	pass  # pass: Mach nichts, wird verwendet für leere Klassen/Methoden

# Die PKW Klasse hat __init__ vererbt bekommen, und muss daher auch Werte bei der Erstellung angeben
pkw = PKW("VW", 20000, 250, 5)
pkw.starteMotor()  # Methoden wurden auch vererbt
pkw.stoppeMotor()
print(pkw.beschreibung())

lkw = LKW("XYZ", 100000, 120, 10)
lkw.beladen(5)
print(lkw.beschreibung())

print(pkw)
print(lkw)