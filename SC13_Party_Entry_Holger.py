# DIFFICULTY: 1
# Bei einem Club soll am Einlass auf gewisse Faktoren geachtet werden, um
# zu entscheiden, ob ein*e Besucher*in Einlass bekommt und welches Armband
# diese*r bekommt.
#
# Dabei gelten die folgenden Einlassregeln, welche mit farbigen Armbändern 
# erkennbar gemachtg werden:
# 1. Unter 16: kein Einlass
# 2. Unter 18: blaues Armband, beschränkter Ausschank
# 3. Ab 18: rotes Armband, voller Ausschank
# 4. VIP: goldenes Armband, Zugang zum VIP Bereich
# 5. Mitarbeiter: violettes Armband, Zugang zu Employee-Only Bereichen
#
# TASK: Schreibe ein Programm, dass diese Faktoren überprüft und dem/der 
#       Besucher*in das entsprechende Armband ausstellt.

def party_entry(age=int(input("Wie alt bist du?: ")), is_vip=input("Bist du VIP? j/n: "), is_employee=input("Bist du Mitarbeiter? j/n: ")):
    
    if age < 16:
        print("Du bekommst kein Armband, weil du keinen Einlass bekommst!")
    elif is_vip == "j" or is_vip == "J":
        print("Du bekommst ein goldenes Armband und Zugang zum VIP-Bereich!")
    elif is_employee == "j" or is_employee == "J":
        print("Du bekommst ein violettes Armband und Zugang zum Employee-Only-Bereich!")
    elif age < 18:
        print("Du bekommst ein blaues Armband und hast beschränkten Ausschank!")
    elif age >= 18:
        print("Du bekommst das rote Armband und vollen Ausschank!")
    else:
        print("Du bekommst keinen Einlass, weil du falsche Angaben gemacht hast!")
        
party_entry()
    