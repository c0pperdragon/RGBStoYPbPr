# small program to find best combination of resistors in my store to match a given value
resistors = [
    75,91,
    100,130,150,180,270,330,340,390,402,470,499,560,680,
    1000,1370,1500,2200,2700,3300,4020,4700,5490,6800,8060,
    10000,16020,
    100000,220000,
]

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
            combos.append([a,b,1/(1/a+1/b)])
            for c in resistors:
                combos.append([a,b,c,1/(1/a+1/b+1/c)])
    best = None    
    for x in combos:
        if best==None or distance(x[len(x)-1],targetvalue)<distance(best[len(best)-1],targetvalue):
            best = x
    return best

def check(targetvalue):
    print ("best for",targetvalue,":",bestcombo(targetvalue))
    
check(3344)
check(1703)
check(8771)
check(5490)
check(1230)
check(713)
check(564)
