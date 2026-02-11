# DIFFICULTY: 4
# TASK: Schreibe ZWEI Programme, welche auf verschiedene Weise die maximale Wortlänge in
#       einem gegebenen String ausgeben.
#       Teste mindestens mit dem gegebenen String "s".
# CHALLENGE: Prüfe, welches deiner Programme schneller an die Lösung gelangt.

text = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor"
text += " invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et"
text += " accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata"
text += " sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing"
text += " elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,"
text += " sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd"
text += " gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
import time


def count_length_of_words(text):
    # Startzeit
    start = time.perf_counter()

    # Teilung des Inhalts in einzelne Wörter
    woerter = (
        text.replace(".", "")  # replace aller Satzzeichen
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

    # Lösche doppelte Wörter
    worte = set(woerter[i].lower() for i in range(len(woerter)))
    worte = list(worte)

    # Verknüpfung der Wörter mit ihrer Länge
    wort_liste = dict()
    for i in range(len(worte)):
        wort_liste[worte[i]] = len(worte[i])

    # Umwandlung des dict in tuple
    laenge = list((k, v) for (k, v) in wort_liste.items())

    # Sortierung nach Anzahl
    for j in range(len(laenge)):
        for l in range(0, len(laenge) - j - 1):
            if laenge[l][1] < laenge[l + 1][1]:
                laenge[l], laenge[l + 1] = laenge[l + 1], laenge[l]

    # Ausgabe
    laenge[0][1]
    zeit = round((time.perf_counter() - start) * 1_000_000)

    return count_length_of_words.__name__, laenge[0][1], zeit, laenge[0][0]


def counting_the_length_of_words_to_get_the_most_longest_word_in_all_of_the_text(text):
    # Startzeit
    start = time.perf_counter()

    # Teilung des Inhalts in einzelne Wörter
    woerter = (
        text.replace(".", "")  # replace aller Satzzeichen
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
        if woerter[i].lower() not in wort_liste:
            wort_liste[woerter[i].lower()] = len(woerter[i])

    # Ausgabe
    laenge = max([v for k, v in wort_liste.items()])
    zeit = round((time.perf_counter() - start) * 1_000_000)

    return (
        counting_the_length_of_words_to_get_the_most_longest_word_in_all_of_the_text.__name__,
        laenge,
        zeit,
    )


def compare_time(text):
    name1, laenge1, zeit1, wort = count_length_of_words(text)
    name2, laenge2, zeit2 = (
        counting_the_length_of_words_to_get_the_most_longest_word_in_all_of_the_text(
            text
        )
    )

    # Bestimme den längsten Namen
    ln1 = count_length_of_words(name1)[1]
    ln2 = counting_the_length_of_words_to_get_the_most_longest_word_in_all_of_the_text(
        name2
    )[1]
    ln3 = len("Funktion")
    if ln1 > ln2 and ln1 > ln3:
        l0 = ln1
        ln = ln1
    elif ln2 > ln1 and ln2 > ln3:
        l0 = ln2
        ln = ln2
    else:
        l0 = ln3
        ln = ln3
    # Bestimme die Länge der Länge
    ll1 = counting_the_length_of_words_to_get_the_most_longest_word_in_all_of_the_text(
        str(laenge1)
    )[1]
    ll2 = len("Max. Länge")
    if ll1 > ll2:
        l0 += ll1
        ll = ll1
    else:
        l0 += ll2
        ll = ll2
    # Bestimme die längste Zeit
    lz1 = count_length_of_words(str(zeit1))[1] + 2
    lz2 = (
        counting_the_length_of_words_to_get_the_most_longest_word_in_all_of_the_text(
            str(zeit2)
        )[1]
        + 2
    )
    lz3 = len("Dauer")
    if lz1 > lz2 and lz1 > lz3:
        l0 += lz1
        lz = lz1
    elif lz2 > lz1 and lz2 > lz3:
        l0 += lz2
        lz = lz2
    else:
        l0 += lz3
        lz = lz3
    # + Länge längstes Wort
    lw1 = laenge1
    lw2 = len("Längstes Wort")
    if lw1 > lw2:
        l0 += lw1
        lw = lw1
    else:
        l0 += lw2
        lw = lw2
    # + Anzahl Trennzeichen
    l0 += 5
    print(f"{"_" * l0}")
    print(
        f"|{" " * ((ln - ln3) // 2)}Funktion{" " * ((ln - ln3) // 2)}|{" " * ((ll - ll2) // 2)}Max. Länge{" " * ((ll - ll2) // 2)}|{" " * ((lz - lz3) // 2)}Dauer{" " * ((lz - lz3) // 2)}|{" " * ((lw - lw2) // 2)}Längstes Wort{" " * ((lw - lw2) // 2)}|"
    )
    print(f"|{"―" * (l0 - 2)}|")
    print(
        f"|{" " * ((ln - ln1) // 2)}{name1}{" " * ((ln - ln1+1) // 2)}|{" " * ((ll - ll1) // 2)}{laenge1}{" " * ((ll - ll1) // 2)}|{" " * ((lz - lz1+1) // 2)}{zeit1}ms{" " * ((lz - lz1) // 2)}|{" " * ((lw - lw1) // 2)}{wort}{" " * ((lw - lw1+1) // 2)}|"
    )
    print(f"|{"―" * (l0 - 2)}|")
    print(
        f"|{" " * ((ln - ln2) // 2)}{name2}{" " * ((ln - ln2) // 2)}|{" " * ((ll - ll1) // 2)}{laenge2}{" " * ((ll - ll1) // 2)}|{" " * ((lz - lz2+1) // 2)}{zeit2}ms{" " * ((lz - lz2) // 2)}|{" " * ((lw - lw1) // 2)}{wort}{" " * ((lw - lw1+1) // 2)}|"
    )
    print(f"{"‾" * l0}")


compare_time(text)
# Manchmal kommt 'consetetur' und manchmal 'sadipscing' als längstes Wort, beides len=10