def main():
    n, m = map(int, input().split())
    table = [list(map(int, input().split())) for i in range(n)]

    ord_a = []
    for i in range(n):
        for j in range(m):
            ord_a.append((table[i][j], i, j))    
    ord_a = sorted(ord_a, key=lambda x: x[0])

    dp = [[1] * m for i in range(n)]
    directions = [(0, -1), (-1, 0), (1, 0), (0, 1)]

    for a, i, j in ord_a:
        for di, dj in directions:
            curr_i, curr_j = i + di, j + dj
            if 0 <= curr_i < n and 0 <= curr_j < m and \
                    table[curr_i][curr_j] == a - 1:
                dp[i][j] = max(dp[i][j], 1 + dp[curr_i][curr_j])

    res = max(max(j) for j in dp)
    print(res)
    return res


if __name__ == '__main__':
    main()