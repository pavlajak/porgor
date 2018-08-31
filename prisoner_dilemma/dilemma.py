results = {}
results[False, False] = [-1, -1]
results[False,  True] = [-3,  0]
results[True,  False] = [0,  -3]
results[True, True] = [-2, -2]

def play(p1, p2):
    #print("playing...")
    ch1 = p1.talk()
    ch2 = p2.talk()
    
    res = results[ch1, ch2]
    r1 = res[0]
    r2 = res[1]
    
    #print("{} talked? {} ({}), {} talked? {} ({}).".format(p1.__class__.__name__, ch1, r1, p2.__class__.__name__, ch2, r2))
    
    p1.getResult(r1)
    p2.getResult(r2)
    
    return res

def playMatch(p1, p2, games):
    #print("Playing match {} vs {}".format(p1.__class__.__name__, p2.__class__.__name__))
    res = [0,0]
    for x in range(0,games):
        tmp = play(p1, p2)
        res[0] += tmp[0]
        res[1] += tmp[1]
    return res