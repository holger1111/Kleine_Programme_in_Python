# DIFFICULTY: 5
# Um unsere Playlist noch praktischer zu gestalten, wollen wir jetzt mehr Infos hinzufügen.
# Das könnten sein:
#   - Artist: wer hat den Song performed?
#   - Album: in welchem Album findet man den Song?
#   - Laufzeit: wie lange ist der Song?
#   - Link: z.B. ein Youtube-Link zum Song
# 
# TASK: Erweitere deine Liste aus "C6_Song_List.py" als Dictionaries für die Songs, in welchen
#       jeweils relevante (wähle max. 2) Meta-Daten zu jedem Song hinterlegt sind.
#       Wir wollen also eine Liste, mit drei Sub-Listen, die jeweils Dictionaries enthalten.
#       Teste wieder, indem du dir jeweils einen Song aus der WarmUp, zwei aus der Main, einen
#       aus der Ending-Liste ausgibst; aber diesmal mit verschiedenen Meta-Daten Ausgaben.
# TIP: Das Sortieren lassen wir hier erstmal aus.

import random


warmup = ["A BCD EFG", "All the saints go marchin thin"]
main = ["Dancing King", "Living as a Slayer", "Eye on the Lion", "Backstreets to Heaven"]
ending = ["We all live in a pink airmachine", "Don't stop recieving"]

dict_warmup = {"A BCD EFG": ["DC/CD", "Learn to speak"], "All the saints go marchin thin": ["Exolence", "Marching diet"]}
dict_main = {"Dancing King": ["BABA", "Synthetic Wisdom"], "Living as a Slayer": ["Barbie S.", "Work a life balance"], "Eye on the Lion": ["Wiht Sharks", "Story of the Animals"], "Backstreets to Heaven": ["RodStocks", "Live Tour"]}
dict_ending = {"We all live in a pink airmachine": ["Bugs", "Classic Flight"], "Don't stop recieving": ["Abitrage Slackers", "Slack the heck"]}


def play_random_warmup(amount):
    print("\nWarmup:")
    for x in range(amount):
        song = random.choice(warmup)
        interpret, album = dict_warmup[song]
        print(f"Song: {song}\nInterpret: {interpret}\nAlbum: {album}\n-----------------------")


def play_random_main(amount):
    print("\nMain:")
    for x in range(amount):
        song = random.choice(main)
        interpret, album = dict_main[song]
        print(f"Song: {song}\nInterpret: {interpret}\nAlbum: {album}\n-----------------------")


def play_random_ending(amount):
    print("\nEnding:")
    for x in range(amount):
        song = random.choice(ending)
        interpret, album = dict_ending[song]
        print(f"Song: {song}\nInterpret: {interpret}\nAlbum: {album}\n-----------------------")
        
        
play_random_warmup(1)
play_random_main(2)
play_random_ending(1)
