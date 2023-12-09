def get_adj_list(n, edge_list):
    adj_list = [[] for i in range(0,n)] 
    for edge in edge_list:
        adj_list[edge[0]].append(edge[1])
    return adj_list

def distant_descendants(adj, k):
    n = len(adj)
    s = [0] * n
    visited = [False] * n
    prev_ancestors = []
    
    def dfs(u):
        visited[u] = True
        prev_ancestors.append(u)
        for v in adj[u]:
            if not visited[v]:
                dfs(v)
                if len(prev_ancestors) > k:
                    s[prev_ancestors[-k-1]] += 1
                s[u] += s[v]
                prev_ancestors.pop()
    
    for u in range(n):
        if not visited[u]:
            dfs(u)
    return s

if __name__ == "__main__":
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (3, 6), (4, 7), (2, 5), (5, 8), (5, 9), (5, 10)]
    adj = get_adj_list(11, edges)
    print(distant_descendants(adj, 2))