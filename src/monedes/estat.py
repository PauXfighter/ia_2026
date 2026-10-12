import copy

SOLUCIO = " XXXC"


class Estat:

    def __init__(self, info, pes: int, cami_previ: list = None):
        if cami_previ is None:
            cami_previ = []

        self.pes = pes
        self.cami = cami_previ
        self.__info = info

    def es_meta(self) -> bool:
        es_meta = True
        for moneda, sol in zip(self.__info, SOLUCIO):
            es_meta = es_meta and (moneda == sol)

        return es_meta

    @staticmethod
    def gira(moneda):
        if moneda == "X":
            return "C"
        elif moneda == "C":
            return "X"
        else:
            return " "

    def transicio(self, acc):
        nou_estat = copy.deepcopy(self)
        acc, pos = acc
        pes = 0
        if acc == "G":
            nou_estat.__info[pos] = Estat.gira(nou_estat.__info[pos])
            pes = 1
        elif acc == "D" or acc == "B":
            moneda = nou_estat.__info[pos]
            if acc == "B":
                moneda = Estat.gira(moneda)

            nou_estat.__info[self.__info.index(" ")] = moneda
            nou_estat.__info[pos] = " "
            pes = 2

        return nou_estat, pes

    @property
    def accions_possibles(self):
        acc_possibles = []
        blanc = self.__info.index(" ")
        # Feim totes les accions possibles i les fiquem al hash
        # Girem totes les monedes
        for pos in range(0, 5):
            if pos != blanc:
                acc_possibles.append(("G", pos))
        # Desplacem totes les monedes possibles
        for desp in (1, -1):
            if 0 <= (blanc + desp) < 5:
                acc_possibles.append(("D", (blanc + desp)))
        # Feim botar les monedes que puguin
        for desp in (2, -2):
            if 0 <= (blanc + desp) < 5:
                acc_possibles.append(("B", (blanc + desp)))
        return acc_possibles

    def genera_fills(self):
        fills = []
        # A partir de les accions posibles, anem generant els fills de l'estat que ens donen
        for acc in self.accions_possibles:
            estat_fill, pes = self.transicio(acc)
            estat_fill.cami.append(acc)
            estat_fill.pes += pes

            fills.append(estat_fill)

        return fills

    def calc_heuristica(self):
        pos = self.__info.index(" ")
        heuristica = 0
        for lletra_es, lletra_sol in zip(self.__info, SOLUCIO):
            if lletra_sol != " ":
                heuristica += int(lletra_es != lletra_sol)

        heuristica += pos

        return heuristica + self.pes