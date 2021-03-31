# even: increasing, odd: decreasing 

class Sort:
    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2 
        left = self.mergeSort(arr[:mid])      # recursive (10, 9, 2, 7, 5)
        right = self.mergeSort(arr[mid:])     # recursive (4, 6, 3, 8, 1)
        return self.merge(left, right)        # the last one 
    
    def merge(self, A, B):
        
        sorted_arr = []
        i, j = 0, 0
        
        while i < len(A) and j < len(B):
            if A[i] % 2 == 0 and B[j] % 2 == 0:
                if A[i] < B[j]:
                    sorted_arr.append(A[i])
                    i += 1
                else:
                    sorted_arr.append(B[j])
                    j += 1
            elif A[i] % 2 != 0 and B[j] % 2 != 0:
                if A[i] > B[j]:
                    sorted_arr.append(A[i])
                    i += 1
                else:
                    sorted_arr.append(B[j])     
                    j += 1
            elif A[i] % 2 == 0:
                sorted_arr.append(A[i])
                i += 1
            else:
                sorted_arr.append(B[j])
                j += 1

        sorted_arr += A[i:]
        sorted_arr += B[j:]
        print('sorted_arr =', sorted_arr)
        
        return sorted_arr

arr = [10, 9, 2, 7, 5, 4, 6, 3, 8, 1]
sort = Sort()
sorted_arr = sort.mergeSort(arr)    # sorted_arr = [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]
print(sorted_arr)