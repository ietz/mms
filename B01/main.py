import numpy as np


# @-------------------
# | Aufgabe 2
# | Teilaufgabe a)
# @

# Erstellt ein 2D array mit einer Zeile bestehend aus 10 1.0en
np.ones((1, 10))

# Erstellt ein 2D array mit einer Spalte bestehend aus 10 1.0en
np.ones((10, 1))

# 1D Array mit 10x 1.0
np.ones((10))

# Das gleiche wie mit ((10))
np.ones(10)

# Datentyp int statt float
np.ones(10, np.int)

# Array mit Zahlen von 1 bis inklusive 9.5 in 0.5er Schritten
np.arange(1, 10, 0.5)

# Array mit absteigenden Zahlen von 100 bis inklusive 51 in 1er Schritten
np.arange(100, 50, -1)

# Array von 0.0 bis inkl. 1.9 in 0.1er Schritten, elementweise multipliziert mit pi
np.pi*np.arange(0, 2, 0.1)


# @
# | Teilaufgabe b)
# @

a = np.array([[1, 2], [3, 4]])
m = np.matrix(a)

# Multipliziert elementweise
a*a

# Macht Matrixmultiplikation mit Zeile*Spalte und so
m*m

# Potenziert elementweise
a**a

# TypeError weil Matrix nur mit int Exponenten potenziert werden kann
m**m

# Macht aufgrund der 2D Eingabearrays eine Matrixmultiplikation
np.dot(a, a)

# Auch Matrixmultiplikation
np.dot(m, m)


# @
# | Teilaufgabe c)
# @

# 6x6 Array mit Zufallszahlen zwischen -10 und 10
z = np.random.randint(-10, 11, (6, 6))

# erste Zeile
z[0]

# fünfte Spalte
zs = z[:, 4]

# fünfte Zeile multipliziert mit 2
zs * 2

# Gerade Zeilen
z[1::2]

# Ungerade Spalten
z[:, ::2]

# 3x3 Matrix
z[1:4, 1:4]

# minimaler Wert 0
z.clip(min=0)
# oder modifizierend
z[z < 0] = 0
