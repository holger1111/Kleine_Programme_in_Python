# DIFFICULTY: 1
# Die kleinste positive Zahl, die durch alle Zahlen von 1 bis 10 ohne Rest teilbar 
# ist, ist die 2520.
#
# TASK: Schreibe ein Programm mit der die kleinste positive Zahl ermittelt wird,
#       die durch alle Zahlen von 1 bis zu einer übergebenen Zahl teilbar ist.
#
#
# TIP: Beginne zuerst mit einer kleineren Zahl und steigere diese danach zum Testen.
#      Teste dein Programm schließlich mit 40. Die geringste Zahl, die durch alle
#      Zahlen von 1 bis 40 teilbar ist, ist 5342931457063200.



# Erste Version, bei kleinen Zahlen funktional, bei 40 dauert es zu lang
def suche_kleinstes_gemeinsames_Vielfaches(zahl):
    x = 1
    while True:
        teiler_ok = True
        for i in range(1, zahl + 1):
            if x % i != 0:
                teiler_ok = False
                break
        if teiler_ok == True:
            print(x)
            break
        x += 1

# Zweiter Versucht mit der Hilfe von Benny zur Nutzung des kgv
def kleinstes_gemeinsames_Vielfaches(zahl1, zahl2):
    temp1 = zahl1
    temp2 = zahl2
    r = temp1 % temp2
    
    while r != 0:
        temp1 = temp2
        temp2 = r
        r = temp1 % temp2
    
    kgv = zahl1 * zahl2 // temp2
    return kgv

def suche_kleinstes_gemeinsames_Vielfaches2(zahl):
    x = 1
    
    for i in range(1, zahl + 1):
        x = kleinstes_gemeinsames_Vielfaches(x, i)
        
    print(f"KGV aller Zahlen 1 bis {zahl}: {x}")





suche_kleinstes_gemeinsames_Vielfaches2(40)
    