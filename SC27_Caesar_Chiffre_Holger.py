# DIFFICULTY: 5
# Ein Caesar-Chiffre ist eine simple Verschlüsselungsmethode, bei
# welcher die Buchstaben des Alphabets um eine beliebige Anzahl 
# "verschoben" werden. 
# Z.B. Verschiebung 2: a = c, b = d, c = e, ...
# Mehr Infos hier: https://de.wikipedia.org/wiki/Caesar-Verschl%C3%BCsselung
# 
# TASK: Schreibe ein Programm, das alle möglichen Lösungen eines mit einer
#       Caesar-Chiffre verschlüsselten Strings ausgibt.
#       Teste mindestens mit diesem String: "vxumxgssokxkt sginz yvgyy"
# TIP: Eine Brute-Force Methode reicht hier vollkommen, alles darüber hinaus
#       sprengt vollkommen die Anforderungen.


def randomize_offset():
    import random
    offset = random.randint(1,1000)
    return offset


def encipher_caesar(lang, code, offset):
    german_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ä","ö","ü","ß"]
    lang_dict = {}
    if lang == "ger":
        code_base = german_letters
        for z in range(len(german_letters)):
            lang_dict[german_letters[z]] = z
    # Umwandlung zu Kleinbuchstaben
    transform_code_1 = list()
    for y in range(len(code)):
        transform_code_1.append(code[y].lower())
    # Säubern von "ungültigen" Zeichen
    cleaner = list()
    for a in transform_code_1:
        if a in code_base:
            cleaner.append(a)
    transform_code_1 = cleaner
    # Umwandlung zu Zahlen
    transform_code_2 = list()
    for x in range(len(transform_code_1)):
        if transform_code_1[x] in lang_dict:
            transform_code_2.append(lang_dict[transform_code_1[x]])
    # Verschiebung um offset
    transform_code_3 = list()
    for v in transform_code_2:
        u = (v + offset) % len(german_letters)
        transform_code_3.append(u)
    # Umwandlung zu Buchstaben
    s = ""
    for r in transform_code_3:
        s += code_base[r]
    # Ausgabe
    print(f"Dein Code '{code}'\nist jetzt verschlüsselt als:\n'{s}'\nVerschoben wurde um:\n'{offset}'")
    print("-" * (len(s)+ 6))
    return s


def decipher_caesar(lang, code):
    german_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ä","ö","ü","ß"]
    lang_dict = {}
    # Sprachauswahl
    if lang == "ger":
        offset = len(german_letters)
        code_base = german_letters
        for z in range(len(german_letters)):
            lang_dict[german_letters[z]] = z
    # Umwandlung zu Kleinbuchstaben
    transform_code_1 = list()
    for y in range(len(code)):
        transform_code_1.append(code[y].lower())
    # Umwandlung zu Zahlen
    transform_code_2 = list()
    for x in range(len(transform_code_1)):
        if transform_code_1[x] in lang_dict:
            transform_code_2.append(lang_dict[transform_code_1[x]])
    # Benutze offset
    transform_code_4 = list()
    # Verschiebung um offset
    for w in range(offset):
        transform_code_3 = list()
        for v in transform_code_2:
            u = (v + w) % offset
            transform_code_3.append(u)
        transform_code_4.append(transform_code_3)
    # Umwandlung zu Buchstaben
    transform_code_5 = list()
    for t in transform_code_4:
        s = ""
        for r in t:
            s += code_base[r]
        transform_code_5.append(s)
    # Ausgabe
    i = 1
    print(f"Es gibt {offset} mögliche Lösungen:")
    for q in transform_code_5:
        if i < 10:
            print(f"  {i}. {q}")
        elif i < 100:
            print(f" {i}. {q}")
        else:
            print(f"{i}. {q}")
        i += 1
    print("-" * (len(q) + 6))


# encipher_caesar("ger", "Hallo", 2)
decipher_caesar("ger", encipher_caesar("ger", "Hallo! Wie geht es dir, Benny?", randomize_offset()))