class Sort:
    def quickSort(self, arr):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return self.quickSort(less) + [pivot] + self.quickSort(greater)

sort = Sort()
arr = [10, 9, 2, 7, 5, 4, 6, 3, 8, 1]
print(sort.quickSort(arr))

# Solution 2: in-place version 
class Sort:
    def quickSort(self, arr, left, right):
        if left >= right:
            return arr

        pivot = left 
        i, j = left, right 

        while i != j:
            while arr[i] <= arr[pivot] and i < j:
                i += 1
            while arr[j] > arr[pivot] and i < j:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]         # swap 

        if arr[pivot] > arr[i]:
            arr[i], arr[pivot] = arr[pivot], arr[i]

        arr = self.quickSort(arr, left, i-1)
        arr = self.quickSort(arr, i+1, right)

        return arr 

