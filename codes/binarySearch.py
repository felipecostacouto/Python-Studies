# In Python, the // operator performs integer division, and the result is always an integer,
# avoiding potential issues with overflow. This ensures that the calculation
# remains within the bounds of the data type being used.

def binary_search(array, target):
    array.sort()
    right = len(array) - 1
    left = 0

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # target not found


arr = [3, 1, 4, 5, 9, 2, 6, 5, 3, 5]
print("Unsorted array is:", arr)
arr.sort()
print("Sorted array is:", arr)
print(binary_search(arr, 2))
