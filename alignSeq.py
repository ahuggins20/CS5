import pandas as pd
import numpy as np
def show_Table(h_seq, v_seq, data, hide_zeros=False):
    df=pd.DataFrame(data,columns=list(v_seq),index=list(h_seq))
    if hide_zeros:
        df[df==0]=' '
    print(df)
def main(h_seq, v_seq):
    data=np.zeros((len(h_seq),len(v_seq)))
    show_Table(h_seq, v_seq, data, hide_zeros=False)
    addValues(h_seq,v_seq,data)
    show_Table(h_seq,v_seq,data,hide_zeros=True)
    idDiags(data)
    show_Table(h_seq,v_seq,data,hide_zeros=True)
def addValues(h_seq, v_seq,data):
    for idHch, Hch in enumerate(h_seq):
        for idVch, Vch in enumerate(v_seq):
            if Hch==Vch:
                data[idHch,idVch]+=1
    return data
def idDiags(data):
    for i in range(1,np.shape(data)[0]):
        for j in range(1,np.shape(data)[1]):
            if data[i,j]==0:
                continue
            data[i,j]=data[i-1,j-1]+1
    return data
def idAlignments(data, h_seq, v_seq):
    coords=np.argmax(data)
    longest=np.amax(data)
    totalScore=longest
    coordList=[coords]
    for coord in coordList:
        temp=getDiag(data, coords)
        totalScore+=temp[0]
        i,j=temp[1]
        if i!=0 and j!=0:
            coordList.append((i-1,j))
            coordList.append((i,j-1))
def getDiag(data, coords):
    return (data[coords],(coords[0]-data[coords]+1, coords[1]-data[coords]+1))
main('really','smelly')