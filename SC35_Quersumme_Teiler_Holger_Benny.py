# DIFFICULTY: 2
# TASK: Schreibe ein Programm, das alle Zahlen bis 1000 ausgibt,
#       die durch ihre Quersumme teilbar sind.
#
# Zum Beispiel:
# 777 / (7 + 7 + 7) = 37

n = 999


def finde_die_quersumme_mit_benny_und_holger(max_zahl):
    liste = list()
    max_zahl = int(max_zahl)
    for zahl in range(1, max_zahl + 1):
        z = zahl
        quersumme = 0
        liste2 = list()
        while z > 0:
            ziffer = z % 10
            liste2.insert(0, ziffer)
            quersumme += z % 10
            z //= 10
        if zahl % quersumme == 0:
            ql = list()
            ql.append(zahl)
            ql.append(liste2)
            ql.append(int(zahl / quersumme))
            liste.append(ql)
    for x in range(len(liste)):
        if len(liste[x][1]) > 1:
            print(f"{liste[x][0]:{len(str(max_zahl))}d} / (", end="")
        else:
            print(f"{liste[x][0]:{len(str(max_zahl))}d} / ", end="")
        j = 0
        while j in range(len(liste[x][1])):
            while len(liste[x][1]) > 0:
                print(f"{liste[x][1][j]}", end="")
                del liste[x][1][0]
                if len(liste[x][1]) > 0:
                    print(" + ", end="")
            if len(str(liste[x][0])) > 1:
                print(")", end="")
                l = len(str(max_zahl))
                e = len(str(liste[x][0]))
                o = l - e
                print(" " * (o * 4 + 1), end="")
                
                print(f"= {liste[x][2]:{len(str(max_zahl))}d}")
            else:
                l = len(str(max_zahl))
                e = len(str(liste[x][0]))
                o = l - e
                print(" " * (o * 4 + 3), end="")
                
                print(f"= {liste[x][2]:{len(str(max_zahl))}d}")
    print("")


finde_die_quersumme_mit_benny_und_holger(1111)
