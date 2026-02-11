# Turm

from figur import Figur


class Turm(Figur):

    def __init__(self, pos: str):
        super().__init__(pos)

    def __str__(self):
        return "Turm@" + Figur.position(self.spalte, self.reihe)

    def find_moves(self):
        position = []
        for i in range(-7, 8):
            if i == 0:
                continue
            # Horizontale
            newpos = Figut.position(self.spalte + i, self.reihe)
            if newpos:
                positions += [newpos]
            # Vertikale
            newpos = Figut.position(self.spalte, self.reihe + i)
            if newpos:
                positions += [newpos]

        return position
