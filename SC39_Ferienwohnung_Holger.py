# DIFFICULTY: 3
# TASK1: Schreibe ein Programm für einen Anbieter für Ferienwohnungen.
#        Der Klassenname soll "Wohnung" sein und die folgenden Infos enthalten:
#        1. Namen der Wohnung
#        2. Standort
#        3. Anzahl der Betten
#        4. Preis pro Übernachtung
#        Verwende hierbei private Attribute (mit __) und dazugehörige 
#        Getter & Setter.
#
# TASK2: Teste die Klasse, indem du einige Wohnungs-Objekte erzeugst und 
#        ihre Werte ausgibst.

class Wohnung:
    def __init__(self, name, place, bed, price):
        self.__name = name
        self.__place = place
        self.__bed = bed
        self.__price = price
        
    def get_name(self):
        print(f"Name: {self.__name}")
        return self.__name
    
    def set_name(self, new_name):
        print(f"Name alt: {self.__name}\nName neu: {new_name}")
        self.__name = new_name
    
    def get_place(self):
        print(f"Standort: {self.__place}")
        return self.__place
    
    def set_place(self, new_place):
        print(f"Standort alt: {self.__place}\nStandort neu: {new_place}")
        self.__place = new_place
    
    def get_bed(self):
        print(f"Betten: {self.__bed}")
        return self.__bed
    
    def set_bed(self, new_bed):
        print(f"Betten alt: {self.__bed}\nBetten neu: {new_bed}")
        self.__bed = new_bed
    
    def get_price(self):
        print(f"Preis pro Nacht: {self.__price} €")
        return self.__price
    
    def set_price(self, new_price):
        print(f"Preis pro Nacht alt: {self.__price} €\nPreis pro Nacht neu: {new_price} €")
        self.__price = new_price


w1 = Wohnung("Sonnenblick", "Freiburg", "5", "100.5")
w2 = Wohnung("Moosgrün", "Hochhausen", "19", "99.99")

w1.get_bed()
w2.get_place()

print(int(w1.get_bed()) * float(w1.get_price()))
print(float(w2.get_price()) + float(w1.get_price()))
