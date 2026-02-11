# DIFFICULTY: 2
# TASK: Schreibe ein Programm, das fünf (Kopf-)Rechenaufgaben stellt.
#       Die genutzen Operatoren (+, -, /, ...), sowie die Zahlen
#       sollen zufällig geählt werden, aber generell im Kopf lösbar
#       sein.
#       Nach Eingabe des Ergebnisses wird ausgegeben, ob dies richtig
#       war und wenn ja, wie lange der/die Nutzer*in bis zur Eingabe
#       des richtigen Ergebnisses gebraucht hat.

import random, time


operatoren_liste = [
    "+",
    "-",
    "*",
    "/",
    "**2",
    "**0.5",
]  # plus, minus, mal, geteilt, hoch2, wurzel2
zahlen_liste = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
quadrat_liste = [i**2 for i in range(1, 11)]  # Quadratzahlen von 1 bis 10


def ran_random(end, start=0, end2=0, start2=0):
    if end2 != 0 and start2 != 0:
        liste = [random.randint(start, end), random.randint(start2, end2)]
        ran = liste[random.randint(0, 1)]
    else:
        ran = random.randint(start, end)
    return ran


def random_maths(diff):
    # Mischen der Zahlen
    random.shuffle(zahlen_liste)

    if diff == "1":
        ope = operatoren_liste[ran_random(3)]  # Bestimmen des Operators
        num1 = zahlen_liste[ran_random(9)]  # Bestimmen der ersten Zahl / Erste Zahl
        while True:  # Bestimmen der zweiten Zahl
            num2 = zahlen_liste[ran_random(9)]  # Zweite Zahl
            if num1 != num2:
                break
        math = f"{num1} {ope} {num2}"  # Ausgabe der Rechnung

    elif diff == "2":
        ope = operatoren_liste[ran_random(3)]  # Bestimmen des Operators
        while True:  # Bestimmen der ersten Zahl
            num1 = zahlen_liste[ran_random(9)]
            if num1 != "0":
                break
        num2 = zahlen_liste[ran_random(9)]
        numa = num1 + num2  # Erste Zahl
        if ope == "*" or ope == "/":  # Bestimmen der zweiten Zahl
            while True:
                num1 = zahlen_liste[ran_random(9)]
                numb = num1  # Zweite Zahl
                if numb != "0":
                    break
        else:
            num1 = zahlen_liste[ran_random(9)]
            if num1 == "0":
                num1 = ""
            while True:
                num2 = zahlen_liste[ran_random(9)]
                numb = num1 + num2  # Zweite Zahl
                if numb != numa and numb != "00":
                    break
        math = f"{numa} {ope} {numb}"  # Ausgabe der Rechnung

    elif diff == "3":
        ope = operatoren_liste[ran_random(5)]  # Bestimmen des Operators
        if ope == "**0.5":
            num = quadrat_liste[ran_random(9)]
            math = f"{num}{ope}"  # Ausgabe der Rechnung
        elif ope == "**2":
            while True:
                num = zahlen_liste[ran_random(9)]  # Erste Zahl
                if num != "0":
                    break
            math = f"{num}{ope}"  # Ausgabe der Rechnung
        elif ope == "*" or ope == "/":
            num1 = zahlen_liste[ran_random(9)]
            if num1 == "0":
                num1 = ""
            while True:
                num2 = zahlen_liste[ran_random(9)]
                if num2 != "0":
                    break
            numa = num1 + num2  # Erste Zahl
            while True:  # Bestimmen der zweiten Zahl
                num1 = zahlen_liste[ran_random(9)]
                numb = num1  # Zweite Zahl
                if numb != "0":
                    break
            math = f"{numa} {ope} {numb}"  # Ausgabe der Rechnung
        elif ope == "+" or ope == "-":
            ope2 = operatoren_liste[ran_random(1)]  # Bestimmen des zweiten Operators
            num1 = zahlen_liste[ran_random(9)]  # Bestimmen der ersten Zahl
            if num1 == "0":
                num1 = ""
            num2 = zahlen_liste[ran_random(9)]
            if num2 == "0" and num1 == "":
                num2 = ""
            while True:
                num3 = zahlen_liste[ran_random(9)]
                if num2 == "" and num3 != "0":
                    break
                elif num2 != "":
                    break
            numa = num1 + num2 + num3  # Erste Zahl
            num1 = zahlen_liste[ran_random(9)]  # Bestimmen der zweiten Zahl
            if num1 == "0":
                num1 = ""
            num2 = zahlen_liste[ran_random(9)]
            if num2 == "0" and num1 == "":
                num2 = ""
            while True:
                num3 = zahlen_liste[ran_random(9)]
                if num2 == "" and num3 != "0":
                    break
                elif num2 != "":
                    break
            numb = num1 + num2 + num3  # Zweite Zahl
            num1 = zahlen_liste[ran_random(9)]  # Bestimmen der dritten Zahl
            if num1 == "0":
                num1 = ""
            num2 = zahlen_liste[ran_random(9)]
            if num2 == "0" and num1 == "":
                num2 = ""
            while True:
                num3 = zahlen_liste[ran_random(9)]
                if num2 == "" and num3 != "0":
                    break
                elif num2 != "":
                    break
            numc = num1 + num2 + num3  # Dritte Zahl
            math = f"{numa} {ope} {numb} {ope2} {numc}"  # Ausgabe der Rechnung

    elif diff == "4":
        ope1 = operatoren_liste[ran_random(5)]  # Bestimmen des ersten Operators
        # Bestimmen der ersten Zahl
        if ope1 == "**0.5":
            numa = quadrat_liste[ran_random(9)]  # Erste Zahl
        elif ope1 == "**2":
            while True:
                numa = zahlen_liste[ran_random(9)]  # Erste Zahl
                if numa != "0":
                    break
        elif ope1 == "*" or ope1 == "/":
            num1 = zahlen_liste[ran_random(9)]
            if num1 == "0":
                num1 = ""
            while True:
                num2 = zahlen_liste[ran_random(9)]
                if num1 == "" and num2 != "0":
                    break
                elif num1 != "":
                    break
            numa = num1 + num2  # Erste Zahl
        elif ope1 == "+" or ope1 == "-":
            num1 = zahlen_liste[ran_random(9)]
            if num1 == "0":
                num1 = ""
            num2 = zahlen_liste[ran_random(9)]
            if num2 == "0" and num1 == "":
                num2 = ""
            while True:
                num3 = zahlen_liste[ran_random(9)]
                if num2 == "" and num3 != "0":
                    break
                elif num2 != "":
                    break
            numa = num1 + num2 + num3  # Erste Zahl
        math1 = f"{numa} {ope1} "  # Ausgabe des ersten Teils
        # Bestimmen des zweiten Operator
        if ope1 == "**0.5" or ope1 == "**2":
            ope2 = operatoren_liste[ran_random(3)]
        elif ope1 == "*" or ope1 == "/":
            ope2 = operatoren_liste[ran_random(5, 4, 0, 1)]
        elif ope1 == "+" or ope1 == "-":
            ope2 = operatoren_liste[ran_random(5, 2)]
        # Bestimmen der zweiten Zahl
        if (ope1 == "**0.5" or ope1 == "**2") and (ope2 == "+" or ope2 == "-"):
            num1 = zahlen_liste[ran_random(9)]
            if num1 == "0":
                num1 = ""
            num2 = zahlen_liste[ran_random(9)]
            if num2 == "0" and num1 == "":
                num2 = ""
            while True:
                num3 = zahlen_liste[ran_random(9)]
                if num2 == "" and num3 != "0":
                    break
                elif num2 != "":
                    break
            numb = num1 + num2 + num3  # Zweite Zahl
        elif (ope1 == "**0.5" or ope1 == "**2") and (ope2 == "*" or ope2 == "/"):
            while True:
                num1 = zahlen_liste[ran_random(9)]
                if num1 != "0":
                    break
            numb = num1  # Zweite Zahl
        elif (ope1 == "*" or ope1 == "/") and ope2 == "**0.5":
            numb = quadrat_liste[ran_random(9)]  # Zweite Zahl
        elif (ope1 == "*" or ope1 == "/") and ope2 == "**2":
            while True:
                numb = zahlen_liste[ran_random(9)]  # Zweite Zahl
                if numb != "0":
                    break
        elif (ope1 == "*" or ope1 == "/") and (ope2 == "+" or ope2 == "-"):
            num1 = zahlen_liste[ran_random(9)]
            if num1 == "0":
                num1 = ""
            while True:
                num2 = zahlen_liste[ran_random(9)]
                if num1 == "" and num2 != "0":
                    break
                elif num1 != "":
                    break
            numb = num1 + num2  # Zweite Zahl
        elif (ope1 == "+" or ope1 == "-") and ope2 == "**0.5":
            numb = quadrat_liste[ran_random(9)]  # Zweite Zahl
        elif (ope1 == "+" or ope1 == "-") and ope2 == "**2":
            while True:
                numb = zahlen_liste[ran_random(9)]  # Zweite Zahl
                if numb != "0":
                    break
        elif (ope1 == "+" or ope1 == "-") and (ope2 == "*" or ope2 == "/"):
            num1 = zahlen_liste[ran_random(9)]
            if num1 == "0":
                num1 = ""
            while True:
                num2 = zahlen_liste[ran_random(9)]
                if num1 == "" and num2 != "0":
                    break
                elif num1 != "":
                    break
            numb = num1 + num2  # Zweite Zahl
        if ope1 == "**0.5" or ope1 == "**2":
            math2 = f"{math1}{ope2} {numb} "  # Ausgabe des zweiten Teils
        else:
            math2 = f"{math1}{numb} {ope2} "  # Ausgabe des zweiten Teils
        # Bestimmen des dritten Operator und der dritten Zahl
        if ((ope1 == "**0.5" or ope1 == "**2") and (ope2 == "+" or ope2 == "-")) or (
            (ope1 == "+" or ope1 == "-") and (ope2 == "**0.5" or ope2 == "**2")
        ):
            ope3 = operatoren_liste[ran_random(3, 2)]
            while True:
                num1 = zahlen_liste[ran_random(9)]
                if num1 != "0":
                    break
            numc = num1  # Dritte Zahl
            math = f"{math2} {ope3} {numc} "  # Ausgabe des dritten Teils
        elif ((ope1 == "*" or ope1 == "/") and (ope2 == "**2" or ope2 == "**0.5")) or (
            (ope1 == "**0.5" or ope1 == "**2") and (ope2 == "*" or ope2 == "/")
        ):
            ope3 = operatoren_liste[ran_random(1)]
            num1 = zahlen_liste[ran_random(9)]
            if num1 == "0":
                num1 = ""
            num2 = zahlen_liste[ran_random(9)]
            if num2 == "0" and num1 == "":
                num2 = ""
            while True:
                num3 = zahlen_liste[ran_random(9)]
                if num2 == "" and num3 != "0":
                    break
                elif num2 != "":
                    break
            numc = num1 + num2 + num3  # Dritte Zahl
            math = f"{math2} {ope3} {numc} "  # Ausgabe des dritten Teils
        elif ((ope1 == "*" or ope1 == "/") and (ope2 == "+" or ope2 == "-")) or (
            (ope1 == "+" or ope1 == "-") and (ope2 == "*" or ope2 == "/")
        ):
            ope3 = operatoren_liste[ran_random(5, 4)]
            if ope3 == "**0.5":
                numc = quadrat_liste[ran_random(9)]  # Dritte Zahl
            elif ope3 == "**2":
                while True:
                    numc = zahlen_liste[ran_random(9)]  # Dritte Zahl
                    if numc != "0":
                        break
            math = f"{math2} {numc} {ope3}"

    # Auswertung
    erge1 = eval(math)
    start = time.time()
    zeit = time.time() - start
    while True:
        print("Ergebnis auf maximal 2 Nachkommastellen gerundet.")
        print(f"{math} =")
        erge2 = input()
        try:
            erge2 = int(erge2)
        except ValueError:
            try:
                erge2 = erge2.replace(",", ".")
                erge2 = float(erge2)
            except ValueError:
                print(f"Bitte gib eine Zahl ein und nicht {erge2}.")
                continue
        if round(erge2, 1) == round(erge1, 1) or (round(erge2, 2) == round(erge1, 2)):
            zeit = time.time() - start
            print(
                f"Deine Antwort ist richtig!\n{math} = {erge1}\nDu hast {zeit:.2f}s gebraucht!"
            )
            break
        else:
            print("Deine Antwort ist leider falsch!\nVersuche es noch einmal!")


def choose_diff():
    print("!Mathetest!")
    choice1 = input("Möchtest du Aufgaben von Schwierigkeitsstufe 1, 2, 3 oder 4?\n")
    if choice1 == "1":
        while True:
            random_maths("1")
            choice2 = input("Noch eine Aufgabe? j/n\n")
            print("------------------------------")
            if choice2 == "n":
                choice3 = input("Beenden? j/n\n")
                if choice3 == "j":
                    exit("Beendet")
                else:
                    choose_diff()
                    break
    elif choice1 == "2":
        while True:
            random_maths("2")
            choice2 = input("Noch eine Aufgabe? j/n\n")
            print("------------------------------")
            if choice2 == "n":
                choice3 = input("Beenden? j/n\n")
                if choice3 == "j":
                    exit("Beendet")
                else:
                    choose_diff()
                    break
    elif choice1 == "3":
        while True:
            random_maths("3")
            choice2 = input("Noch eine Aufgabe? j/n\n")
            print("------------------------------")
            if choice2 == "n":
                choice3 = input("Beenden? j/n\n")
                if choice3 == "j":
                    exit("Erfolgreich Beendet")
                else:
                    choose_diff()
                    break
    elif choice1 == "4":
        while True:
            random_maths("4")
            choice2 = input("Noch eine Aufgabe? j/n\n")
            print("------------------------------")
            if choice2 == "n":
                choice3 = input("Beenden? j/n\n")
                if choice3 == "j":
                    exit("Erfolgreich Beendet")
                else:
                    choose_diff()
                    break
    else:
        print(f"Bitte gib 1, 2, 3 oder 4 ein und nicht {choice1}!")


choose_diff()
