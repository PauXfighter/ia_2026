""" Fitxer que conté els diferents agents aspiradors.

Percepcions:
    "Loc": [0]
    "Net": [1]

Accions:
    AccionsAspirador.DRETA
    AccionsAspirador.ESQUERRA
    AccionsAspirador.ATURA
    AccionsAspirador.ASPIRA

Autor: Miquel Miró Nicolau (UIB), 2022
"""
import abc
from importlib.resources import files

import pygame

from iaLib import agent


class Aspirador(agent.Agent):
    def __init__(self):
        super().__init__(long_memoria=1)

    def pinta(self, display):
        img_path = files("aspirador.images") / "sprite.png"

        img = pygame.image.load(img_path)
        img = pygame.transform.scale(img, (100, 100))
        display.blit(img, self._posicio_pintar)

    @abc.abstractmethod
    def actua(self, percepcio):
        pass


class AspiradorTaula(Aspirador):
    TAULA = {
        (0, True): "A",
        (0, False): "D",
        (1, True): "A",
        (1, False): "E",
    }

    def actua(self, percepcio: dict):
        return AspiradorTaula.TAULA[
            (percepcio["Loc"], percepcio["Brut"])
        ]


class AspiradorReflex(Aspirador):
    def actua(self, percepcio: dict):
        if percepcio["Brut"]:
            return "A"
        else:
            if percepcio["Loc"] == 0:
                return "D"
            elif percepcio["Loc"]== 1:
                return "E"



class AspiradorMemoria(Aspirador):
    def __init__(self):
        super().__init__()
        self.estat_habitacions = {0: None, 1: None}
    def actua(self, percepcio: dict):
        loc=percepcio["Loc"]
        brut=percepcio["Brut"]
        self.estat_habitacions[loc] = brut
        if brut:
            return "A"
        # Determinar quina és l'altra habitació per consultar la memòria
        estat_altra = self.estat_habitacions[1 if loc == 0 else 0]

        # Decidir el moviment en funció de la informació addicional per saber quan aturar
        if estat_altra is False:
            return "S"
        # Si l'altre no ha estat visitada, ens movem
        elif estat_altra is None or estat_altra is True:
            return "D" if loc == 0 else "E"


