import copy

from victoria import victoria


class Estat:

    def __init__(self, taulell_actual: list = None, torn_actual: str = "X"):
        self.mida=3
        if taulell_actual is None:
            # Matriz 3x3 vacía
            self.taulell = [[" " for _ in range(self.mida)] for _ in range(self.mida)]
        else:
            self.taulell = taulell_actual

        self.torn = torn_actual

    def es_meta(self) -> bool:

        return self.hi_ha_guanyador() or len(self.accions_possibles) == 0

    def hi_ha_guanyador(self):
        for fila in range(self.mida):
            for col in range(self.mida):
                if self.taulell[fila][col] != " " and victoria(self.taulell, (fila, col)):
                    return True
        return False

    def transicio(self, acc):
        fila, col = acc
        nou_taulell = [fila_actual.copy() for fila_actual in self.taulell]
        nou_taulell[fila][col] = self.torn
        nou_torn = "0" if self.torn == "X" else "X"
        return Estat(taulell_actual=nou_taulell, torn_actual=nou_torn)


    @property
    def accions_possibles(self):
        return [
            (fila, col) for fila in range(self.mida) for col in range(self.mida) if self.taulell[fila][col] == " "
        ]

    def genera_fills(self):
        return [self.transicio(acc) for acc in self.accions_possibles]

    def calc_heuristica(self):
        pass