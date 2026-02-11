# DIFFICULTY: 3
# Schere, Stein, Papier kann für beliebig viele Runden gespielt werden.
# Wir wollen uns am Anfang aussuchen, wie viele Runden wir spielen wollen
# und danach diese gewählte Anzahl spielen.
#
# TASK: Schreibe ein Programm, dass das Spiel für eine beliebige Anzahl
#       an Runden umsetzt.
#
# CHALLENGE 1: Gib dem Computer eine 100% Chance zu gewinnen.
# CHALLENGE 2: Gib dem Computer etwas bessere Chancen zu gewinnen, aber
#              lass es immer noch glaubwürdig erscheinen.
right = False


def play_rock_paper_scissors_totaly_unfair():
    while True:
        print("Wie viele Runden möchtest du spielen?: ")
        rounds = input()
        print("-----------------------------------")
        try:
            rounds = int(rounds)
            if rounds <= 0:
                rounds = int("fool")
        except Exception:
            print(f"Bitte gib eine ganze Zahl ein, die größer als 0 ist und nicht {rounds}!")
            continue
        player_score = 0
        ai_score = 0
        for i in range(rounds):
            print(f"{i+1}. Runde:")
            print("-----------------------------------")
            try:
                player = int(input("1 Schere, 2 Stein, 3 Papier!\n"))
            except Exception:
                print("-----------------------------------")
                print(f"Der Spieler hat aufgegeben, die KI gewinnt!\nFehleingaben, also alle Eingaben außer 1 oder 2 oder 3\nzählen als Eingeständniss der Unfähigkeit des Spielers\nund führen zur sofortigen Aufgabe des Spiels!")
                exit("Spieler ist unfähig!")
            print("-----------------------------------")
            if player == 1:
                print("Spieler hat Schere!")
                print("KI hat Stein!")
                print("KI hat gewonnen!")
                print("-----------------------------------")
                ai_score += 1
                print(f"KI {ai_score}:{player_score} Spieler")
            elif player == 2:
                print("Spieler hat Stein!")
                print("KI hat Papier!")
                print("KI hat gewonnen!")
                print("-----------------------------------")
                ai_score += 1
                print(f"KI {ai_score}:{player_score} Spieler")
            elif player == 3:
                print("Spieler hat Papier!")
                print("KI hat Schere!")
                print("KI hat gewonnen!")
                print("-----------------------------------")
                ai_score += 1
                print(f"KI {ai_score}:{player_score} Spieler")
        print(f"Das Spiel ist beendet!\nDie KI hat mit {ai_score} zu {player_score} gewonnen!")
        print("Möchtest du nochmal spielen? j/n: ")
        end = input()
        if end != "j" and end != "J":
            exit("Spiel beendet!")


def ai_fair(player, player_score, ai_score):
    import random
    player_score = player_score
    ai_score = ai_score
    ai = random.randint(1,3)
    if player == 1:
        print("Spieler hat Schere!")
    elif player == 2:
        print("Spieler hat Stein!")
    elif player == 3:
        print("Spieler hat Papier!")
        
    if ai == 1:
        print("KI hat Schere!")
    elif ai == 2:
        print("KI hat Stein!")
    elif ai == 3:
        print("KI hat Papier!")
    
    if (player == 1 and ai == 1) or (player == 2 and ai == 2) or (player == 3 and ai == 3):
        print("Spieler und KI sind gleich!\nUnentschieden!")
        print("-----------------------------------")
    elif (player == 1 and ai == 2) or (player == 2 and ai == 3) or (player == 3 and ai == 1):
        print("KI hat gewonnen!")
        print("-----------------------------------")
        ai_score += 1
    else:
        print("Spieler hat gewonnen!")
        print("-----------------------------------")
        player_score += 1
    return player_score, ai_score


def ai_wins(player, player_score, ai_score):
    if player == 1:
        print("Spieler hat Schere!")
        print("KI hat Stein!")
        print("KI hat gewonnen!")
        print("-----------------------------------")
    elif player == 2:
        print("Spieler hat Stein!")
        print("KI hat Papier!")
        print("KI hat gewonnen!")
        print("-----------------------------------")
    elif player == 3:
        print("Spieler hat Papier!")
        print("KI hat Schere!")
        print("KI hat gewonnen!")
        print("-----------------------------------")
    ai_score += 1
    return player_score, ai_score


def play_rock_paper_scissors_mostly_fair():
    while True:
        print("Wie viele Runden möchtest du spielen?: ")
        rounds = input()
        print("-----------------------------------")
        try:
            rounds = int(rounds)
            if rounds <= 0:
                rounds = int("fool")
        except Exception:
            print(f"Bitte gib eine ganze Zahl ein, die größer als 0 ist und nicht {rounds}!")
            continue
        player_score = 0
        ai_score = 0
        for i in range(rounds):
            print(f"{i+1}. Runde:")
            print("-----------------------------------")
            try:
                player = int(input("1 Schere, 2 Stein, 3 Papier!\n"))
            except Exception:
                print("-----------------------------------")
                print(f"Der Spieler hat aufgegeben, die KI gewinnt!\nFehleingaben, also alle Eingaben außer 1 oder 2 oder 3\nzählen als Eingeständniss der Unfähigkeit des Spielers\nund führen zur sofortigen Aufgabe des Spiels!")
                exit("Spieler ist unfähig!")
            print("-----------------------------------")
            if player_score >= ai_score:
                player_score, ai_score = ai_wins(player, player_score, ai_score)
                print(f"KI {ai_score}:{player_score} Spieler")
            elif player_score < ai_score:
                player_score, ai_score = ai_fair(player, player_score, ai_score)
                print(f"KI {ai_score}:{player_score} Spieler")
        if player_score == ai_score:
            print(f"Das Spiel ist beendet!\nDie KI hat mit {ai_score} und der Spieler mit {player_score} unentschieden gespielt!")
        elif player_score < ai_score:
            print(f"Das Spiel ist beendet!\nDie KI hat mit {ai_score} zu {player_score} gewonnen!")
        elif player_score > ai_score:
            print(f"Das Spiel ist beendet!\nDer Spieler hat mit {player_score} zu {ai_score} gewonnen!")
        print("Möchtest du nochmal spielen? j/n: ")
        end = input()
        if end != "j" and end != "J":
            exit("Spiel beendet!")

print("Willkommen zu Schere, Stein, Papier!")
while right == False:
    print("Wie möchtest du spielen?:\n 1 Hohe Gewinn-Chance\n 2 Normale Gewinn-Chance")
    choice = input()
    print("-----------------------------------")
    try:
        choice = int(choice)
    except Exception:
        print(f"Gib die Zahl 1 oder 2 ein und nicht {choice}!")
        continue
    if choice == 1:
        play_rock_paper_scissors_mostly_fair()
        right = True
    elif choice == 2:
        play_rock_paper_scissors_totaly_unfair()
        right = True
    else:
        print(f"Gib die Zahl 1 oder 2 ein und nicht {choice}!")