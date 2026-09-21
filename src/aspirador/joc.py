from iaLib import agent, joc

class Aspirador(joc.JocNoGrafic):

    def __init__(self, agents: list[agent.Agent] | None = None):
        if agents is None:
            agents = []
        super(Aspirador, self).__init__(agents=agents)
        self.habitacions=[True, True]
        self.posicio_esquerra=True


    def _draw(self):
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
        return posicio, self.habitacions[posicio]


    def _aplica(self, accio, params=None, agent_actual=None):
        # TODO
        pass

