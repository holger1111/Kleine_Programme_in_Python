# DIFFICULTY: 3
# Wir haben eine Liste mit zufälligen Zahlen.
from random import randint

random_list = []
for _ in range(5):
    random_list.append(randint(1, 10))
print(f"Zufalls-Liste: {random_list}")

# TASK: Schreibe ein Programm, dass diese Liste auf Dopplungen
#       von Zahlen prüft. Wenn mind. eine Zahl mehrfach vorkommt,
#       soll True ausgegeben werden.


def find_double(liste):
    sorted_liste = sorted(liste)
    double = False
    print(f"Sortierte Liste: {sorted_liste}")
    for i in range(len(sorted_liste) - 1):
        if sorted_liste[i] != sorted_liste[i + 1]:
            pass
        elif sorted_liste[i] == sorted_liste[i + 1]:
            double = True
            print(f"{double}\nMindestens eine Zahl kommt mehrfach vor.")
            break
    if double == False:
        print(f"{double}\nKeine Zahl kommt mehrfach vor.")


find_double(random_list)