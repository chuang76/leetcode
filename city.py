def solution(T):
    
    if len(T) == 0:
        return []
    
    g = collections.defaultdict(list)
    for child, parent in enumerate(T):
        if child != parent:
            g[parent].append(child)
        else:
            capital = child 
    
    print(g)
    
    table = [0] * (len(T) - 1)
    
    def dfs(parent, dist):
        print('parent = %d, dist = %d' %(parent, dist))
        for child in g[parent]:
            print('child =', child)
            table[dist] += 1
            print('table =', table)
            print('=======================================')
            dfs(child, dist + 1)
    
    dfs(capital, 0)

T = [9, 1, 4, 9, 0, 4, 8, 9, 0, 1]
solution(T)