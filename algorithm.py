import numpy as np
from scipy.stats import pearsonr as cor

class PersonR():
    Fields = ["Estabelecer um ambiente de concentracao",
              "Aprofundamento por material teorico",
              "Estudo por meio de aulas complementares",
              "Estudo por discencia",
              "Curiosidade individual",
              "Estabelecimento de rotina",
              "Longos Periodos de Estudo",
              "Resolucao de problemas externos",
              "Tempo de antecedenta para assimilacao"]
    Results = {}
    def __init__(self, entry):
        self.entry = entry
    
    def similarityVector():

