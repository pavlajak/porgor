import prisoner
import random

class Prisoner1(prisoner.Prisoner):
    
    def __init__(self):
        print("Creating Prisoner by Team1")    
    
    def talk(self):
        return random.choice([True, True, True, True, False, False])
    
    def getResult(self, result):
        #print(result)
        i = 0
