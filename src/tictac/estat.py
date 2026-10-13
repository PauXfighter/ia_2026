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
        # S'ha acabat el joc si algú ha guanyat o si ja no queden caselles buides
        return self.guanyador() is not None or len(self.accions_possibles) == 0

    def guanyador(self) -> str | None:
        #R etorna X, 0 si algun d'ells ha guanyat, o None si ningú ha guanyat.
        for i in range(len(self.taulell)):
            for j in range(len(self.taulell[i])):
                fitxa = self.taulell[i][j]
                if fitxa in ("X", "0") and victoria(self.taulell, (i, j)):
                    return fitxa
        return None

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

    def calc_heuristica(self) -> int:
        # Si ja hem acabat la partida, tornem el valor extrem
        guanya = self.guanyador()
        if guanya == "X":
            return 100
        elif guanya == "0":
            return -100
        elif len(self.accions_possibles) == 0:
            return 0  # Empate

        puntuacio_x = 0
        puntuacio_0 = 0

        for linia in self.__obtenir_linies():
            # Cuenta cuántas fichas hay de cada tipo en la línea
            nums_x = linia.count("X")
            nums_0 = linia.count("0")

            # Línea viable para X (no contiene ningún 0)
            if nums_0 == 0:
                if nums_x == 2:
                    puntuacio_x += 10  # A punto de ganar
                elif nums_x == 1:
                    puntuacio_x += 1

            # Línea viable para 0 (no contiene ninguna X)
            if nums_x == 0:
                if nums_0 == 2:
                    puntuacio_0 += 10  # Rival a punto de ganar
                elif nums_0 == 1:
                    puntuacio_0 += 1

        # Restamos las puntuaciones tal como marca la teoría
        return puntuacio_x - puntuacio_0

    def __obtenir_linies(self) -> list[list[str]]:
        linies = []
        # 3 files
        for fila in self.taulell: linies.append(fila)

        # 3 columnes
        linies.append([self.taulell[f][c] for f in range(3) for c in range(3)])

        # 2 diagonals
        diagonal_principal = [self.taulell[i][i] for i in range(3)]
        diagonal_secundaria = [self.taulell[i][2 - i] for i in range(3)]
        linies.append(diagonal_principal)
        linies.append(diagonal_secundaria)

        return linies
