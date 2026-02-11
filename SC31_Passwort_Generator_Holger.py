# DIFFICULTY: 3
# TASK: Schreibe ein Programm, welches ein Passwort anhand folgender
#       Anforderungen generiert:
#       1. Nimmt eine Zahl für die Länge entgegen, mind. aber 8 Zeichen
#       2. Enthält immer: Groß-, Kleinbuchstabe, Zahl, Sonderzeichen
# TIP: Einige imports können dir hier sehr viel Arbeit abnehmen. Recherchiere
#      über Möglichkeiten, möglichst einfach z.B. Großbuchstaben abzubilden.
import random, secrets
# Zufallszahl von 1 bis 10 (kryptografisch sicher)
# zahl = secrets.randbelow(10) + 1


def enter_length():
    print("Bitte geben Sie die gewünschte Länge des Passworts als ganze Zahl ein.\nMindestlänge: 8")
    while True:
        laenge = input("Gewünschte Länge: ")
        try:
            laenge = int(laenge)
            if laenge >= 8:
                break
            else:
                print("Bitte geben Sie eine Länge von mindestens 8 als ganze Zahl ein!")
        except Exception:
            print("Bitte geben Sie eine Länge von mindestens 8 als ganze Zahl ein!")
    print("---------------------------------")
    return laenge


def generate_password(laenge=enter_length()):
    big_letter= ["A", "B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    small_letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    special_letter = ["Ä", "Ö", "Ü", "ä","ö","ü","ß", "-", "+", "*", "=", "@", "€", "$", "§", "!", "?", ",", ".", ";", ":", "_", "/", "{", "}", "[", "]", "(", ")", "#", "'", '"', "%", "&", "~", "^","°", "`","´", "<", ">", "|"]
    number_letter = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    forbidden_letter = ["\\"]
    
    # Gesamte Liste
    all_letter = list()
    for x in range(len(big_letter)):
        all_letter.append(big_letter[x])
    for x in range(len(small_letter)):
        all_letter.append(small_letter[x])
    for x in range(len(special_letter)):
        all_letter.append(special_letter[x])
    for x in range(len(number_letter)):
        all_letter.append(number_letter[x])
    # print(all_letter) # TODO: auskommentieren
    
    # Mindestens 1 Großbuchstabe, 1 Kleinbuchstabe, 1 Sonderzeichen und 1 Zahl
    passwort_letter = list()
    big = secrets.choice(big_letter)
    small = secrets.choice(small_letter)
    special = secrets.choice(special_letter)
    numb = secrets.choice(number_letter)
    # print(big, small, special, numb) # TODO: auskommentieren
    passwort_letter.append(big)
    passwort_letter.append(small)
    passwort_letter.append(special)
    passwort_letter.append(numb)
    
    # Mit restlichen Stellen auffüllen
    for x in range(laenge-4):
        temp = secrets.choice(all_letter)
        passwort_letter.append(temp)
    # print(passwort_letter, len(passwort_letter)) # TODO: auskommentieren
    
    # Mixen der Zeichen
    mixer = secrets.randbelow(1000) + 1
    
    for x in range(1, mixer - 1):
        rand = False
        while rand == False:
            a = random.randint(1, len(passwort_letter) -1)
            b = random.randint(1, len(passwort_letter) -1)
            if a != b:
                rand = True
        passwort_letter[a], passwort_letter[b] = passwort_letter[b], passwort_letter[a]
        
    # Ausgabe
    passwort = ""
    for x in range(len(passwort_letter)):
        passwort += passwort_letter[x]
    # print(passwort) # TODO: auskommentieren
    # print(len(all_letter)) # TODO: auskommentieren
    return passwort


generate_password()