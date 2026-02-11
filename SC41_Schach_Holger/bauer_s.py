# Bauer schwarz

from figur import Figur


class Bauer_s(Figur):

    def __init__(self, pos: str):
        super().__init__(pos)

    def __str__(self):
        return "Bauer schwarz@" + Figur.position(self.spalte, self.reihe)

    def find_moves(self):
        if self.reihe == 2:
            offsets = [
                (0, 1),
                (0, 2),
            ]
        else:
            offsets = [
                (0, 1)
            ]
        positions = []
        for soff, roff in offsets:
            newpos = Figur.position(self.spalte + soff, self.reihe + roff)
            if newpos:
                positions += [newpos]
        return positions
