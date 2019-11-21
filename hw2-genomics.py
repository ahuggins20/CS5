import numpy as np
import pprint
def patternFinder(pattern, genome):
    for i in range(0,len(genome)-len(pattern)):
        if genome[i:i+len(pattern)]==pattern:
            print(i,end=' ')
    print('')
with open('Cholera/cholera.txt') as f:
    cholera=f.read()
with open('Cholera/choleraOri.txt') as f:
    ori=f.read()
ori=ori.upper()
patternFinder('ATGATCAAG',cholera)
patternFinder(ori, cholera)
def LTClump(text, k, l, t):
    out=[]
    for i in range(len(text)-l):
        temp=frequent_words(text[i:i+l],k)
        if temp[1]>=t:
            for kmer in temp[0]:
                out.append(kmer)
    out=np.array(out)
    out=np.unique(out)
    return out 

def frequent_words(text, k):
    k_mer_dict={}
    for i in range(len(text)-k+1):
        try:
            k_mer_dict[text[i:i+k]]+=1
        except:
            k_mer_dict[text[i:i+k]]=1
    max_iters=max(k_mer_dict.values())
    keys=[]
    possible_messages=[]
    for key in k_mer_dict.keys():
        if k_mer_dict[key]==max_iters:
            keys.append(key)
    temp_keys=keys.copy()
    if len(temp_keys)>1:
        for key in temp_keys:
            temp=reverseCompliment(key)
            if temp in keys:
                possible_messages.append((key,temp))
                temp_keys.remove(temp)
    return (keys,max_iters,possible_messages)

def reverseCompliment(text):
    compliment=''
    text=text.lower()
    base_dict={'a':'t','t':'a','c':'g','g':'c'}
    for ch in text:
        compliment+=base_dict[ch]
    temp=compliment[::-1]
    temp=temp.upper()
    return temp
#print(LTClump('CGGACTCGACAGATGTGAAGAAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA',5,50,4))
def FreqKmer(ori,minK,maxK):
    kmer_dict={}
    pp = pprint.PrettyPrinter(indent=4)
    for i in range(minK,maxK+1):
        temp=frequent_words(ori,i)
        kmer_dict[i]=(temp[1], temp[0])
    pp.pprint(kmer_dict)
FreqKmer(ori, 3, 9)