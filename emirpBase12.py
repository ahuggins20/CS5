import math
def main(num):
    arr=[]
    i=10
    while len(arr)<10:
        if isPrime(i) and isPrime(reverse(i)) and i!=reverse(i):
            arr.append(i)
        i+=1
    return arr
def isPrime(num):
    for i in range(2,(num//2)):
        if num%i==0:
            return False
    return True

def reverse_b12(x):
    b12_x=''
    while x>0:
        end=x%12
        if end>=10:
            if end==10:
                b12_x+="A"
            if end==11:
                b12_x+="B"
        else:
            b12_x+=str(x%12)
        x=x//12
    return b12_x
print(reverse_b12(71))