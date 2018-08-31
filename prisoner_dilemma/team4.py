import prisoner
import random

class Prisoner4(prisoner.Prisoner):
    
    def __init__(self):
        print("Creating Prisoner by Team4")    
    
    def talk(self):
        return random.choice([True, False, False])
    
    def getResult(self, result):
        #print(result)
        i = 0