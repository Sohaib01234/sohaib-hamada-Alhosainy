def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(arr)


array = [4, 5, 2, 6, 3, 1, 7, 9, 8, 10]

selectionSort(array)
print(array)

#sec (5) صهيب حمادة