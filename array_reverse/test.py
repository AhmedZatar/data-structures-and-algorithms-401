arr=[1,2,3,4]

def reverseArray(arr):
    newArr=[]
    t=len(arr)
    while t!=0:
        newArr.append(arr[t-1])
        t=t-1
    return newArr

print(reverseArray(arr))