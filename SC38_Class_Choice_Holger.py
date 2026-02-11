# DIFFICULTY: 2
# TASK1: Suche dir ein Objekt aus deiner Umgebung/Fantasie/einem Spiel/...
#        Schreibe für dieses Objekt eine Klasse, mit allen Kernelementen:
#           1. Konstruktor
#           2. Objekt-Attributen
#           3. Objekt-Methoden
#           4. Statisches Attribut
#           5. ToString-Methode __str__()
#           6. Getter & Setter
#
# TASK2: Erzeuge einige Objekte deiner Klasse, verändere sie und lasse sie wieder anzeigen.

class Muetze:
    # statische Attribute
    anzahl_muetzen = 0
    
    # Konstruktor
    def __init__(self, color, icon, material, size):
        self.color = color
        self.icon = icon
        self.material = material
        self.size = size
        Muetze.anzahl_muetzen +=1
    
    # Getter und Setter
    def get_color(self):
        print(f"Farbe: {self.color}")
        return self.color
    
    def set_color(self, new_color):
        print(f"Farbe alt: {self.color}\nFarbe neu: {new_color}")
        self.color = new_color
    
    def get_icon(self):
        print(f"Icon: {self.icon}")
        return self.icon
    
    def set_icon(self, new_icon):
        print(f"Icon alt: {self.icon}\nIcon neu: {new_icon}")
        self.icon = new_icon
    
    def get_material(self):
        print(f"Material: {self.material}")
        return self.material
    
    def set_material(self, new_material):
        print(f"Material alt: {self.material}\nMaterial neu: {new_material}")
        self.material = new_material

    def get_size(self):
        print(f"Größe: {self.size}")
        return self.size
    
    def set_size(self, new_size):
        print(f"Größe alt: {self.size}\nGröße neu: {new_size}")
        self.size = new_size
    
    # to String
    def __str__(self):
        return f"Mütze:\nFarbe: {self.color}\nIcon: {self.icon}\nMaterial: {self.material}\nGröße: {self.size}"
        


m1 = Muetze("Grün", "Ente", "Cord", "L")
m2 = Muetze("Blau", "Stern", "Denim", "M")

print(m1, m2)
print(f"Anzahl der Mützen: {Muetze.anzahl_muetzen}")
m2.set_icon("Maus")
