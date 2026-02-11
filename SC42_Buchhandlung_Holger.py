# DIFFICULTY: 5
# In einer Buchhandlung finden wir in einem Abrechnungsprogramm
# Listen mit folgendem Aufbau:


# Bestellnummer      Buchtitel und Autor            Anzahl      Einzelpreis
#     34587       Learning Python, Mark Lutz          4           40.95
#     98762       Programming Python, Mark Lutz       5           56.80
#     77226       Head First Python, Paul Barry       3           32.95


orders = [
    ["34587", "Learning Python, Mark Lutz", 4, 40.95],
    ["98762", "Programming Python, Mark Lutz", 5, 56.80],
    ["77226", "Head First Python, Paul Barry", 3, 32.95],
]

# TASK: Schreibe ein Programm mit map() & lambda, das als Ergebnis
#       eine Liste mit Zweier-Tupeln liefert.
#
# Jedes Tupel besteht aus der Bestellnummer und dem Produkt aus der
# Anzahl und dem Einzelpreis. Das Produkt soll jedoch um 10,- € erhöht
# werden, wenn der Bestellwert unter 100,00 € liegt. Die map()-Funktionen
# dürfen auch verschachtelt sein.


def create_tuple(order):
    # Ohne map() und lambda
    # Create Dictonary number : [price]
    dict1 = {}
    for i in range(len(order)):
        dict1[order[i][0]] = round(
            (
                order[i][2] * order[i][3]
                if order[i][2] * order[i][3] > 100
                else order[i][2] * order[i][3] + 10
            ),
            2,
        )
    print(dict1)

    # Umwandlung in tuple
    bestellung = [(k, v) for k, v in dict1.items()]
    print(bestellung)
    # ---------------------------------------

    bestell_nr = [i[0] for i in orders]
    preis = list(map(lambda i: round(i[2] * i[3], 2) + (10 if i[2] * i[3] < 100 else 0), orders))
    dict2 = dict(zip(bestell_nr, preis))
    print(dict2)
    # Umwandlung in tuple
    bestellung2 = [(k, v) for k, v in dict2.items()]
    print(bestellung2)
    
create_tuple(orders)

