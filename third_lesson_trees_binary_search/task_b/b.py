def main():
    n = int(input())    

    tree = {i: [] for i in range(1, n + 1)}    

    for _ in range(n-1):
        parent, child = map(int, input().split())
        if parent not in tree:
            tree[parent] = []
        tree[parent].append(child)
        tree[child].append(parent)
    
    leaves = [situation for situation in tree if len(tree[situation]) == 1]    

    def bfs(start, finish):
        if start == finish:
            return 0
        queue = [(start, 0)]
        visited = {start}

        while queue:
            situation, dist = queue[0]
            queue = queue[1:]

            for next_situation in tree[situation]:
                if next_situation not in visited:
                    if next_situation == finish:
                        return dist + 1
                    visited.add(next_situation)
                    queue.append((next_situation, dist + 1))
        return 10**5

    min_dist = 10**5
    for i in range(len(leaves)):
        for j in range(i + 1, len(leaves)):
            dist = bfs(leaves[i], leaves[j])
            min_dist = min(min_dist, dist)

    print(min_dist)    
    return str(min_dist)


if __name__ == '__main__':
    main()