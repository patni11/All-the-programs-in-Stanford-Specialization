#Inversion for small array size
arr = [4,6,7,9,1,2,5,3,8]
inversions = 0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] > arr[j]:
            inversions += 1

print(inversions)