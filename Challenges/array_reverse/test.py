arr=[1,2,3,4]

def reverseArray(arr):
    
    a=0
    b=len(arr)-1
    while a<b:
       arr[a], arr[b] = arr[b], arr[a]
       a += 1
       b -= 1
    return arr

    

print(reverseArray(arr))