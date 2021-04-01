class DFS():
    
    def __init__(self, graph):
        self.visited = []
        self.graph = graph
        self.used = dict.fromkeys(set(graph), False)
    
    def traverse(self, s):
    
        if self.used[s] == False:
            self.visited.append(s)
            self.used[s] = True

        for n in self.graph[s]:
            self.traverse(n) 
        
        return self.visited

dfs = DFS(graph)
visited = dfs.traverse('A')
print([i for i in visited])        # A -> B -> D -> E -> F -> C