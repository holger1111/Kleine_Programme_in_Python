# DIFFICULTY: 1
# Wir haben eine beliebige Liste, z.B.:
# [1, 2, 3, 2, 7, 3, 9]
#
# TASK: Schreibe ein Programm, welches die Liste aufsteigend
#       sortiert und ohne Dopplungen wiedergibt.

my_list = [1, 2, 3, 2, 6, 5, 5, 8, 9, 1, 2, 7, 5, 6, 7, 4, 7, 3, 9]


def annihilate_doppelgaenger(liste):
    sorted_liste = sorted(liste)
    i = 0
    while i < (len(sorted_liste) - 1):
        if sorted_liste[i] == sorted_liste[i + 1]:
            sorted_liste.pop(i + 1)
        else:
            i += 1
    print(sorted_liste)

# annihilate_doppelgaenger(my_list)
    
print(list(set(my_list)))