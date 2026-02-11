# DIFFICULTY: 1
# TASK: Erstelle eine Funktion, welcher Preis, Anzahl und Währung übergeben werden.
#       Daraus sollen die entsprechenden Gesamtkosten erechnet und ausgegeben werden.
#       Währung und Anzahl sollen jeweils einen Standardwert haben (z.B. € und 1)


def calculate_all_costs(preis=None, waehrung=None, anzahl=None):
    print("-------------")
    
    waehrung_allowed = ("€", "EUR", "Euro", "$", "Dollar", "dollar")
    # Eingaben kontrollieren
    if preis == None:
        exit("Bitte gib einen Preis ein!")
    elif type(preis) is float or type(preis) == int:
        print(f"Preis:   OK")
        if type(preis) is int:
            preis = float(preis)
    else:
        exit(f"!Stop!\n'{preis}' ist kein Preis!")
        
    if waehrung == None:
        waehrung = "€"
        print(f"Währung nicht angegeben!\nWährung wurde auf '€' gesetzt!")
    elif type(waehrung) is str and waehrung in waehrung_allowed:
        print(f"Währung: OK")
        if waehrung == "€" or waehrung == "EUR" or waehrung == "Euro":
            waehrung = "€"
        elif waehrung == "$" or waehrung == "Dollar" or waehrung == "dollar":
            waehrung = "$"
    else:
        print(f"'{waehrung}' ist keine Währung!\nWährung wird auf '€' gesetzt!")
        waehrung = "€"
        
    if anzahl == None:
        anzahl = 1
        print(f"Anzahl nicht angegeben!\nAnzahl wird auf '1' gesetzt!")
    elif type(anzahl) is float or type(anzahl) is int:
        print(f"Anzahl:  OK")
    else:
        print(f"'{anzahl}' ist keine Zahl!\nAnzahl wird auf '1' gesetzt!")
        anzahl = 1
        
    print("-------------")
    # Summe ermitteln
    summe = preis * anzahl
    # Formatieren
    summe = str(summe).replace(".",",")
    preis = str(preis).replace(".",",")
    
    summe_test = summe.split(",")
    preis_test = preis.split(",")
    
    summe_nach_komma = summe_test[1]
    preis_nach_komma = preis_test[1]
    
    if len(summe_nach_komma) < 2:
        summe += "0"
    if len(preis_test[1]) < 2:
        preis += "0"
    # Ausgabe
    if anzahl > 1:
        print(f"Der Gesamtpreis für {anzahl} Waren zu {preis} {waehrung} ist:\n{summe} {waehrung}")
    else:
        print(f"Der Gesamtpreis für {anzahl} Ware zu {preis} {waehrung} ist:\n{summe} {waehrung}")
    print("-------------")


calculate_all_costs(10.12, "€", 2)
calculate_all_costs(102.10, "Dollar")
calculate_all_costs(20)
calculate_all_costs(11.2, "fool",)
calculate_all_costs(2, 3, 2)
calculate_all_costs("lol", "€", "2")
