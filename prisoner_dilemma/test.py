#!/usr/bin/env python2

import prisoner
import random
import dilemma

class TestPrisoner(prisoner.Prisoner):
    def talk(self):
        return random.choice([True, False, False])
    
    def getResult(self, result):
        print(result)
     
def main():
    tp = TestPrisoner()
    mp = prisoner.Prisoner()
    res = dilemma.playMatch(tp, mp, 10)
    print("Match {} vs {} -- {}:{}".format(tp.__class__.__name__, mp.__class__.__name__, res[0], res[1]))
    
main()