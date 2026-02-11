# DIFFICULTY: 3
# Domino-Steine haben immer zwei Hälften, die jeweils "Werte"
# zwischen 0 und 6 beinhalten.
# Mehr Infos dazu hier: https://de.wikipedia.org/wiki/Domino
#
# TASK: Schreibe ein Programm, dass alle möglichen Kombinationen
#       von Dominosteinen ausgibt, ohne Dopplungen.
#
# Beispiel:
"""
(0|0)(0|1)(0|2)(0|3)(0|4)(0|5)(0|6)
     (1|1)(1|2)(1|3)(1|4)(1|5)(1|6)
          (2|2)(2|3)(2|4)(2|5)(2|6)
               (3|3)(3|4)(3|5)(3|6)
                    (4|4)(4|5)(4|6)
                         (5|5)(5|6)
                              (6|6)
"""


for x in range(7):
     for z in range(x):
          print("     ", end="")
     for y in range(x, 7):
          print(f"({x}|{y})", end="")
     print("")