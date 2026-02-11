# DIFFICULTY: 2
# Wir wollen die folgenden Einheiten umrechnen. Dabei wollen wir lediglich eine Zahl
# eingeben, und dabei die Umrechnung in beide Richtungen erhalten.
# z.B. 100 -> Umrechnung von 100 Pfund zu Euro UND 100 Euro zu Pfund.
#
# 1. Kilometer und Meilen
# 2. Centimeter und Inches
# 3. Euro und Pfund
#
# Nutze Google (oder sonstige Resourcen) um an die benötigten Umrechnungen zu kommen 
# (aber nicht an den Code selbst).
#
# TASK: Schreibe ein Programm, welches die gewählte Zahleneingabe in beide Richtungen
#       umrechnet.
# TIP: Du kannst die verschiedenen Aufgabenteile auch mit einem einzelnen Input 
#      lösen, indem für jede Umrechnung die gleiche Zahl als Grundlage genommen wird.

def km_to_m(km):
    return km * 0.6214


def m_to_km(m):
    return m * 1.60934


def cm_to_inch(cm):
    return cm / 2.54


def inch_to_cm(inch):
    return inch * 2.54


def euro_to_pound(euro):
    return euro * 0.88


def pound_to_euro(pound):
    return pound / 0.88


while True:
    print("Enter a number to choose what you want to convert:\n1. kilometers to miles\n2. miles to kilometers\n3. centimeters to inches\n4. inches to centimeters\n5. euros to pounds\n6. pounds to euros")
    choice = int(input())
    if choice == 1:
        print("Enter kilometers:")
        km = float(input())
        m = round(km_to_m(km), 2)
        print(m, "miles")
        break
    elif choice == 2:
        print("Enter miles:")
        m = float(input())
        km = round(m_to_km(m), 2)
        print(km, "kilometers")
        break
    elif choice == 3:
        print("Enter centimeters:")
        cm = float(input())
        inch = round(cm_to_inch(cm), 2)
        print(inch, "inches")
        break
    elif choice == 4:
        print("Enter inches:")
        inch = float(input())
        cm = round(inch_to_cm(inch), 2)
        print(cm, "centimeters")
        break
    elif choice == 5:
        print("Enter euros:")
        euro = float(input())
        pound = round(euro_to_pound(euro), 2)
        print(pound, "pounds")
        break
    elif choice == 6:
        print("Enter pounds:")
        pound = float(input())
        euro = round(pound_to_euro(pound), 2)
        print(euro, "euros")
        break
    else:
        print("Invalid choice")

