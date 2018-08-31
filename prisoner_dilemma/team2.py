import prisoner
import random

class Prisoner2(prisoner.Prisoner):
    
    def __init__(self):
        print("Creating Prisoner by Team2")
        self.coopCounter = 0
    
    def talk(self):
        self.coopCounter += 1
        #print("Played {} games".format(self.coopCounter))
        return True
    
    def getResult(self, result):
        #print(result)
        i = 0