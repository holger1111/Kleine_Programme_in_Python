# DIFFICULTY: 4
# TASK: Schreibe ein Programm, welches beliebig viele Durchgänge eines
#       Würfelspiels simuliert, wo jedes mal 5 Würfel geworfen werden.
#       Die Augensumme der Würfel wird addiert und stellt das Ergebnis
#       Durchgang dar.
#
#       Visualisiere die Häufigkeit jeder Augensumme in z.B. folgender
#       Weise:
"""
05->
06->
07->xx
08->xxxxx
09->xxxxxxxxx
10->xxxxxxxxxxxxx
11->xxxxxxxxxxxxxxxxxxxxxxxxxxx
12->xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
13->xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
14->xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
15->xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
16->xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
17->xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
18->xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
19->xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
20->xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
21->xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
22->xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
23->xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
24->xxxxxxxxxxxxxxxx
25->xxxxxxxxxxxxxxxx
26->xxxxxxxxxxx
27->xxxxx
28->xx
29->xx
30->
"""
import random


def throw_5_dices(amount):
    throws = list()
    
    for x in range(amount):
        throw_1 = random.randint(1,6)
        throw_2 = random.randint(1,6)
        throw_3 = random.randint(1,6)
        throw_4 = random.randint(1,6)
        throw_5 = random.randint(1,6)
        throwing = [throw_1, throw_2, throw_3, throw_4, throw_5]
        throws.append(throwing)
    #print(throws) # TODO: auskommentieren
    return throws


def sum_the_dices(liste):
    sum_list = list()
    
    for x in range(len(liste)):
        z = 0
        for y in range(len(liste[x])):
            z += liste[x][y]
        sum_list.append(z)
    #print(sum_list) # TODO: auskommentieren
    return sum_list


def draw_histogram(liste):
    counter = dict()
    for x in range(5, 31):
        y = liste.count(x)
        counter[x]= y
    # print(counter) # TODO: auskommentieren
    for x in range(5, 31):
        if x < 10:
            print(f"0{x}->", end="")
        else:
            print(f"{x}->", end="")
        for y in range(counter[x]// 2):
            print("x", end="")
        print("")


draw_histogram(sum_the_dices(throw_5_dices(3000)))





