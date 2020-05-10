#counting inversions using merge sort
#IntegerArray.txt
f = open("input_beaunus_48_8192.txt",'r')
arr = []
for line in f:
    a = line
    arr.append(a)
print(len(arr))    

def merge_sort(arr,inversion):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        inv_count_L = merge_sort(L,inversion)
        inv_count_R = merge_sort(R,inversion)

        i = j = k = 0
        inversion = 0 + inv_count_R + inv_count_L

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
                inversion += len(L)-i + 1
            k += 1        
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            inversion += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1        
            inversion += 1
    return inversion

print(merge_sort(arr,0))
