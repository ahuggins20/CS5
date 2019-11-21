import itertools
def evenList(my_list):
    return [my_list[i] for i in range(0, len(my_list),2) if my_list[i]%2==0]
#print(evenList([1,3,5,8,10,13,18,36,78]))

def leastNonRepresentableInt(my_list):
    out=[]
    for i in range(1, len(my_list)):
        temp=(list(itertools.combinations(my_list,i)))
        for comb in temp:
            out.append(sum(comb))
    out.append(sum(my_list))
    for i in range(1,max(out)+2):
        if i not in out:
            return i
print(leastNonRepresentableInt([1,2,2,5,7]))