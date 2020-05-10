
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            arr[k] = right[j]
            k += 1
            j += 1   

    else:
        return        
        
if __name__ == "__main__":
    print("Welcome to Merge Sort, Please enter the array you want to sort seperated by comma")
    arr = list(map(int, input().split(',')))
    merge_sort(arr)
    print("Sorted array is : ") 
    print(arr) 
