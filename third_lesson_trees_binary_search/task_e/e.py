def main():
    n = int(input())

    tree = [[] for _ in range(n)]
    parents = [-1] + [int(input()) for _ in range(1, n)]
    weights = list(map(int, input().split()))

    for i in range(1, n):
        tree[parents[i]].append(i)
    
    res = 0
    for parent in range(n):
        children_weight = 0
        for child in tree[parent]:
            children_weight += weights[child]
        
        res += abs(children_weight - weights[parent])

    print(res)
    return res


if __name__ == '__main__':
    main()