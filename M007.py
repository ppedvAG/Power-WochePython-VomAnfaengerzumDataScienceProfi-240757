# Module
# Sind Bibliotheken die wir in unseren Code einbinden können
# Ein Modul ist nur ein normales Python Skript
# Es können ganze Skripte oder nur einzelne Funktionen/Klassen eines Skripts importiert werden

# Wie funktioniert importieren?
# import turtle

# turtle.color('red', 'yellow')
# turtle.begin_fill()
# while True:
#     turtle.forward(400)
#     turtle.left(170)
#     if abs(turtle.pos()) < 1:
#         break
# turtle.end_fill()
# turtle.done()

# Alias
# Packages umbenennen
# z.B. turtle verkürzen zu t
# import turtle as t

# t.color('red', 'yellow')
# t.begin_fill()
# while True:
#     t.forward(400)
#     t.left(170)
#     if abs(t.pos()) < 1:
#         break
# t.end_fill()
# t.done()

# from import
# Mit dem from import können Teile eines Skripts importiert werden (Funktionen, Klassen)
# Alle Funktionen und Klassen die mit dem from import importiert werden, werden in unser Skript eingebunden
# -> Es muss kein Alias oder der Name angegeben werden
# from turtle import color, begin_fill, forward, left, pos, end_fill, done
# from turtle import *  # import *: Bindet alle Member des Skripts ein
#
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(400)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

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