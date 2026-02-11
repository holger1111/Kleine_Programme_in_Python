# DIFFICULTY: 3
# Für ein Event wollen wir eine Liste mit einer beliebigen Anzahl an Songs
# erstellen. Diese Liste soll folgende Struktur haben:
#   - Eine gesamte Liste, in der alle Songs vorhanden sind
#   - Eine Sub-Liste mit WarmUp-Songs, welche in der ersten Stunde gespielt werden.
#   - Eine Sub-Liste mit Ending-Songs, welche zum "Rauswerfen" am Ende gespielt werden.
#   - Die Listen sollen zur Übersicht alle alphabetisch sortiert sein, da aus ihnen 
#     am Ende zufällig ausgewählt wird.
# 
# TASK: Bilde die vorgegebene Listenstruktur mit deiner Auswahl an Songs ab. Teste ihre
#       Funktionalität, indem du dir jeweils einen Song aus der WarmUp-Liste, zwei aus der
#       "Haupt-"Liste und einen aus der Ending-Liste ausgeben lässt.

import random

warmup = ["A BCD EFG", "All the saints go marchin in"]
warmup.sort()
main = ["Dancing Queen", "Livin on a Prayer", "Eye of the Tiger", "Highway to Hell"]
main.sort()
ending = ["We all live in a yellow submarine", "Don't stop believin"]
ending.sort()
song_list = ["A BCD EFG", "All the saints go marchin in", "Dancing Queen", "Eye of the Tiger", "Highway to Hell", "Livin on a Prayer", "We all live in a yellow submarine", "Don't stop believin"]
song_list.sort()

print("Warmup Songs:")
for i in range(len(warmup)):
    print(str(i+1) + ". " + warmup[i])
print("Main Songs:")
for i in range(len(main)):
    print(str(i+1) + ". " + main[i])
print("Ending Songs:")
for i in range(len(ending)):
    print(str(i+1) + ". " + ending[i])
print("All Songs:")
for i in range(len(song_list)):
    print(str(i+1) + ". " + song_list[i])
print("---------------------------")


def play_random_warmup(amount):
    for x in range(amount):
        print("Warmup: " + random.choice(warmup))


def play_random_main(amount):
    for x in range(amount):
        print("Main: " + random.choice(main))


def play_random_ending(amount):
    for x in range(amount):
        print("Ending: " + random.choice(ending))


play_random_warmup(1)
play_random_main(2)
play_random_ending(1)


def add_song(name):
    song_list.append(name)
    song_list.sort()


def add_warmup(name):
    warmup.append(name)
    warmup.sort()


def add_main(name):
    main.append(name)
    main.sort()
    
    
def add_ending(name):
    ending.append(name)
    ending.sort()


def add_song_name():
    print("What kind of song do you want to add?\n1. WarmUp\n2. Main\n3. Ending")
    choice = int(input())
    print("Enter the song name:")
    name = input()
    if choice == 1:
        add_warmup(name)
        add_song(name)
    elif choice == 2:
        add_main(name)
        add_song(name)
    elif choice == 3:
        add_ending(name)
        add_song(name)

