class BFS():
    
    def __init__(self, graph):
        self.visited = []
        self.queue = []
        self.graph = graph
        self.used = dict.fromkeys(set(graph), False)
    
    def traverse(self, start):
        
        self.visited.append(start)
        self.queue.append(start)
    
        while self.queue:
            s = self.queue.pop(0)

            for n in self.graph[s]:
                if self.used[n] == False:
                    self.visited.append(n)
                    self.used[n] = True
                    self.queue.append(n)
        
        return self.visited

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

bfs = BFS(graph)
visited = bfs.traverse('A')
print([i for i in visited])           # A -> B -> C -> D -> E -> F 
