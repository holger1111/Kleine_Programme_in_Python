# DIFFICULTY: 1
# Wir brauchen ein kleines Programm, was uns eine Begrüßung abhängig der 
# aktuellen Uhrzeit ausgibt.

# 22:00 - 05:00: Gute Nacht!
# 05:00 - 11:00: Guten Morgen!
# 11:00 - 15:00: Mahlzeit!
# 15:00 - 18:00: Guten Nachmittag!
# 18:00 - 22:00: Guten Abend!

# TASK: Schreibe ein Programm, was eine der Uhrzeit entsprechende Begrüßung ausgibt. 
#       Teste mit random und/oder input.

import time

current_time = time.localtime()
hour = current_time.tm_hour

def greeting_input():
    print("Please enter the current hour (0-24):")
    hour = int(input())
    greeting_current(hour)

def greeting_current(hour):
    if 0 <= hour < 5 or 22 <= hour <= 24:
        print("Gute Nacht!")
    elif 5 <= hour < 11:
        print("Guten Morgen!")
    elif 11 <= hour < 15:
        print("Mahlzeit!")
    elif 15 <= hour < 18:
        print("Guten Nachmittag!")
    elif 18 <= hour < 22:
        print("Guten Abend!")
    else:
        print("Du bist nicht willkommen.")
        
        

greeting_current(hour)