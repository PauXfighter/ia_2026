""" Fitxer que conté l'agent informat.

S'ha d'implementar el mètode:
    actua()
"""

from queue import PriorityQueue
from quiques.agent import Barca
from quiques.estat import Estat

class BarcaGreedy(Barca):
    def __init__(self):
        super(BarcaGreedy, self).__init__()
        self.__frontera = None
        self.__tancats = None
        self.__cami_exit = None

    def heuristica(self, estat: Estat) -> int:
        """
        Estima la distància fins a la meta.
        Comptem quants animals queden a l'esquerra.
        Com menys animals quedin, més a prop s'està de la solució.
        """
        return estat.quica_esq + estat.llops_esq

    def cerca(self, estat_inicial: Estat) -> bool:
        self.__frontera = PriorityQueue()
        self.__tancats = set()
        exit = False
        estat_actual = None
        comptador = 0  # Desempat si dues heurístiques són iguals

        self.__frontera.put((self.heuristica(estat_inicial), comptador, estat_inicial))
        while not self.__frontera.empty():
            _, _, estat_actual = self.__frontera.get()

            if estat_actual in self.__tancats or not estat_actual.es_segur():
                continue

            if estat_actual.es_meta():
                break

            self.__tancats.add(estat_actual)

            for f in estat_actual.genera_fill():
                if f not in self.__tancats and f.es_segur():
                    comptador += 1
                    prioritat = self.heuristica(f)
                    self.__frontera.put((prioritat, comptador, f))

        if estat_actual and estat_actual.es_meta():
            self.__cami_exit = estat_actual.cami
            exit = True

        return exit

    def actua(self, percepcio: dict) -> str | tuple[str, (int, int)]:
        if self.__cami_exit is None:
            estat_inicial = Estat(
                local_barca=percepcio["Lloc"],
                llops_esq=percepcio["Llop Esq"],
                polls_esq=percepcio["Poll Esq"],
            )

            self.cerca(estat_inicial)

        if self.__cami_exit:
            quiques, llops = self.__cami_exit.pop(0)
            return "M", (quiques, llops)
        else:
            return "A", None