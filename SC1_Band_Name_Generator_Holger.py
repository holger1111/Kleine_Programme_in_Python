# DIFFICULTY: 2
# Anhand der folgenden Schritte, kann man einen Generator für einen möglichen Band-Namen
# schreiben:
# 0. Erstelle ein Struktogramm für das Projekt.
# 1. Erstelle eine Begrüßung für dein Programm.
# 2. Frage die/den Nutzer*in, in welcher Stadt sie/er aufgewachsen ist.
# 3. Frage nach ihrem/seinem Lieblingstier.
# 4. Kombiniere den Namen der Stadt mit dem Namen des Lieblingstieres zu einem Band Namen.
# 5. Achte darauf, dass das Fenster offen bleibt.
#
# TASK: Folge den einzelnen Schritten und schreibe ein Programm, welche einen Band-Namen 
#       anhand der Stadt und des Lieblingstiers ausgibt.
# TIP: Die Ein-/Ausgabe auf Englisch macht korrekte Grammatik hier deutlich einfacher.

print("Welcome to the Band Name Generator.\nYour Band Name will be generated based on your input.\n")
print("What city did you grow up in?")
city = input()
print("What is your favorite animal?")
animal = input()
band_name = city + " " + animal
print("Your band name could be:\n\n" + band_name)