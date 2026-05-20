# small program to find best combination of available resistors to match a given value
resistors = [15,22,33,47,68,100,150,220,330,470,680,1000,1500,2200,3300,4700,6800,10000,15000,22000,33000,47000,68000,100000,150000,220000,330000,470000]

def distance(a,b):
    if a>b:
        return a/b - 1
    else:
        return b/a - 1

def bestcombo(targetvalue):
    combos = []
    for a in resistors:
        combos.append([a])
        for b in resistors:
#            combos.append(["s",a,b,a+b])
            combos.append(["p",a,b,1/(1/a+1/b)])
            for c in resistors:
                combos.append(["p",a,b,c,1/(1/a+1/b+1/c)])
                
    best = None    
    for x in combos:
        if best==None or distance(x[len(x)-1],targetvalue)<distance(best[len(best)-1],targetvalue):
            best = x
    return best

print(bestcombo(3344))
print(bestcombo(1703))
print(bestcombo(8771))
print(bestcombo(564))
print(bestcombo(713))
