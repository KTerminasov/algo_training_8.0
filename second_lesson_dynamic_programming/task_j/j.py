def main():
    n, l = map(int, input().split())

    # Pi Ri Qi Fi
    stores = [[j for j in map(int, input().split())] for i in range(n)]
    max_opt = sum(s[3] for s in stores) + 1
    dp = [[10**9] * max_opt for i in range(n + 1)]
    dp[0][0] = 0

    from collections import deque

    inf = 10**9
    big = 10**18

    def cost(i, j):
        if j == 0:
            return 0

        if j <= stores[i][3]:
            if j < stores[i][1]:
                return j * stores[i][0]
            else:
                return j * stores[i][2]
        else:
            return inf

    for i in range(1, n + 1):
        P, R, Q, F = stores[i-1]
        # copy no buy
        for jj in range(max_opt):
            dp[i][jj] = dp[i-1][jj]

        def f(mm, CC):
            if dp[i-1][mm] >= inf:
                return big
            else:
                return dp[i-1][mm] - mm * CC

        def update_range(low, high, C):
            if low > high:
                return
            dq = deque()
            for j in range(low, max_opt):
                m_new = j - low
                if m_new < 0:
                    continue
                if dp[i-1][m_new] < inf:
                    while dq and f(dq[-1], C) >= f(m_new, C):
                        dq.pop()
                    dq.append(m_new)
                while dq and dq[0] < max(0, j - high):
                    dq.popleft()
                if dq:
                    min_f = f(dq[0], C)
                    new_val = min_f + j * C
                    dp[i][j] = min(dp[i][j], new_val)

        low = 1
        high = min(R - 1, F)
        if low <= high:
            update_range(low, high, P)

        low = R
        high = F
        if low <= high:
            update_range(low, high, Q)

    min_cost = 10**9
    best_total = -1
    for j in range(l, max_opt):
        if dp[n][j] < min_cost:
            min_cost = dp[n][j]
            best_total = j

    if min_cost >= 10**9:
        print(-1)
        return '-1'
    else:
        res = f'{min_cost}\n'
        amounts = []
        j = best_total
        for i in range(n, 0, -1):            
            for a in range(stores[i-1][3] + 1):
                prev_j = j - a
                if prev_j < 0:
                    continue
                c = cost(i-1, a)
                if dp[i-1][prev_j] + c == dp[i][j]:
                    amounts.append(a)
                    j = prev_j
                    break

        amounts.reverse()
        res += ' '.join(map(str, amounts))
        print(res)
        return res


if __name__ == '__main__':
    main()