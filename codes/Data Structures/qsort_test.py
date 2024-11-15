def qsort_test(arr, left, right):
    if left < right:
        pi = pivot(arr, left, right)
        qsort_test(arr, left, pi -1)
        qsort_test(arr, pi + 1, right)
    
def pivot(arr, left, right):
    index = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] <= index:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

arr = [3, 6, 8, 10, 1, 2, 1]
qsort_test(arr, 0, len(arr) - 1)
print(arr)