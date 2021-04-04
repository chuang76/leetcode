def reverse(arr):
    for i in range(len(arr) // 2):
        j = len(arr) - 1 - i
        arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [1, 2, 3, 4, 5, 6]
print(reverse(arr))