import numpy as np
from scipy.stats import pearsonr

class PersonR():
    Results = {}
    def __init__(self, entry):
        self.entry = entry
    
    def printResults(self):
        for result in self.Results:
            print(f"Para o usuario")
