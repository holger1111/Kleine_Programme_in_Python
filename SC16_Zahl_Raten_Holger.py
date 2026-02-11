# DIFFICULTY: 2
# Der PC wählt eine Zahl zwischen 1 und 100. 
# Du gibst eine Zahl ein und bekommst die Info, ob sie richtig, zu hoch oder
# zu niedrig ist.
# Danach wiederholt sich das Ganze, bist du die Zahl richtig geraten hast.
#
# TASK: Schreibe ein Programm, was dieses Zahlen-Raten-Spiel umsetzt.

import random


def human_guess(counter, ai_number, max_try, min_num, max_num):
    guess = input("Spieler rät: ")
    try:
        guess = int(guess)
        if guess > 100 or guess <= 0:
            guess = int("fool")
    except Exception:
        print(f"Bitte gib eine Zahl zwischen 1 und 100 ein und nicht {guess}")
        print("-----------------------------------")
    if guess == ai_number:
        print(f"Du hast die Zahl der KI {ai_number} mit {counter + 1} von {max_try} Versuchen richtig erraten!")
        print("-----------------------------------")
        exit("Spieler hat gewonnen!")
    elif guess > ai_number:
        print(f"Du has die Zahl der KI nicht richtig erraten, deine Zahl {guess} ist zu groß!")
        print("-----------------------------------")
    elif guess < ai_number:
        print(f"Du has die Zahl der KI nicht richtig erraten, deine Zahl {guess} ist zu klein!")
        print("-----------------------------------")
    return counter, ai_number, max_try, min_num, max_num, guess


def ai_guess(counter, number, max_try, min_num, max_num):
    guess_ai = random.randint(min_num, max_num)
    print(f"KI rät: {guess_ai}")
    if guess_ai == number:
        print(f"Die KI hat deine Zahl {number} mit {counter + 1} von {max_try} Versuchen richtig erraten!")
        print("-----------------------------------")
        exit("KI hat gewonnen!")
    elif guess_ai > number:
        print(f"Die KI hat deine Zahl nicht richtig erraten, ihre Zahl {guess_ai} ist zu groß!")
        print("-----------------------------------")
        max_num = guess_ai - 1
    elif guess_ai < number:
        print(f"Die KI hat deine Zahl nicht richtig erraten, ihre Zahl {guess_ai} ist zu klein!")
        print("-----------------------------------")
        min_num = guess_ai + 1
    return counter, number, max_try, min_num, max_num, guess_ai


def play_guess_numbers_human():
    min_num = 0
    max_num = 100
    max_try = 10
    counter = 0
    ai_number = random.randint(min_num, max_num)
    print(f"Die KI hat eine ganze Zahl zwischen {min_num} und {max_num} ausgewählt.\nVersuche, sie zu erraten!\nDu hast {max_try} Versuche!")
    print("-----------------------------------")
    while counter <= 10:
        if counter == 10:
            print("Du hast alle Versuche verbraucht!")
            exit("Spieler hat verloren!")
        print(f"Versuch {counter + 1} von {max_try}:")
        counter, ai_number, max_try, min_num, max_num, guess = human_guess(counter, ai_number, max_try, min_num, max_num)
        counter += 1


# play_guess_numbers_human()


def play_guess_numbers_ai():
    min_num = 0
    max_num = 100
    is_valid = False
    max_try = 10
    counter = 0
    print(f"Du darfst eine ganze Zahl zwischen {min_num} und {max_num} auswählen und die KI versucht, sie zu erraten:")
    while is_valid == False:
        number = input()
        try:
            number = int(number)
            if number > 100 or number <= 0:
                number = int("fool")
            else:
                is_valid = True
        except Exception:
            print(f"Bitte gib eine ganze Zahl zwischen {min_num} und {max_num} ein und nicht {number}!")
            print("-----------------------------------")
    counter = 0
    print(f"Deine Zahl ist {number}. Die KI hat {max_try} Versuche, um sie zu erraten!")
    while counter <= 10:
        if counter == 10:
            print("Die KI hat alle Versuche verbraucht!")
            exit("Spieler hat gewonnen!")
        print(f"Versuch {counter + 1} von {max_try}:")
        counter, number, max_try, min_num, max_num, guess_ai = ai_guess(counter, number, max_try, min_num, max_num)
        counter += 1

# play_guess_numbers_ai()


def play_guess_numbers_ai_vs_human():
    min_num = 0
    max_num = 100
    is_valid = False
    ai_start = True
    max_try = 10
    counter2 = 0
    list_human = list()
    list_ai = list()
    print(f"Du darfst eine ganze Zahl zwischen {min_num} und {max_num} auswählen:")
    while is_valid == False:
        number = input()
        try:
            number = int(number)
            if number > 100 or number <= 0:
                number = int("fool")
            else:
                is_valid = True
        except Exception:
            print(f"Bitte gib eine ganze Zahl zwischen {min_num} und {max_num} ein und nicht {number}!")
            print("-----------------------------------")
    ai_number = random.randint(min_num, max_num)
    print(f"Die KI hat ebenfalls eine ganze Zahl zwischen {min_num} und {max_num} ausgewählt.\nVersuche, abwechseln mit der KI die Nummern zu erraten!\nJeder hat {max_try} Versuche!")
    print("-----------------------------------")
    while counter2 < 1:
        print("Gib eine ganze Zahl zwischen 1 und 10 ein.\nIst deine Zahl größer als die der KI, darfst du anfangen: ")
        choice = input()
        ai_choice = random.randint(1, 10)
        try:
            choice = int(choice)
            if choice < 1 or choice > 10:
                choice = int("fool")
            if ai_choice > choice:
                print("Die KI hat die größere Zahl und beginnt!")
            elif ai_choice < choice:
                print("Du hast die größere Zahl und beginnst!")
                ai_start = False
        except Exception:
            print(f"Du hast keine ganze Zahl zwischen 1 und 10 eingegen, sondern {choice}!\nDaher darf die KI anfangen!")
        counter2 += 1
    counter = 0
    while counter <= max_try:
        if counter == max_try:
            print("Alle Versuche verbraucht!")
            exit("Spieler und KI haben verloren!")
        print(f"Versuch {counter + 1} von {max_try}:")
        if ai_start == True:
            
            counter, number, max_try, min_num, max_num, guess_ai = ai_guess(counter, number, max_try, min_num, max_num)
            list_ai.append(guess_ai)
            
            counter, ai_number, max_try, min_num, max_num, guess = human_guess(counter, ai_number, max_try, min_num, max_num)
            list_human.append(guess)
        
        else:
            counter, ai_number, max_try, min_num, max_num, guess = human_guess(counter, ai_number, max_try, min_num, max_num)
            list_human.append(guess)
            
            counter, number, max_try, min_num, max_num, guess_ai = ai_guess(counter, number, max_try, min_num, max_num)
            list_ai.append(guess_ai)
            
        counter += 1


play_guess_numbers_ai_vs_human()