# Figur


class Figur:

    spalte: int
    reihe: int

    def __init__(self, pos: str):
        if len(pos) != 2:
            raise ValueError("Falsche Zeichenanzahl der Position!")
        s = pos[0].lower()
        r = pos[1]
        if (not pos[0].lower() in "abcdefgh") or (not pos[1] in "12345678"):
            raise ValueError("Ungültige Zeichen in der Position!")
        self.spalte = "abcdefgh".find(s)
        self.reihe = "12345678".find(r)

    # Liefert Schachnotation zurück
    @staticmethod
    def position(spalte: int, reihe: int) -> str:
        if reihe < 0 or reihe > 7 or spalte < 0 or spalte > 7:
            return ""
        return "abcdefgh"[spalte] + "12345678"[reihe]

    def __str__(self):
        return Figur.position(self.spalte, self.reihe)
