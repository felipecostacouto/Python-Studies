def quicksort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quicksort(arr,left, pivot -1)
        quicksort(arr, pivot + 1, right)


def partition(arr, left, right):
    pivot = arr[right]
    i = left -1 

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] == arr[j], arr[i]
    
    arr[i + 1], arr[right] == arr[right], arr[i + 1]
    return i + 1




def main():
    return 0

if __name__ == "__main__":
    main()