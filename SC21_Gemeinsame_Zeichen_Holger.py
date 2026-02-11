# DIFFICULTY: 2
# TASK: Schreibe ein Programm, dass die gemeinsamen Zeichen
#       von zwei angegebenen Strings ausgibt.
#       Teste mindestens mit den Strings string1 & string2, sowie
#       mindestens zwei zusätzlichen.

string1 = 'Python'
string2 = 'Programmierung'

string3 = 'Aufmerksamkeitsdefizit-Hyperaktivitätsstörung'
string4 = 'Kraftfahrzeug-Haftpflichtversicherung'


def print_equal_chars(str1, str2):
    liste = list()
    if len(str1) > len(str2):
        for i in range(len(str1)):
            if str1[i] in str2:
                liste.append(str1[i])
    else:
        for i in range(len(str2)):
            if str2[i] in str1:
                liste.append(str2[i])
    sorted_liste = sorted(liste)
    i = 0
    while i < (len(sorted_liste) - 1):
        if sorted_liste[i] == sorted_liste[i + 1]:
            sorted_liste.pop(i + 1)
        else:
            i += 1
    print(f"Gemeinsame Buchstaben von:\n{str1}\n{str2}\n{sorted_liste}")
    print(f"Insgesamt {len(sorted_liste)} unterschiedliche Buchstaben.")

print_equal_chars(string1, string2)
print("")
print_equal_chars(string3, string4)


