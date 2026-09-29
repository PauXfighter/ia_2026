""" Fitxer que conté l'agent informat.

S'ha d'implementar el mètode:
    actua()
"""

from quiques.agent import Barca
from quiques.estat import Estat


class BarcaGreedy(Barca):
    def __init__(self):
        super(BarcaGreedy, self).__init__()

    def actua(self, percepcio: dict) -> tuple[str, (int, int)]:
        pass
