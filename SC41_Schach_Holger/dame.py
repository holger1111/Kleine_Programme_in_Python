# Dame

from figur import Figur


class Dame(Figur):

    def __init__(self, pos: str):
        super().__init__(pos)

    def __str__(self):
        return "Dame@" + Figur.position(self.spalte, self.reihe)

    def find_moves(self):
        positions = []
        for i in range(-7, 8):
            if i == 0:
                continue
            # Diagonale von links unten nach rechts oben
            newpos = Figur.position(self.spalte + i, self.reihe + i)
            if newpos:
                positions += [newpos]
            # Diagonale von rechts unten nach links oben
            newpos = Figur.position(self.spalte + i, self.reihe - i)
            if newpos:
                positions += [newpos]
            # Horizontale
            newpos = Figut.position(self.spalte + i, self.reihe)
            if newpos:
                positions += [newpos]
            # Vertikale
            newpos = Figut.position(self.spalte, self.reihe + i)
            if newpos:
                positions += [newpos]
        return positions
