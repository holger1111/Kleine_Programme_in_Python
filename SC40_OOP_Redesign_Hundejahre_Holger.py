# DIFFICULTY: 3
# TASK: Suche dir eine vorherige Aufgabe aus den Skillchecks aus,
#       die du schon gelöst hast (z.B. Blackjack aus Welt 2). Schreibe
#       sie so um, dass sie auf den Grundkonzepten des OOP aufbaut.


# Aufgabe SC12_Hundejahre
# DIFFICULTY: 1
# Eine Faustformel, um Hundejahre in Menschenjahre umzurechnen, ist das Alter des
# Hundes mit 7 zu multiplizieren.
# Je nach Hundegröße und Rasse sieht die Umrechnung jedoch etwas anders aus,
# - Ein einjähriger Hund entspricht in etwa einem 14-jährigen Menschen.
# - 2 Jahre eines Hundes entsprechen 22 Jahre eines Menschen.
# - Ab dann entspricht ein Hundejahr jeweils 5 Menschenjahren.

# TASK: Schreibe ein Programm, das das Alter eines Hundes entgegennimmt und das
#       entsprechende Menschenalter ausgibt.


def transform_dog_years_to_human_years(dog_years):
    if dog_years == 1:
        print(f"Das Alter von {dog_years} Jahren entspricht 14 Hundejahren.")
    elif dog_years == 2:
        print(f"Das Alter von {dog_years} Jahren entspricht 22 Hundejahren.")
    elif dog_years > 2:
        human_years = 22 + (dog_years - 2) * 5
        print(f"Das Alter von {dog_years} Jahren entspricht {human_years} Hundejahren.")
    elif dog_years <= 0:
        print(f"{dog_years} ist ein ungültiges Hundealter.")


# transform_dog_years_to_human_years(dog_years=int(input("Gib das Alter des Hundes in Jahren ein: ")))


# OOP Redesign
class Hund:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_name(self):
        print(f"Name: {self.name}")
        return self.name

    def set_name(self, name):
        print(f"Name alt: {self.name}\nName neu: {name}")
        self.name = name

    @property
    def age(self):
        return self.__age

    def get_human_years(self):
        age = self.__age
        if age == 1:
            human_years = 14
        elif age == 2:
            human_years = 22
        elif age > 2:
            human_years = 22 + (age - 2) * 5
        return human_years

    def __str__(self):
        return f"Der Hund mit dem Namen {self.name} ist {self.__age} Jahre alt, bzw. {self.get_human_years()} Hundejahre."


h1 = Hund("Bello", 3)
h2 = Hund("Luna", 1)

print(f"{h1.get_human_years()} Hundejahre")
h2.get_name()
h1.set_name("Max")

print(h1)
print(h2)
