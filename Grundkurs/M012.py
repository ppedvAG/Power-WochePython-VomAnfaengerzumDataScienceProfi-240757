# Lambda

# Anonyme Funktionen (d.h. Methoden ohne Kopf -> def), welche nur einmal verwendet werden
# Jede Funktion ist ein Objekt

def Hallo():
	print("Hallo")

func = Hallo  # Methodenzeiger in eine Variable speichern
print(func)

# Kurzform von dem obigen Code ohne Methodendefinition aber mit Lambda
l = lambda: print("Hallo")
print(l)


# Lambda-Expression mit Parametern
def Addiere(x: int, y: int):
	print(x + y)
# ->
a = lambda x, y: print(x + y)

# Verwendung: Parameter bei Funktionen
l()
a(4, 5)

def RunLambda(l):
	l()

RunLambda(l)
RunLambda(lambda: print("Hallo Welt"))

# Praktische Anwendung

# Aufgabenstellung: Erstelle eine Liste von 0 bis 100 und finde alle Zahlen die durch 3 teilbar sind
# Drei Möglichkeiten: normale Schleife, List Comprehension, filter()
bis100 = list(range(0, 100))

durch3Schleife = []
for zahl in bis100:
	if zahl % 3 == 0:
		durch3Schleife.append(zahl)
print(durch3Schleife)

# List Comprehension
durch3LC = [z for z in bis100 if z % 3 == 0]
print(durch3LC)

# filter()
# filter geht die Liste mit einer Schleife durch, und führt bei jedem Element die gegebene Funktion aus
# Jedes Element welches True ist, kommt in die Ergebnismenge
durch3Filter = filter(lambda z: z % 3 == 0, bis100)
print(list(durch3Filter))

# Aufgabenstellung 2: Nimm die Liste von 0 bis 100, und stelle diese in der Form x^2 dar
hoch2Schleife = []
for zahl in bis100:
	hoch2Schleife.append(zahl ** 2)
print(hoch2Schleife)

# LC
hoch2LC = [z ** 2 for z in bis100]
print(hoch2LC)

# map()
# Wandelt jedes Element einer Liste in eine andere Form um
hoch2Map = map(lambda z: z ** 2, bis100)
print(list(hoch2Map))