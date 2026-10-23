import copy
import json
import random
import string
from genetic import nlp

class Individu:
    def __init__(self, text):
        self.clau = list(string.ascii_lowercase)
        random.shuffle(self.clau)
        self.text=text

    def descifra(self):

