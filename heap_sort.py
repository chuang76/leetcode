class minHeap():
    def __init__(self):
        self.heap = []
        self.size = 0       
    
    def insert(self, value):
        self.heap.append(value)
        self.size += 1
        self.swim(self.size-1)    
    
    def swim(self, i):
        while i > 0:
            target = (i - 1) // 2
            if self.heap[i] < self.heap[target]:
                self.heap[i], self.heap[target] = self.heap[target], self.heap[i]
            i = target
    
    def remove(self):
        root = self.heap[0]              
        self.heap[0] = self.heap[-1]      
        self.heap = self.heap[:-1]        
        self.size -= 1                    
        self.sink(0)                     
        return root 
    
    def sink(self, i):
        while (i * 2 + 1) < self.size:        
            target = self.minChild(i)
            if self.heap[i] > self.heap[target]:
                self.heap[i], self.heap[target] = self.heap[target], self.heap[i]
            i = target
    
    def minChild(self, i):
        if (i * 2 + 2) == self.size:
            return i * 2 + 1  
        if self.heap[i*2+1] < self.heap[i*2+2]:
            return i * 2 + 1
        return i * 2 + 2

arr = []
for i in range(10):
    arr.append(random.randint(0, 100))

# arr = [10, 9, 2, 7, 5, 4, 6, 3, 8, 1]
heap = minHeap()
for i in arr:
    heap.insert(i)

while heap.size > 0:
    print(heap.remove(), end=' ')
print()