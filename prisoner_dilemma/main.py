#!/usr/bin/env python2

import dilemma
import team1 as t1
import team2 as t2
import team3 as t3
import team4 as t4

def getPrisonerInstance(team):
    if(team == 1):
        return t1.Prisoner1()
    elif(team == 2):
        return t2.Prisoner2()
    elif(team == 3):
        return t3.Prisoner3()
    elif(team == 4):
        return t4.Prisoner4()
  
 
games = 10000

def main():
    print("PORGOR Prisoner dilemma")
    results = [0,0,0,0]
    for i in range(1, 5):
        for j in range(i+1, 5):
            if(i != j):
                tmp = dilemma.playMatch(getPrisonerInstance(i), getPrisonerInstance(j), games)
                print("Match {} vs {} -- {}:{}".format(i, j, tmp[0], tmp[1]))
                results[i - 1] += tmp[0]
                results[j - 1] += tmp[1]
                #print("results: {}".format(results))
    print results
    return 0

main()