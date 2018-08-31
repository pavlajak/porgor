import prisoner
import random

class Prisoner3(prisoner.Prisoner):
    
    def __init__(self):
        print("Creating Prisoner by Team3")    
    
    def talk(self):
        return random.choice([True, True, False])
    
    def getResult(self, result):
        #print(result)
        i = 0