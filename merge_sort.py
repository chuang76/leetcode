# in-place 

class Sort:
    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2 
        left = self.mergeSort(arr[:mid])      # recursive
        right = self.mergeSort(arr[mid:])     # recursive
        return self.merge(left, right)        # the last one 
    
    def merge(self, left, right):
        sorted_arr = []
        i, j = 0, 0 
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1

        sorted_arr += left[i:]
        sorted_arr += right[j:]
        return sorted_arr

import random
arr = []
for i in range(10):
    arr.append(random.randint(0, 100))
print(arr)

sort = Sort()
sorted_arr = sort.mergeSort(arr)
print(sorted_arr)


# merge sort: split into even and odd 
class Sort:
    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr
        
        even = self.mergeSort([arr[i] for i in range(len(arr)) if i % 2 == 0])
        odd = self.mergeSort([arr[i] for i in range(len(arr)) if i % 2 != 0])
                
        return self.merge(even, odd)
    
    def merge(self, A, B):
        sorted_arr = []
        i, j = 0, 0 
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                sorted_arr.append(A[i])
                i += 1
            else:
                sorted_arr.append(B[j])
                j += 1

        sorted_arr += A[i:]
        sorted_arr += B[j:]
        
        return sorted_arr