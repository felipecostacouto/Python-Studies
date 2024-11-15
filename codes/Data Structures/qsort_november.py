class Qsort:
    def quick_sort(self, arr, left, right):
        if left < right:
            index = Qsort.pivot(arr, left, right)
            Qsort.quick_sort(arr, left, index -1)
            Qsort.quick_sort(arr, index + 1, right)

    @staticmethod
    def pivot(arr, left, right):
        piv = arr[right]
        i = left - 1

        for j in range(left, right):
            if arr[j] <= piv:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[right] = arr[right], arr[i + 1]
        return i + 1

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
Qsort.quick_sort(arr, 0, len(arr) - 1)
print(arr)