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


transform_dog_years_to_human_years(dog_years=int(input("Gib das Alter des Hundes in Jahren ein: ")))
