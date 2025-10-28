def main():    
    n = int(input())
    a = [0] + list(map(int, input().split()))
    tree = [[] for _ in range(n+1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())        
        tree[u].append(v)
        tree[v].append(u)

    total_capacity = sum(a)
    parents = [0] * (n + 1)
    subtrees_capacities = [0] * (n + 1)
    for i in range(1, n + 1):
        subtrees_capacities[i] = a[i]
    
    stack = [1]
    order = []
    visited = [False] * (n + 1)
    visited[1] = True
    
    while stack:
        v = stack.pop()
        order.append(v)

        for u in tree[v]:
            if u == parents[v]:
                continue
            
            parents[u] = v
            visited[u] = True
            stack.append(u)
    
    for i in range(len(order)-1, -1, -1):
        v = order[i]
        for u in tree[v]:
            if u == parents[v]:
                continue
            subtrees_capacities[v] += subtrees_capacities[u]
    
    best_node = 1
    best_value = float('inf')
    for v in range(1, n+1):
        max_capacity = 0
        
        for u in tree[v]:
            if u == parents[v]:
                capacity = total_capacity - subtrees_capacities[v]
            else:
                capacity = subtrees_capacities[u]
            
            max_capacity = max(capacity, max_capacity)
        
        queue_size = max(a[v], max_capacity)
        if queue_size < best_value:
            best_value = queue_size
            best_node = v
    
    print(best_node)
    return best_node


if __name__ == '__main__':
    main()