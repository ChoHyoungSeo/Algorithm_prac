# bubble sort, O(N^2)
# compare two adjacent numbers
def bubbleSort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

# improved bubble sort, O(N) in bestcase
def modified_bubbleSort(array):
    length = len(array) - 1
    
    for i in range(length):
        isSort = False
        for j in range(length-i):
            if(array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
                isSort = True

        if isSort == False:
            break
                
    return array

# insertionSort bestcase O(N), worstcase O(N^2)
# increase sorted group
# std num, compare with left numbers, insert
def insertionSort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i - 1
        
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
            
        array[j+1] = key
    return array
    
def insertionSort02(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i, 0, - 1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
    return array

# O(N), O(N^2)
# find smallest number, switch location
def selectionSort(array):
    for i in range(len(array)-1):
        min_index = i
        
        for j in range(i+1,len(array)):
            if array[min_index] > array[j]:
                min_index = j
        
        array[i],array[min_index] = array[min_index],array[i]
        
    return array

# height logN * compare operation N => O(nlogn)
# divide and merge
def mergeSort(array):
    if len(array) < 2:
        return array
    mid = len(array) // 2
    low_arr = mergeSort(array[:mid])
    high_arr = mergeSort(array[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    print("temp:", merged_arr)
    return merged_arr

# divide & conquer like mergesort
# doesn't need additional memory
# using pivot
# usually in built-in functions
def quickSort(array):
    if len(array) <= 1:
        return array
    pivot = len(array) // 2
    front_arr, pivot_arr, back_arr = [], [], []
    for value in array:
        if value < array[pivot]:
            front_arr.append(value)
        elif value > array[pivot]:
            back_arr.append(value)
        else:
            pivot_arr.append(value)
    print("temp:",front_arr, pivot_arr, back_arr)
    return quickSort(front_arr) + quickSort(pivot_arr) + quickSort(back_arr)
    
if __name__ == '__main__':
    array = [9,8,7,6,5,4,3,2,1]
    print("bubble sort:", bubbleSort(array))
    print("modified_bubbleSort:", modified_bubbleSort(array))
    print("insertionSort:", insertionSort(array))
    print("insertionSort:", insertionSort02(array))
    print("selectionSort:", selectionSort(array))
    print("mergeSort:", mergeSort(array))
    print("quickSort:", quickSort(array))