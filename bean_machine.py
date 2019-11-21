import random
import numpy as np
def bean_machine(balls, slots_num):
    slots=[0]*slots_num
    start=((1+slots_num)/2)-1
    for i in range(balls):
        string=''
        index=start
        for j in range(slots_num-1):
            if random.random()>0.5:
                string+="L"
                index-=0.5
            else:
                string+="R"
                index+=0.5
        slots[int(index)]+=1
        print(string)
    for balls in slots:
        for i in range(balls):
            print('0', sep='', end='')
        print()
    print(slots)
bean_machine(5,5)