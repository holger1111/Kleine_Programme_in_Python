# DIFFICULTY: 3
# TASK: Schreibe eine Funktion frequencies(), die zu jedem Zeichen eines übergebenen Strings 
#       deren Häufigkeit ermittelt.
#       Zurückgegeben wird ein Dictionary in dem jedem Zeichen dessen Vorkommenshäufigkeit zugeordnet wird.

# Beispiel:
# print(frequencies("Erdbeere"))
# {"E": 1, "r": 2, "d": 1, "b": 1, "e": 3}


def frequencies(string):
    liste = list()
    liste_all = list()
    dict_abc = {}
    # Teilen in char
    for i in range(len(string)):
        liste.append(string[i])
    # Sortieren
    sorted_liste = sorted(liste)
    i = 0
    # Doppelgänger entfernen
    while i < (len(sorted_liste) - 1):
        if sorted_liste[i] == sorted_liste[i + 1]:
            sorted_liste.pop(i + 1)
        else:
            i += 1
    # Buchstaben zählen und zuordnen
    for a in range(len(sorted_liste)):
        dict_abc = {liste[a]: liste.count(liste[a])}
        liste_all.append(dict_abc)
        print(dict_abc)
        
    print(liste_all)


frequencies("Erdbeere")
