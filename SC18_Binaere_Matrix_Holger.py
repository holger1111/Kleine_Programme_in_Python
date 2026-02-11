# DIFFICULTY: 3
# Wir wollen alle binären Zahlen bis 255 als binäre Matrix abbilden:
"""
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1
0 0 0 0 0 0 1 0
0 0 0 0 0 0 1 1
0 0 0 0 0 1 0 0
...
...
...
1 1 1 1 1 0 1 1
1 1 1 1 1 1 0 0
1 1 1 1 1 1 0 1
1 1 1 1 1 1 1 0
1 1 1 1 1 1 1 1
"""

# TASK: Schreibe ein Programm, was diese Anforderung erfüllt. Achte dabei darauf, 
#       dass Leerzeichen eingefügt werden und die Matrizen korrekt aufsteigen sortiert sind.

def binary_matriz():
    start = 0
    end = 255
    line_list = list()
    line = "0 0 0 0 0 0 0 0"
    #       012345678901234
    for i in range(start, end + 1):
        line = ""
        if i < 10:
            line += "  " + str(i) + ": "
        elif i < 100:
            line += " " + str(i) + ": "
        elif i < 1000:
            line += "" + str(i) + ": "
        l1 = (i // 128) % 2
        line += " " + str(l1)
        l2 = (i // 64) % 2
        line += " " + str(l2)
        l3 = (i // 32) % 2
        line += " " + str(l3)
        l4 = (i // 16) % 2
        line += " " + str(l4)
        l5 = (i // 8) % 2
        line += " " + str(l5)
        l6 = (i // 4) % 2
        line += " " + str(l6)
        l7 = (i // 2) % 2
        line += " " + str(l7)
        l8 = str(i % 2)
        line += " " + str(l8)
        
        line_list.append(line)
        
    for i in range(len(line_list)):
        print(line_list[i])
        
binary_matriz()