def binary_search(array, x):
    l = 0
    r = len(array) - 1
    array.sort()
    while l <= r:
        mid = (l + r) // 2
        if array[mid] == x:
            return mid
        if array[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return None


arr = [1, 90, 3, 88, 5, 2, 7, 0, 9]
element = int(input("Enter the element to be searched: \n"))
index = binary_search(arr, element)
if index is not None:
    print(f"Element is present at index {index}")
else:
    print("Element is not present in the array")
    print(arr)
