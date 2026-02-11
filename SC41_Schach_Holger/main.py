# Wir haben ein Schach-Programm, welches für verschiedene Figuren ihre jeweils
# gültigen Züge abhängig von ihrer Position ausgibt.

# Beispiele:
# Springer e5: ['f7', 'g6', 'd7', 'c6', 'f3', 'g4', 'd3', 'c4']
# Läufer d5: ['a2', 'a8', 'b3', 'b7', 'c4', 'c6', 'e6', 'e4', 'f7', 'f3', 'g8', 'g2', 'h1']

# Schachbrett Referenz:
"""
A8 B8 C8 D8 E8 F8 G8 H8
A7 B7 C7 D7 E7 F7 G7 H7
A6 B6 C6 D6 E6 F6 G6 H6
A5 B5 C5 D5 E5 F5 G5 H5
A4 B4 C4 D4 E4 F4 G4 H4
A3 B3 C3 D3 E3 F3 G3 H3
A2 B2 C2 D2 E2 F2 G2 H2
A1 B1 C1 D1 E1 F1 G1 H1
"""

# TASK: Ergänze die Klassen "Turm" und "Dame". Prüfe alle Klassen und erlaubten
#       Züge mehrmals.

# main

from springer import Springer
from laeufer import Laeufer
from turm import Turm
from dame import Dame

springer = Springer("e5")
print(springer)  # Springer@e5
print(springer.find_moves())  # ['f7', 'g6', 'd7', 'c6', 'f3', 'g4', 'd3', 'c4']

laeufer = Laeufer("d5")
print(laeufer)  # Läufer@d5
print(
    laeufer.find_moves()
)  # ['a2', 'a8', 'b3', 'b7', 'c4', 'c6', 'e6', 'e4', 'f7', 'f3', 'g8', 'g2', 'h1']

turm = Turm("b7")
print(turm)  # Turm@b7
print(
    turm.find_moves()
)  # ['b8', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7', 'b6', 'b5', 'b4', 'b3', 'b2', 'b1', 'a7']


dame = Dame("c3")
print(dame)  # Dame@c3
print(
    dame.find_moves()
)  # ['c4', 'c5', 'c6', 'c7', 'c8', 'd3', 'e3', 'f3', 'g3', 'h3', 'c2', 'c1', 'b3', 'a3', 'd4', 'e5', 'f6', 'g7', 'h8', 'd2', 'e1', 'b4', 'a5', 'b2', 'a1']
