import copy
import json
import random
import string
from importlib.resources import files

from genetic import nlp

ALFABET = list(string.ascii_lowercase)
LONG_ALFABET = len(ALFABET)

class Individu:
    
    # Desar el diccionari en un fitxer
    __path = files("genetic") / "bigrama.json"
    with open(__path, "r", encoding="utf-8") as file:
        BIGRAMES = json.load(file)

    def __init__(self, clau = None, aleatori=False):


        if clau is None and not aleatori:
            clau = [None] * LONG_ALFABET
        elif clau is None:
            alfabet = copy.deepcopy(ALFABET)
            random.shuffle(alfabet)
            clau = alfabet
            
        self.clau = clau
        self.__fitness = None

    def __getitem__(self, index):
        if not isinstance(index, (int, slice)):
            raise KeyError("La clau de la classe Estat ha de ser un enter o un slice")
        
        return self.clau[index]

    def __setitem__(self, key, value):
        self.reset_fitness()
        if not isinstance(key, (int, slice)):
            raise KeyError("La clau de la classe Estat ha de ser un enter o un slice")

        self.clau[key] = value

    def __contains__(self, item):
        return item in self.clau

    def __len__(self):
        return len(self.clau)

    def reproduccio(self, pare2):
        inici, final = sorted(random.sample(range(LONG_ALFABET), 2))

        fill = Individu()
        fill[inici:final] = self[inici:final]
        
        p2_index = 0
        for i in range(LONG_ALFABET):
            if fill[i] is None:
                while pare2[p2_index] in fill:
                    p2_index += 1
                fill[i] = pare2[p2_index]
        
        return fill


    def mutacio(self):
        mutat = copy.deepcopy(self)
        
        idx1, idx2 = random.sample(list(range(LONG_ALFABET)), 2)
        mutat[idx1], mutat[idx2] = mutat[idx2], mutat[idx1]

        return mutat

    def desxifra(self, texts):
        desxifrats = []
        for text in texts:
            trans = str.maketrans("".join(self.clau), "".join(ALFABET)) # type: ignore
            text_str = "".join(text)

            desxifrat = text_str.translate(trans)
            desxifrats.append(desxifrat)
        

        return " ".join(desxifrats)

    def fitness(self, text):
        fitness = self.__fitness

        if fitness is None:
            # Create translation map
            decrypted = self.desxifra(text)
            prediccio = nlp.calcular_bigrames_lletres(decrypted)
            
            score = 0.0

            for bigrama, frequencia in prediccio.items():
                gt = 0
                if bigrama in self.BIGRAMES:
                    gt = self.BIGRAMES[bigrama] 
                
                score += abs(gt - frequencia)
            fitness = score
            self.__fitness = fitness
        
        return fitness

    def reset_fitness(self):
        self.__fitness = None