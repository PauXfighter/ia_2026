from aspirador import joc
from aspirador import agent

agents = [agent.AspiradorReflex()]

hab = joc.Aspirador(agents)
hab.comencar()