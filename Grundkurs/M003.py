# Kontrollstrukturen

a = 4
b = 7
if a < b:  # Doppelpunkt am Ende einer Zeile nicht vergessen
	print("a kleiner b")  # Hier auch Einrückungen nicht vergessen
	if a > 5:  # Durch Einrückungen im Code wird Verschachtelung erzeugt
		print("a größer 5")

if a < b:  # Doppelpunkt am Ende einer Zeile nicht vergessen
	print("a kleiner b")
elif a > b:
	print("a größer b")
else:
	print("a gleich b")

# Vergleichsoperatoren
# ==, !=, <> (ungleich)
# <, >=
# >, <=

# Logische Operatoren
# and (&), or (|)
# not (~)
# is
# in

if a < b and a > 5:
	print("Beides ist gültig")

if a < b or a > 5:
	print("a ist kleiner als b oder a ist größer als 5")

meineListe = [1, 2, 3, 4, 5]
if 4 in meineListe:
	print("4 ist in der Liste enthalten")

if 4 not in meineListe:
	print("4 ist nicht in der Liste enthalten")

meinText = "Hallo ich bin ein Text"
if not meinText.isascii():
	print("Dieser Text enthält Unicode Zeichen")

if ~meinText.isascii():
	print("Dieser Text enthält Unicode Zeichen")


# Ternary Operator
# Ermöglicht, große if/else Bäume als Einzeiler darzustellen
if a < b:
	print("a kleiner b")
elif a > b:
	print("a größer b")
else:
	print("a gleich b")

print("a kleiner b") if a < b else print("a größer b") if a > b else print("a gleich b")
# Anweisung -> Bedingung -> else -> ...
print("a kleiner b" if a < b else "a größer b" if a > b else "a gleich b")

# Übung 1
# Wir haben 3 vorgegebene Listen
list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7]
# Finde heraus welche Liste die längste ist (es können auch mehrere Listen die längsten sein)

gesamt = [list1, list2, list3]
gesamt.sort()
maxL = len(gesamt[-1])
if len(list1) == maxL:
	print()
if len(list2) == maxL:
	print()
if len(list3) == maxL:
	print()

# Übung 2
# Nimm die oberen drei Listen und überprüfe ob eine der Listen eine der drei Zahlen enthält: 3, 7, 10
if 3 in gesamt or 7 in gesamt or 10 in gesamt:
	print()

if 3 in list1 or 7 in list1 or 10 in list1:
	print()
if 3 in list2 or 7 in list2 or 10 in list2:
	print()
if 3 in list3 or 7 in list3 or 10 in list3:
	print()