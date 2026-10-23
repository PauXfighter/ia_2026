from tictac.victoria import victoria


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
        # S'ha acabat el joc si algú ha guanyat o si ja no queden caselles buides
        return self.guanyador() is not None or len(self.accions_possibles) == 0

    def guanyador(self) -> str | None:
        for linia in self.__obtenir_linies():
            if linia[0] != " " and linia[0] == linia[1] == linia[2]:
                return linia[0]
        return None

    def utilitat(self, jugador_max: str) -> int:
        guanya = self.guanyador()
        rival = "0" if jugador_max == "X" else "X"
        if guanya == jugador_max:
            return 1
        elif guanya == rival:
            return -1
        return 0

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

    def __obtenir_linies(self) -> list[list[str]]:
        linies = []
        # 3 files
        for fila in self.taulell: linies.append(fila)

        # 3 columnes
        for c in range(self.mida):
            linies.append([self.taulell[f][c] for f in range(self.mida)])
        # 2 diagonals
        diagonal_principal = [self.taulell[i][i] for i in range(3)]
        diagonal_secundaria = [self.taulell[i][(self.mida-1) - i] for i in range(3)]
        linies.append(diagonal_principal)
        linies.append(diagonal_secundaria)

        return linies
