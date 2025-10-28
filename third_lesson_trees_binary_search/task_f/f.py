import sys


def main():
    
    n = int(input())
    
    tree = [None] + [[] for _ in range(n)]    
    parents = [None] + list(map(int, input().split()))
    root = None
    
    for i in range(1, n + 1):
        if parents[i] == 0:
            root = i
        else:
            tree[parents[i]].append(i)
    
    in_time = [0] * (n + 1)
    out_time = [0] * (n + 1)

    stack = [(root, True)]
    time_count = 0

    while stack:
        ancestor, is_in = stack.pop()

        if is_in:
            time_count += 1
            in_time[ancestor] = time_count
            stack.append((ancestor, False))

            for descendant in reversed(tree[ancestor]):
                stack.append((descendant, True))
            
        else:
            time_count += 1
            out_time[ancestor] = time_count

    m = int(input())
    res = ''
    for i in range(m):
        ancestor, descendant = map(int, input().split())
        
        if in_time[ancestor] <= in_time[descendant] and \
                out_time[ancestor] >= out_time[descendant] and \
                ancestor != descendant:
            res += '1\n'
        else:
            res += '0\n'
    
    result = res.rstrip()
    print(result)
    return result


if __name__ == '__main__':
    main()