# DIFFICULTY: 4
# Wir wollen einen Bubble-Sort schreiben, welcher wie folgt vorgeht:
# 1. Eine Liste wird von links durchlaufen.
# 2. Jeder Index/Zahl wird mit der folgenden verglichen.
# 2.1 Wenn die folgende Zahl kleiner ist, wird diese mit dem aktuellen
#     Index getauscht.
# 3. Es schreitet zum nächsten Index weiter und prüft erneut die Größen.
# 4. Dies wiederholt sich so lange, bis bei einem gesamten Durchgang keine
#    Zahlen mehr getauscht werden müssen.
# 5. Die neue, sortierte Liste wird zurückgegeben.

# TASK: Schreibe ein Programm, was eine beliebige Liste von Ganzzahlen
#       entgegennimmt und diese aufsteigend sortiert. Teste mit verschiedenen Listen.

liste_von_zahlen = [2,3,5,23,3,2,523,534,23,2,32,12,5,2,21,2,523,12,3,12,52,3234,2351,2,1,1,1,0,124,23]


def create_a_list_of_random_numbers(amount, mini, maxi):
    import random
    liste = list()
    for x in range(amount):
        liste.append(random.randint(mini, maxi+1))
    return liste
    


def sort_bubbles(liste):
    counter = 1
    while counter > 0:
        counter = 0
        for i in range(len(liste)-1):
            if liste[i] > liste[i + 1]:
                temp = liste[i]
                liste[i] = liste[i+1]
                liste[i+1] = temp
                counter += 1
    print(liste)


sort_bubbles(liste_von_zahlen)

sort_bubbles(create_a_list_of_random_numbers(100, 0, 100))