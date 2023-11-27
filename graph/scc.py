def get_adj_list(n, edge_list):
    adj_list = [[] for i in range(0,n)] 
    for edge in edge_list:
        adj_list[edge[0]].append(edge[1])
    return adj_list

def reverse_graph(adj_list):
    n = len(adj_list)
    adj_reverse = [[] for i in range(n)]
    for u in range(n):
        for v in adj_list[u]:
            adj_reverse[v].append(u)
    return adj_reverse

def kosaraju(adj_list):
    n = len(adj_list)
    post_order = [0] * n
    visited = set()
    clock = 1
    
    def post_visit(node):
        nonlocal clock
        post_order[node] = clock
        clock += 1
    
    adj_reverse = reverse_graph(adj_list)
    
    def explore(u):
        visited.add(u)
        for v in adj_reverse[u]:
            if v not in visited:
                explore(v)
        post_visit(u)
        
    for u in range(n):
        if u not in visited:
            explore(u)
    
    post_with_node = []
    for u, post in enumerate(post_order):
        post_with_node.append((post, u))
    
    post_with_node= sorted(post_with_node, reverse=True)
    
    visited = set()
    res = []
    s = set()
    
    def dfs(u):
        s.add(u)
        visited.add(u)
        for v in adj_list[u]:
            if v not in visited:
                dfs(v)
                
    for _, u in post_with_node:
        if u not in visited:
            dfs(u)
        if len(s) != 0:
            res.append(s)
            s = set()

    return res

def tarjan(adj_list):
    n = len(adj_list)
    pre_order = [0] * n
    low_link = [0] * n
    visited = set()
    clock = 0
    
    st = []
    instack = set()
    
    res = []
    
    def pre_visit(node):
        nonlocal clock
        pre_order[node] = clock
        low_link[node] = clock
        clock += 1
        
    def dfs(u):
        visited.add(u)
        st.append(u)
        instack.add(u)
        pre_visit(u)
        for v in adj_list[u]:
            if v not in visited: # tree edge
                dfs(v)
                low_link[u] = min(low_link[u], low_link[v])
            elif v in instack: # back edge
                low_link[u] = min(low_link[u], pre_order[v])
        
        s = set()
        if pre_order[u] == low_link[u]: # root of this scc
            v = st.pop()
            instack.remove(v)
            s.add(v)
            while v != u:
                v = st.pop()
                instack.remove(v)
                s.add(v)
            res.append(s)
    
    for u in range(n):
        if u not in visited:
            dfs(u)
    
    return res
    
if __name__ == "__main__":
    lst1 = [(0, 2), (2, 1), (1, 0), (1, 3), (3, 4), (4, 5), (5, 3), (5, 6)]
    adj1 = get_adj_list(7, lst1)
    print(kosaraju(adj1))
    print(tarjan(adj1))