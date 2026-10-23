""" Agent Minimax.

Mòdul en el qual es desenvolupa un agent Minimax amb poda alfa-beta per resoldre el problema del
Tic Tac Toe.

Creat per: Miquel Miró Nicolau (UIB), 2024
"""
from iaLib import agent
from tictac.estat import Estat



class Agent(agent.Agent):
    def __init__(self, poda = True):
        super(Agent, self).__init__(long_memoria=1)
        self.__visitats = None
        self.__cami_exit = None
        self.__poda = poda

    def cerca(self, estat: Estat, alpha, beta, torn_max=True, jugador_max: str = "X") -> int:
        if estat.es_meta():
            return estat.utilitat(jugador_max)

        if torn_max:
            max_eval = -float("inf")
            for fill in estat.genera_fills():
                punt = self.cerca(fill, alpha, beta, False, jugador_max)
                max_eval = max(max_eval, punt)
                alpha = max(alpha, punt)
                if self.__poda and alpha >= beta:
                    break  # Poda beta
            return max_eval

        else:
            min_eval = float("inf")
            for fill in estat.genera_fills():
                punt = self.cerca(fill, alpha, beta, True, jugador_max)
                min_eval = min(min_eval, punt)
                beta = min(beta, punt)
                if self.__poda and alpha >= beta:
                    break  # Poda alfa
            return min_eval

    def actua(self, percepcio: dict):
        torn_actual = percepcio["torn"]
        estat_actual = Estat(
            taulell_actual=percepcio["taulell"], torn_actual=torn_actual
        )

        accions = estat_actual.accions_possibles
        if not accions or estat_actual.es_meta():
            return "E", None

        millor_accio = None
        millor_valor = -float("inf")
        alpha = -float("inf")

        for acc in accions:
            fill = estat_actual.transicio(acc)
            valor = self.cerca(
                fill,
                alpha=alpha if self.__poda else -float("inf"),
                beta=float("inf"),
                torn_max=False,
                jugador_max=torn_actual,
            )

            if valor > millor_valor:
                millor_valor = valor
                millor_accio = acc
                alpha = max(alpha, valor)

        if millor_accio is not None:
            return "P", millor_accio
        return "E", None
