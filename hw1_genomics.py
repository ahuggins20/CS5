import numpy as np
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

def hidden_message(text, pattern):
    count=0
    for i in range(len(text)-len(pattern)):
        if text[i:i+len(pattern)]==pattern:
            count+=1
    return count

def reverseCompliment(text):
    compliment=''
    text=text.lower()
    base_dict={'a':'t','t':'a','c':'g','g':'c'}
    for ch in text:
        compliment+=base_dict[ch]
    temp=compliment[::-1]
    temp=temp.upper()
    return temp
with open('Cholera/cholera.txt') as f:
    cholera=f.read()
with open('Cholera/choleraOri.txt') as f:
    ori=f.read()
with open("Cholera/frequentWordsTest.txt") as f:
    frequent_words_test=f.read()
#print(frequent_words(ori,9))
#print(hidden_message(frequent_words_test,'CGTGGCGTG'))

def ifReverseCompliment(ori, text):
    for i in range(len(ori)-len(text)):
        if ori[i:i+len(text)]==reverseCompliment(text):
            return True
    return False

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
print(LTClump(frequent_words_test, 9, 200, 5))