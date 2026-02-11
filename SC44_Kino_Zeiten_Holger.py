# DIFFICULTY: 1
# TASK: Schreibe ein Programm, welches die End-Zeit eines Films
#       anhand der Start- & Laufzeit ermittelt und ausgibt.
#       Teste mindestens mit 3 verschiedenen Zeiten.


def bestimme_Filmendzeit():
    # Eingabe Startzeit
    start = input("Bitte gib die Startzeit des Films an. z.B 18:15\n")
    startzeit = True
    while startzeit == True:
        try:
            start1 = start.split(":")
            hour = int(start1[0])
            minute = int(start1[1])

            if hour > 23 or hour < 0:
                raise ValueError  # Value und TypeError nicht als Standard-Error sondern nur verwendet, damit keine eigenen Error erstellt werden müssen
            elif minute > 59 or minute < 0:
                raise TypeError
            startzeit = False
        except ValueError:
            print(
                "______________________________\nBitte gib eine Startzeit zwischen 00:00 und 23:59 ein."
            )
            start = input("Bitte gib die Startzeit des Films an.\n")
        except TypeError:
            print(
                "______________________________\nBitte gib eine Startzeit zwischen 00:00 und 23:59 ein."
            )
            start = input("Bitte gib die Startzeit des Films an.\n")
        except Exception:
            print(
                "______________________________\nBitte gib die Startzeit so an:\nStunde:Minute"
            )
            start = input("Bitte gib die Startzeit des Films an.\n")

    # Eingabe Laufzeit
    laufzeit = input("Bitte gib die Laufzeit des Films in Minuten an. z.B. 90\n")
    lauf_zeit = True
    while lauf_zeit == True:
        try:
            laufzeit1 = int(laufzeit)
            if laufzeit1 <= 0:
                raise ValueError
            lauf_zeit = False
        except ValueError:
            print(
                "______________________________\nBitte gib eine Laufzeit größer 0 ein."
            )
            laufzeit = input(
                "Bitte gib die Laufzeit des Films in Minuten an. z.B. 90\n"
            )
        except Exception:
            print(
                "______________________________\nBitte gib die Laufzeit so an:\nMinute"
            )
            laufzeit = input(
                "Bitte gib die Laufzeit des Films in Minuten an. z.B. 90\n"
            )

    # Bestimme Laufzeit in Stunden und Minuten
    lauf_stunde = laufzeit1 // 60
    lauf_minute = laufzeit1 % 60

    # Bestimme Filmende
    gesamt_minuten = minute + lauf_minute
    end_minute = gesamt_minuten % 60
    end_stunde = (hour + lauf_stunde + (gesamt_minuten // 60)) % 24

    # Formatierung Ausgabe
    if hour < 10:
        hour = "0" + str(hour)
    else:
        hour = str(hour)
    if minute < 10:
        minute = "0" + str(minute)
    else:
        minute = str(minute)
    if end_stunde < 10:
        end_stunde = "0" + str(end_stunde)
    else:
        end_stunde = str(end_stunde)
    if end_minute < 10:
        end_minute = "0" + str(end_minute)
    else:
        end_minute = str(end_minute)
    print(
        f"{"_" * 26}\n|Startzeit: {hour}:{minute} Uhr{" " * 4}|\n|Laufzeit:{" " * (4 if len(laufzeit) > 2 else 5)}{laufzeit} Minuten|\n|Endzeit:{" " * 3}{end_stunde}:{end_minute} Uhr{" " * 4}|\n{"-" * 26}"
    )


bestimme_Filmendzeit()
