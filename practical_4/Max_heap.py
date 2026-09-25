def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    print("Max Heap:", arr)

    # Heap Sort
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


# array 1
arr1 = [25, 15, 30, 10, 20]
print("Original:", arr1)
print("Sorted :", heap_sort(arr1.copy()))

# array 2
arr2 = [25, 5, 18, 7, 3]
print("\nOriginal:", arr2)
print("Sorted :", heap_sort(arr2.copy()))
