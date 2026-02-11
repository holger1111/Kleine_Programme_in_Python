# DIFFICULTY: 4
# TASK: Erstelle eine Liste mit 50 Zufallszahlen zwischen 0 und 9.
#       Werte diese Liste anhand folgender Kriterien aus.
#       1. Summe aller Elemente
#       2. Anzahl des Elements 0
#       3. Position der ersten 0
#       Vermeide hierbei die Nutzung fertiger Listen-Methoden.

import random

random_list = list()

for i in range(50):
    x = random.randint(0,9)
    random_list.append(x)

sum_list = 0

for y in range(len(random_list)):
    sum_list += random_list[y]

print(f"Die Liste hat als Summe aller Elemente {sum_list}.")

summ_list_0 = random_list.count(0)
print(f"Die Zahl 0 kommt {summ_list_0} mal in der Liste vor.")

for z in range(len(random_list)):
    if random_list[z] == 0:
        print(f"Die erste 0 ist am Index {z}, also an der Stelle {z + 1}.")
        break