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