# This is my implementation of the 2-sat algorithm
# 1 for x_1, -1 for ~x_1
# return -1 if not satisfiable,
# if satisfiable, return a dict with key of literals, value of true or false

def build_graph_by_clauses(n, clauses):
    adj_list = dict([(i, []) for i in range(-n, n+1) if i != 0])
    for a, b in clauses:
        adj_list[-a].append(b)
        adj_list[-b].append(a)
    return adj_list

def tarjan(adj):
    n = len(adj) + 1
    clock = 1
    pre_vals = [0] * n
    lowlink_vals = [0] * n
    visited = [False] * n
    offset = n // 2
    
    st = []
    instack = [False] * n
    
    res = []
    
    def previsit(node):
        nonlocal clock
        pre_vals[node + offset] = clock # number of nodes must be 2 * |V|
        lowlink_vals[node + offset] = clock
        clock += 1
    
    def dfs(u):
        visited[u + offset] = True
        previsit(u)
        st.append(u)
        instack[u + offset] = True
        for v in adj[u]:
            if not visited[v + offset]: # tree edge
                dfs(v)
                lowlink_vals[u + offset] = min(lowlink_vals[u + offset], lowlink_vals[v + offset])
            elif instack[v + offset]: # back edge
                lowlink_vals[u + offset] = min(lowlink_vals[u + offset], pre_vals[v + offset])
                
        s = set()
        if pre_vals[u + offset] == lowlink_vals[u + offset]: # root of this scc
            v = st.pop()
            instack[v + offset] = False
            s.add(v)
            while v != u:
                v = st.pop()
                instack[v + offset] = False
                s.add(v)
            res.append(s)
        
    for u in adj.keys():
        if not visited[u + offset]:
            dfs(u)
    
    return res

def num_of_literals(clauses):
    res = []
    for c in clauses:
        res.extend(c)
    return max(res)

def contains_negation(scc):
    for i in range(len(scc) - 1):
        for j in range(i + 1, len(scc)):
            if scc[i] == -scc[j]:
                return True
    return False

def build_dag(sccs, adj):
    n = len(sccs)
    dag_adj = [[] for _ in range(n)] 
    for i in range(len(sccs)):
        for node in sccs[i]:
            for neighbor in adj[node]:
                if neighbor not in sccs[i]:
                    for j in range(len(sccs)):
                        if neighbor in sccs[j]:
                            if j not in dag_adj[i]:
                                dag_adj[i].append(j)
                            continue     
    return dag_adj

def toposort(dag): # dag is a list of adj list, return a list of nodes in topological order (reversed)
    n = len(dag)
    visited = [False] * n
    res = []
    
    def dfs(u):
        visited[u] = True
        for v in dag[u]:
            if not visited[v]:
                dfs(v)
        res.append(u)
    
    for u in range(n):
        if not visited[u]:
            dfs(u)
    return res

def two_sat(clauses):
    n = num_of_literals(clauses)
    adj_list = build_graph_by_clauses(n, clauses)
    sccs = tarjan(adj_list)
    for scc in sccs:
        if contains_negation(list(scc)):
            return -1 # not satisfiable
    dag_adj = build_dag(sccs, adj_list)
    reversed_topo_order = toposort(dag_adj)
    assign = {}
    assigned = [False] * (n + 1)
    for i in reversed_topo_order:
        if all(assigned):
            break
        for literal in sccs[i]:
            if literal > 0:
                assign[literal] = True
            else:
                assign[-literal] = False
            assigned[abs(literal)] = True
    return assign
    
    
if __name__ == "__main__":
    clauses_1 = [[1, -2], [-1, -3], [1, 2], [-3, 4], [-1, 4]]
    print(two_sat(clauses_1))
    clauses_2 = [[1, 2], [-2, 3], [-1, -2], [3, 4], [-3, 5], [-4, -5], [-3, 4]]
    print(two_sat(clauses_2))
    clauses_3 = [[1, -2], [2, -3], [-1, 3], [-2, -3]]
    print(two_sat(clauses_3))
    clauses_4 = [[1, -2], [2, -3], [3, -1], [-1, -2], [-2, -3], [-3, -1]]
    print(two_sat(clauses_4))
    clauses_5 = [[1, 2], [1, 3], [2, 3], [-1, -2], [-1, -3], [-2, -3]]
    print(two_sat(clauses_5))