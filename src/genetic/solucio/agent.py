""" Solució a la decodificació d'una cadena de caràcters emprant algoritmes genètics.

Author: Miquel Miró Nicolau (UIB), 2026
"""

import random

from iaLib import agent
from tqdm import tqdm

from genetic.solucio.individu import Individu

MIDA_POBLACIO = 600
GENERACIONS = 300
RATI_MUTACIO = 0.2

class Genetic(agent.Agent):
    def __init__(self):
        super().__init__(long_memoria=1)

    def pinta(self, display):
        print(self._posicio_pintar)

    def actua(self, percepcio: dict) -> tuple[str, (int, int)]:
        text_xifrat = percepcio["text"]
        poblacio = [Individu(aleatori=True) for _ in range(MIDA_POBLACIO)]

        pbar = tqdm(range(GENERACIONS), desc="Generacions")
        for _ in pbar:
            poblacio = sorted(poblacio, key=lambda e: e.fitness(text_xifrat))
            pbar.set_postfix_str(f"{round(poblacio[0].fitness(text_xifrat), 3)} - {poblacio[0].desxifra(text_xifrat)}")

            nova_poblacio = []
            while len(nova_poblacio) < MIDA_POBLACIO:
                poblacio = poblacio[:int(MIDA_POBLACIO // 3)]
                p1, p2 = random.choices(poblacio, k=2)
                fill = p1.reproduccio(p2)

                if random.random() < RATI_MUTACIO:
                    fill = fill.mutacio()

                nova_poblacio.append(fill)
            poblacio = nova_poblacio

            # print(millor.fitness(text_xifrat), millor.desxifra(text_xifrat))
        millor = min(poblacio, key=lambda e: e.fitness(text_xifrat))

        return millor.desxifra(text_xifrat)