# DIFFICULTY: 3
# TASK: Schreibe ein Programm, welches eine Textdatei entgegennimmt und die
#       Häufigkeiten aller Wörter in den darin enthaltenen Texten wie folgt
#       ausgibt:
#       1. Sortierte Liste (absteigende Häufigkeit)
#       2. mit Tupeln (Wort, Häufigkeit)


def zaehle_woerter(text):
    # Laden der Datei
    with open(text, "r", encoding="utf-8") as datei:
        inhalt = datei.read()
    
    # Teilung des Inhalts in einzelne Wörter
    woerter = (
        inhalt.replace(".", "")  # replace aller Satzzeichen
        .replace(":", "")
        .replace(",", "")
        .replace(";", "")
        .replace("?", "")
        .replace("!", "")
        .replace("-", " ")
        .replace("‑", " ")
        .replace("\n", " ")
        .split()
    )  # leeres Split, damit eventuelle leere Strings gelöscht werden
    
    # Verknüpfung der Wörter mit ihrer Anzahl
    wort_liste = dict()
    for i in range(len(woerter)):
        if woerter[i] in wort_liste:
            wort_liste[woerter[i]] += 1
        else:
            wort_liste[woerter[i]] = 1
    
    # Umwandlung des dict in tuple
    anzahl = list()
    for k, v in wort_liste.items():
        anzahl.append((k, v))

    # Sortierung nach Anzahl
    for j in range(len(anzahl)):
        for l in range(0, len(anzahl) - j - 1):
            if anzahl[l][1] < anzahl[l + 1][1]:
                anzahl[l], anzahl[l + 1] = anzahl[l + 1], anzahl[l]
    
    # Ausgabe
    print("Häufigkeit, absteigend:")
    for m in anzahl:
        print(m)

zaehle_woerter(
    "C:/Users/Student/OneDrive - GFN GmbH (EDU)/LFZQ7 Programmierung Python/Blank/Welt_5_Dorf/5_Skill_Check/Text.txt"
)
