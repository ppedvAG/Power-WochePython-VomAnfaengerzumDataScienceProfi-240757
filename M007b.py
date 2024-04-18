import sys

import M007
M007.countCase("Test")

from M007 import countCase
countCase("Test")

import Test.M007c
Test.M007c.hallo('Max')

# Modul Suchpfade
# 1. Im Ordner des Ausführenden Skripts
# 2. In der Standardbibliothek (venv)
# 3. In eigens konfigurierten Pfaden (mittels sys.path.append)
# Wenn das Modul nicht gefunden wird -> ModuleNotFoundError
for p in sys.path:
	print(p)
print(sys.version)
# sys.exit(0)

# Externe Pakete
# 2 Möglichkeiten Pakete zu installieren
# Über Python Packages
# Über pip
# - pip install <package>
# - pip install <package>

# Die Main Methode
# Code der ausgeführt wird, wenn das Skript gestartet wird
# __name__: __main__, wenn das Skript direkt gestartet wird oder der Name des Skripts selbst, wenn dieses importiert wird
print(__name__)

# __init__.py
# Wird ausgeführt, wenn ein oder mehrere Skript(e) aus dem Ordner importiert wird/werden

# Die Main Methode wird oft ausgelagert in eine eigene Methode
def main():
	print()

if __name__ == '__main__':
	main()