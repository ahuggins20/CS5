def test(arr):
    num=max(arr)
    while True:
        if num%arr[0]==0 and num%arr[1]==0 and num%arr[2]==0 and num%arr[3]==0:
            return num
        else:
            num+=max(arr)
print(test([3,4,6,16]))