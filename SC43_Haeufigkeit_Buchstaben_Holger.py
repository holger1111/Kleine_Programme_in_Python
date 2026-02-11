# DIFFICULTY: 3
# TASK: Schreibe eine Funktion, die die Buchstabenhäufigkeit eines Strings bestimmt.
#       Die Häufigkeiten sollen sortiert ausgegeben werden. Dabei sollen keine Sonderzeichen
#       & Ziffern berücksichtigt werden.
import string


def count_alphabet_char(text):
    alphabet = string.ascii_letters + "ÄäÖöÜüß"
    # Teilung des Texts in einzelne Zeichen
    text2 = [char for char in text]
    # Übertragung aller Buchstaben des Alphabets in eine Liste und mache sie klein
    buchstaben = [
        text2[char].lower() for char in range(len(text2)) if text2[char] in alphabet
    ]
    # Verknüpfung der Buchstaben mit ihrer Anzahl
    buchstaben_liste = dict()
    for i in range(len(buchstaben)):
        if buchstaben[i] in buchstaben_liste:
            buchstaben_liste[buchstaben[i]] += 1
        else:
            buchstaben_liste[buchstaben[i]] = 1
    # buchstaben_liste = {buchstaben[i] += 1 for i in range(len(buchstaben)) if buchstaben[i] in buchstaben_liste else buchstaben[i] = 1}
    # Umwandlung in tuple
    anzahl = [(k, v) for k, v in buchstaben_liste.items()]
    # Ordnung nach der Menge
    for j in range(len(anzahl)):
        for l in range(0, len(anzahl) - j - 1):
            if anzahl[l][1] < anzahl[l + 1][1]:
                anzahl[l], anzahl[l + 1] = anzahl[l + 1], anzahl[l]
    # anzahl = [[[anzahl[i], anzahl[i + 1] = anzahl[i + 1], anzahl[i] for i in range(len(anzahl) - j - 1)] for j in range(len(anzahl))] if anzahl[i][1] < anzahl[i + 1][1]]
    print(anzahl)


a = "Ein sonniger Herbsttag zog über die Hügel des Schwarzwaldes. Bauer Heinrich trieb seine robusten Kühe zur Weide, während die Kinder lachend durch bunte Laubhaufen tobten. Im Dorf läuteten die Kirchenglocken zur Vesper. Oma Martha buk frischen Apfelkuchen, dessen Duft durch die Gassen schwebte. Nachbarn plauderten über die Ernte und den nahenden Winter. Der alte Müller spann Garn vor seiner Tür und erzählte Geschichten von einst. Friedlich pulsierte das Leben in diesem kleinen Paradies."
count_alphabet_char(a)
