# DIFFICULTY: 2
# TASK: Schreibe ein Programm, was ein gegebenes Passwort anhand eines
#       Punktesystems auf seine Sicherheit überprüft.
#       Dabei gelten die folgenden Regeln:
#       1. Mindestens 8 Zeichen, sonst immer 0 Punkte
#       2. Jeweils einen Punkt für:
#       – Enthält sowohl Groß- als auch Kleinbuchstaben
#       – Enthält mehr als sechs unterschiedliche Zeichen
#       – Enthält mindestens eine Ziffer
#       – Enthält mindestens ein Sonderzeichen
#       - Jedes Zeichen ab 9
#
# Beispiele:
# abc -> 0 Punkte
# abcdefghij -> 2 Punkte
# ab1122$$!! -> 3 Punkte
# Abcd1234$! -> 5 Punkte

from SC31_Passwort_Generator_Holger import generate_password

def estimate_security_passwort(passwort):
    big_letter= ["A", "B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    small_letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    special_letter = ["Ä", "Ö", "Ü", "ä","ö","ü","ß", "-", "+", "*", "=", "@", "€", "$", "§", "!", "?", ",", ".", ";", ":", "_", "/", "{", "}", "[", "]", "(", ")", "#", "'", '"', "%", "&", "~", "^","°", "`","´", "<", ">", "|"]
    number_letter = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        
    punkte = 0
    # Prüfe Länge > 8
    if len(passwort) < 8:
        exit(f"Passwort:\n{passwort}\nBewertung:\n{punkte} Punkte")
    
    # Prüfe 1 Großbuchstabe und 1 Kleinbuchstabe
    big = False
    small = False
    for x in range(len(passwort)):
        if passwort[x] in big_letter:
            big = True
        if passwort[x] in small_letter:
            small = True
    if big is True and small is True:
        punkte += 1
    
    # Prüfe > 6 unterschiedliche Zeichen
    sorte_passwort = sorted(passwort)
    i = 0
    counter = 0
    while i < (len(sorte_passwort) - 1) and counter < len(passwort) - 6:
        if sorte_passwort[i] == sorte_passwort[i + 1]:
            counter += 1
        i += 1
    if counter < len(passwort) - 6:
        punkte += 1
    
    # Prüfe 1 Ziffer
    numb = False
    for x in range(len(passwort)):
        if passwort[x] in number_letter:
            numb = True
    if numb == True:
        punkte += 1
    
    # Prüfe 1 Sonderzeichen
    special = False
    for x in range(len(passwort)):
        if passwort[x] in special_letter:
            special = True
    if special == True:
        punkte += 1
    
    # Prüfe Länge
    laenge = len(passwort) - 8
    punkte += laenge
    
    print(f"Passwort:\n\n{passwort}\n\nBewertung:\n\n{punkte} Punkte")
    print("---------------------------------")


estimate_security_passwort(generate_password())