def cubeThing(sideLength):
    intSquareLength=sideLength*5**(1/2)/2
    intSquareArea=intSquareLength**2
    return((intSquareArea/sideLength**2)**2)
print(cubeThing(1))