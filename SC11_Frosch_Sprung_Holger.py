# DIFFICULTY: 2
# Wir haben einen sehr "speziellen" Frosch vor uns, der eine
# 2.5m breite Straße überqueren will.
# Mit dem ersten Sprung legt er die erstaunliche Distanz von 
# einem Meter zurück, dann springt er wegen zunehmender Erschöpfung 
# mit jedem weiteren Schritt immer nur noch halb so weit wie vorher.
#
# Zum Beispiel:
# Sprung 1: 1m, Sprung 2: 0.5m, Sprung 3: 0.25m...
#
# TASK: Schreibe ein Programm, welches ermittelt, ob der Frosch je
#       die andere Straßenseite erreicht und wie viele Sprünge er 
#       dazu braucht.
# ACHTUNG: Du brauchst potentiell eine Ausstiegsbedingung, um die
#          Möglichkeit einer Endlosschleife zu vermeiden.


def frog_jump(distance):
    first_jump = 1.0
    last_jump = first_jump
    rest_distance = distance - first_jump
    jumpers = 1
    while rest_distance < distance:
        if jumpers == 20:
            print(f"Der Frosch schafft es nicht, mit {jumpers} Sprüngen die Straße zu überqueren.")
            print(f"Gesprungene Strecke: {distance - rest_distance}m")
            return
        next_jump = last_jump / 2
        rest_distance -= next_jump
        last_jump = next_jump
        jumpers += 1
        print(jumpers)
    print(f"Der Frosch braucht {jumpers} Sprünge, um die Straße zu überqueren.")


frog_jump(2.5)
