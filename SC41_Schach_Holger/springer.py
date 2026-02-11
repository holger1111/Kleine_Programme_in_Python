# Springer

from figur import Figur


class Springer(Figur):

    def __init__(self, pos: str):
        super().__init__(pos)

    def __str__(self):
        return "Springer@" + Figur.position(self.spalte, self.reihe)

    def find_moves(self):
        offsets = [
            (1, 2),
            (2, 1),
            (-1, 2),
            (-2, 1),
            (1, -2),
            (2, -1),
            (-1, -2),
            (-2, -1),
        ]
        positions = []
        for soff, roff in offsets:
            newpos = Figur.position(self.spalte + soff, self.reihe + roff)
            if newpos:
                positions += [newpos]
        return positions
