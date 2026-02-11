# DIFFICULTY: 5
# TASK: Schreibe eine Funktion flatten(), die eine nested Liste oder Tupel
#       in eine flache Liste ohne Nestings überführt.

nested_list = [(1, 2), 'Python', ['a', [1, 7]], 1, 1.3]
# [1, 2, 'Python', 'a', 1, 7, 1, 1.3]


def flatten(listen):
    new_liste = list()
    counter = 1
    liste = listen
    while counter >= 1:
        for x in range(len(liste)):
            inner_liste = list()
            if type(liste[x]) is list or type(liste[x]) is tuple:
                counter += 1
                for z in range(len(liste[x])):
                    inner_liste.append(liste[x][z])
                for y in range(len(inner_liste)):
                    new_liste.append(inner_liste[y])
                inner_liste = list()
            else:
                new_liste.append(liste[x])
        # print(counter)
        liste = new_liste
        new_liste = list()
        counter -= 1
    # print(liste)
    return liste


flatten(nested_list)