# DIFFICULTY: 3
# TASK1: Schreibe ein Programm, dass eine Liste mit 9 zufälligen Zahlen erstellt.
#       Jede Zahl, bis auf eine, soll darin doppelt enthalten sein. Gebe diese Liste aus.

# TASK2: Mische die Liste mit random.shuffle() und erweitere das Programm, so dass es
#        die Zahl findet, die einmalig vorkommt und diese ausgibt.

import random
liste_1 = []


def nine_random_numbers_double_only_one_unique():
    for x in range(5):
        number = random.randint(0, 101)
        if number not in liste_1:
            liste_1.append(number)
    
    for x in range(len(liste_1)-1):
        liste_1.append(liste_1[x])


def shuffle_list_and_find_unique():
    random.shuffle(liste_1)
    for number in liste_1:
        if liste_1.count(number) == 1:
            print("Unique number:", number)
            break


nine_random_numbers_double_only_one_unique()
print(liste_1)
print("___________________________")
shuffle_list_and_find_unique()
