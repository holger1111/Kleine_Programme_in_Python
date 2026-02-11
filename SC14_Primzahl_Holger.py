# DIFFICULTY: 4
# Eine Primzahl ist immer nur durch 1 und sich selbst teilbar.
#
# TASK: Schreibe ein Programm, was alle Primzahlen zwischen zwei eingegeben
#       Zahlen ausgibt.


def find_prime():
    prime_start = int(input("Gib die untere Grenze ein:\n"))
    prime_end = int(input("Gib die obere Grenze ein:\n"))
    prime_list = list()
    prime_current = prime_start
    for i in range(prime_start, prime_end + 1):   
        is_prime = True
        if prime_current > 1:
            for x in range(2, prime_current):
                if prime_current % x == 0:
                    is_prime = False
        else:
            is_prime = False
        if is_prime != False:
            prime_list.append(prime_current)
        prime_current += 1
    print(f"Im Bereich von {prime_start} bis {prime_end} sind {len(prime_list)} Primzahlen, und zwar folgende:\n{prime_list}")
    
    
find_prime()