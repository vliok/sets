def union(setA, setB):
    diff = [x for x in setB if x not in setA]
    setC = setA + diff
    return setC

#print union([1,2,3], [2,3,4])

def intersect(setA, setB):
    setC = [x for x in setA if x in setB]
    return setC

#print intersect([1,2,3], [2,3,4])

def setDiff(setA, setB):
    setC = [x for x in setA if x not in setB]
    return setC

#print setDiff([1,2,3], [2,3,4])

def symDiff(setA, setB):
    specialA = [x for x in setA if x not in setB]
    specialB = [x for x in setB if x not in setA]
    setC = specialA + specialB
    return setC

#print symDiff([1,2,3], [2,3,4])

def cartProduct(setA, setB):
    setC = [[x,y] for x in setA for y in setB]
    return setC

#print cartProduct([1,2,3], ["red","white"])
