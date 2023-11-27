def make_adj_list(n, edge_list):
    adj_list = [[] for i in range(0,n)] 
    for edge in edge_list:
        adj_list[edge[0]].append(edge[1]) # need to include both directions for the edge
        adj_list[edge[1]].append(edge[0])
    return adj_list

def tarjan(adj_list):
    visited = [False] * len(adj_list)
    pre = [0] * len(adj_list)
    lowlink = [0] * len(adj_list)
    parent = [0] * len(adj_list)
    clock = 1
    st = []
    instack = set()
    
    def previsit(u):
        nonlocal clock
        pre[u] = clock
        lowlink[u] = clock
        clock += 1
    
    def explore(u):
        visited[u] = True
        st.append(u)
        instack.add(u)
        previsit(u)
        for v in adj_list[u]:
            if not visited[v]: # tree edge
                parent[v] = u
                explore(v)
                lowlink[u] = min(lowlink[u], lowlink[v])
            elif v in instack and parent[u] != v: # back edge
                lowlink[u] = min(lowlink[u], pre[v])

        if pre[u] == lowlink[u]: # root of this scc
            v = st.pop()
            instack.remove(v)
            while u != v:
                v = st.pop()
                instack.remove(v)
                
    for v in range(len(adj_list)):
        if not visited[v]:
            pre[v] = v
            explore(v)
    return parent, pre, lowlink

def get_critical_vertex(n, parent, pre, lowlink):
    res = []
    for i in range(n):
        if lowlink[i] > pre[parent[i]]:
            res.append(parent[i])
    return res

if __name__ == '__main__':
    lst1 = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (4, 5), (4, 6), (5, 6)]
    adj = make_adj_list(7, lst1)
    print(get_critical_vertex(len(adj), *tarjan(adj)))
    lst2 = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (4, 5), (3, 5)]
    adj = make_adj_list(6, lst2)
    print(get_critical_vertex(len(adj), *tarjan(adj)))
    lst3 = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (4, 5), (4, 6), (5, 6), (6, 7), (7, 8), (7, 9), (8, 9)]
    adj = make_adj_list(10, lst3)
    print(get_critical_vertex(len(adj), *tarjan(adj)))
    lst4 = [[0,1],[1,2],[2,0],[1,3]]
    adj = make_adj_list(4, lst4)
    print(get_critical_vertex(len(adj), *tarjan(adj)))