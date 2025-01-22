def binary_search(arr, x):
    arr.sort()
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r)// 2

        if arr[mid] == x:
            return mid
        
        elif arr[mid] < x:
            l = mid + 1
        
        else:
            r = mid - 1

    return None

arr = [1, 90, 3, 88, 5, 2, 7, 0, 9]
element = int(input("Enter the element to be searched: \n"))
index = binary_search(arr, element)
arr.sort()
print("Sorted Array: " + str(arr))
if index is not None:
    print(f"Element is present at index {index}")
else:
    print("Element is not present in the array")
    print(arr)
