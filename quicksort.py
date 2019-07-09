def partition(arr, low, high):
    i = low -1 # index of smaller element
    pivot = arr[high]  # pivot
    for j in range(low, high):
        # If current element is smaller than or
        # equal to pivot
        # print(arr[j])
        if arr[j] <= pivot:
            # increment index of smaller element
            print(arr[j],"smaller",pivot)
            i = i + 1
            print(i)
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(arr)
    return (i + 1)


def quickSort(arr ,low ,high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr ,low ,high)
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi -1)
        quickSort(arr, pi + 1, high)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)


print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i],end=",")
