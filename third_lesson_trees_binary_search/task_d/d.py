def main():
    n, p = map(int, input().split())
    c = list(map(int, input().split()))

    ord_c = [(c[ind], ind + 1) for ind in range(n)]
    ord_c.sort()

    min_diff = 10**9
    best_i = best_j = 0

    for j in range(n):
        c_j = ord_c[j][0]
        target = p * c_j

        left, right = 0, n - 1
        nearest_pos = 0
        while left < right:
            m = (left + right) // 2
            
            if ord_c[m][0] <= target:
                left = m + 1
                nearest_pos = m
            else:
                right = m
                
        for pos in (nearest_pos - 1, nearest_pos, nearest_pos + 1):
            if 0 <= pos < n and pos != j:
                c_i = ord_c[pos][0]

                diff = abs(c_i / c_j - p)
                if diff < min_diff:
                    min_diff = diff
                    best_i = ord_c[pos][1]
                    best_j = ord_c[j][1]

    print(best_i, best_j)       


if __name__ == '__main__':
    main()