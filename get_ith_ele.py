import random

arr = [5,3,8,9,4,1,2,7,6]

def get_element(arr,s,e,ith):
    
    value = partition(arr,s,e)
    if value == ith:
        return arr[value]
    elif ith > value:
        get_element(arr,value+1,e,ith)
    elif ith < value:
        get_element(arr,s,value-1,ith)        

def partition(arr,s,e):
    val = random.randint(s,e)
    swap(arr,s,val)
    pivot = s
    i = pivot + 1
    j = i
    while j <= e:
        if arr[j] < arr[pivot]:
            swap(arr,i,j)
            i += 1
        j += 1

    swap(arr,i-1,pivot)
    return val        


def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

print(get_element(arr,0,len(arr)-1,5))