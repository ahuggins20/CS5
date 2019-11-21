import string
def read(note):
    startSpot=note[0]
    endSpot=note[4]
    spotCreated=(note[2])
    spotsInRegion=[]
    if '[' in note:
        startIndex=note.find('[')
        endIndex=note.find(']')
        for i in range(startIndex+1, endIndex):
            if note[i]!=',':
                spotsInRegion.append(note[i])
    return(startSpot,endSpot,spotCreated,spotsInRegion)
print(read('1(3)1[2]'))