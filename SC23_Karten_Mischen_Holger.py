# DIFFICULTY: 4
# Ein Skat Spiel hat 32 Karten mit folgenden Farbe-Wert Kombinationen:
# Farben sind: Kreuz, Pik, Herz und Karo.
# Werte sind: Ass, König, Dame, Bube, Zehn, Neun, Acht, Sieben.
#
# TASK1: Schreibe ein Programm, was eine Liste mit allen 32 Karten erstellt,
#        wobei jede Karte ein Tupel mit Farbe und Wert ist.
#
# TASK2: Erweitere dein Programm, um das Mischen der Karten zu erlauben.
#        Versuche dies ohne random.shuffle() zu verwenden.
# TIP: Zufällige Karten auswählen (mit random) und ihre Positionen in der
#      Liste tauschen.

import random
suits = ['Kreuz', 'Pik', 'Herz', 'Karo']
ranks = ['Ass', 'Koenig', 'Dame', 'Bube', '10', '9', '8', '7']


def shuffle_cards(switches):
    tupler = list()
    tuplerone = list()
    for a in range(len(suits)):
        for b in range(len(ranks)):
            tupler = list()
            tupler.append(suits[a])
            tupler.append(ranks[b])
            mein_tuple = tuple(tupler)
            tuplerone.append(mein_tuple)
    print(tuplerone)
    # print(len(tuplerone))     # Kontrolle, ob 32 Karten existieren
    
    for c in range(1, switches - 1):
        rand = False
        while rand == False:
            rand1 = random.randint(1, 31)
            rand2 = random.randint(1, 31)
            if rand1 != rand2:
                rand = True
        print("Ursprung: " + str(tuplerone[rand1]), str(tuplerone[rand2]))
        tuplerone[rand1], tuplerone[rand2] = tuplerone[rand2], tuplerone[rand1]
        print("Gemischt" + str(tuplerone[rand1]), str(tuplerone[rand2]))
    
    print(tuplerone)


shuffle_cards(100)
