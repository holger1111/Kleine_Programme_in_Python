# DIFFICULTY: 4
# Happy Numbers sind Zahlen, die, wenn man sie durch die Summe
# der Quadrate ihrer Ziffern wiederholt teilt, irgendwann 1 ergeben.
#
# Zum Beispiel:
# 13 -> 1² + 3² = 10 -> 1² + 0² = 1
#
# TASK: Schreibe ein Programm, was eine eingegeben Zahl darauf
#       überprüft, ob sie eine Happy Number ist.
# ACHTUNG: Es kann zu Endlosschleifen kommen, für die du eine
#          passende Ausstiegsbedingung finden musst.


def try_happy_number(zahl):
    counter = 0
    max_counter = 100
    o_zahl = zahl
    while counter < max_counter:
        t = 0
        for x in str(zahl):
            temp = int(x)**2
            t += temp
        if t == 1:
            print(f"{o_zahl} ist nach {counter + 1} Versuchen eine 'happy number'!")
            return
        zahl = t
        counter += 1
    print(f"{o_zahl} ist nach {max_counter} Versuchen keine 'happy number'!")


try_happy_number(13)
try_happy_number(205)
try_happy_number(999)
try_happy_number(329)
try_happy_number(332)
try_happy_number(31)
