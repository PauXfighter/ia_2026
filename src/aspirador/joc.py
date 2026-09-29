import sys
from xmlrpc.client import Boolean

from iaLib import agent, joc
import random

class AspiradorRomput(Exception):
    def __init__(self):
        self.message = "L'aspirador ha caigut i s'ha romput"
        super().__init__(self.message)

class Aspirador(joc.JocNoGrafic):

    def __init__(self, agents: list[agent.Agent] | None = None):
        if agents is None:
            agents = []
        super(Aspirador, self).__init__(agents=agents)
        self.habitacions=[Boolean(random.randint(0,1)), Boolean(random.randint(0,1))]
        self.posicio_esquerra=Boolean(random.randint(0,1))


    def _draw(self):
        # True = Bruta, False = Neta
        estat_esquerra = "Bruta" if self.habitacions[0] else "Neta"
        estat_dreta = "Bruta" if self.habitacions[1] else "Neta"

        # Determinamos de forma visual dónde está el aspirador
        asp_esquerra = " <--- [ASPIRADOR]" if self.posicio_esquerra else ""
        asp_dreta = " <--- [ASPIRADOR]" if not self.posicio_esquerra else ""

        # Imprimimos el estado por pantalla de forma sencilla y clara
        print("\n--- ESTAT ACTUAL DE L'ENTORN ---")
        print(f"Habitació Esquerra: [{estat_esquerra}]{asp_esquerra}")
        print(f"Habitació Dreta:    [{estat_dreta}]{asp_dreta}")
        print("--------------------------------\n")
        pass


    def percepcio(self):
        posicio=0 if self.posicio_esquerra else 1
        return {"Loc": posicio, "Brut": self.habitacions[posicio]}

    def _aplica(self, accio, params=None, agent_actual=None):
        if accio == "A":
            self.habitacions[0 if self.posicio_esquerra else 1] = False
        elif accio == "D":
            if not self.posicio_esquerra:
                raise AspiradorRomput
            self.posicio_esquerra = False
        elif accio == "E":
            if self.posicio_esquerra:
                raise AspiradorRomput
            self.posicio_esquerra = True
        elif accio == "S":
            sys.exit()
        else:
            raise Exception(f"Acció no existent en aquest joc: {accio}")

        if not self.habitacions[0] and not self.habitacions[1]:
            print("¡Enhorabona! Ambdues habitacions estan netes. Fi del joc.")

