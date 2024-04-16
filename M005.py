# List Comprehension
# Gibt die Möglichkeit, schnell und einfach eine Liste zu erzeugen

# Syntax: [<Der Wert der in die Liste kommt> for <Schleifenvariable> in <Liste> (optional) if ...]

# Ohne List Comprehension
zahlen = []
for i in range(0, 100):
	zahlen.append(i)
print(zahlen)

# Mit List Comprehension
zahlenLC = [i for i in range(0, 100)]  # Hier in die Klammer die Schleife einsetzen, dann mit dem Cursor an den Anfang zurück springen und die Schleifenvariable verwenden
print(zahlenLC)

# Bei einer List Comprehension können auch Bedingungen eingesetzt werden
# Alle geraden Zahlen von 0 bis 100
zahlenGeradeLC = [i for i in range(0, 100) if i % 2 == 0]

zahlenGerade = []
for i in range(0, 100):
	if i % 2 == 0:
		zahlenGerade.append(i)

# Beim Einfügen der Werte in die Liste können die Werte vorher auch bearbeitet werden
iHochI = []
for i in range(1, 11):
	iHochI.append(i ** i)
print(iHochI)

iHochILC = [i ** i for i in range(1, 11)]
print(iHochILC)

# Zahl + Potenz anzeigen
iHochIAusgabeLC = [f"{i}^{i}={i**i}" for i in range(1, 11)]  # Ergebnis: Liste von strings
print(iHochIAusgabeLC)

# Verschachtelte Schleife in LC
einMalEins = [i * j for i in range(1, 11) for j in range(1, 11)]
print(einMalEins)

einMalEinsOutput = [f"{i} x {j} = {i * j}" for i in range(1, 11) for j in range(1, 11)]
print(einMalEinsOutput)

# Ternary Operator in LC
fizzBuzz = ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else  # else wegen Ternary Operator
            "Fizz" if i % 3 == 0 else
            "Buzz" if i % 5 == 0 else
            i
            for i in range(1, 100)]
print(fizzBuzz)

# str.split(...)
text = "Das ist ein Text und dieser Text hat jetzt ein paar mehr Begriffe"
liste = text.split(" ")  # Anhand eines Trennzeichens den string in eine Liste zerteilen
print(liste)

# Aufgabe: Alle Wörter mit einem e finden
print([wort for wort in liste if wort.lower().count("e") > 0])

# Alle Großbuchstaben finden
print([buchstabe for buchstabe in text if buchstabe.isupper()])

# Übung 1
# Schreibe eine List-Comprehension die nur Zahlen aus einer Range von 1 bis inklusive 30 in die neue Liste packt, falls die Zahl durch 6 teilbar ist
# Bevor die Zahl in die neue Liste gepackt wird, soll sie um 12 erhöht werden

# Übung 2
# Schreibe eine List-Comprehension die aus einem Text alle Kleinbuchstaben nimmt und Groß in die Liste schreibt

# Übung 3
# Schreibe eine List-Comprehension die aus einem Text alle Anfangsbuchstaben nimmt

# Übung 4
# Schreibe eine List-Comprehension die aus einem Text alle Wörter nimmt die 3 oder weniger Zeichen haben