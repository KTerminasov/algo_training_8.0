def main():
    tribs = ' ' + input()
    n = len(tribs) - 1

    if n == 0:
        print(1)
        return 1
    
    INF = float('inf')
    dp = [[INF] * 2 for _ in range(n + 1)]
    dp[0][0] = 0   # Начинаем с левого берега, без переправ
    dp[0][1] = 1  # Начинаем с правого берега с одной переправой

    for i in range(1, n + 1):
        trib = tribs[i]

        for current_trib in range(2):
            cost = 0

            if trib == 'B':
                cost = 1
            elif trib == 'L':
                cost = 1 if current_trib == 0 else 0
            elif trib == 'R':
                cost = 1 if current_trib == 1 else 0
            
            for prev_trib in range(2):
                transfer_cost = 1 if current_trib != prev_trib else 0

                dp[i][current_trib] = min(dp[i][current_trib], dp[i-1][prev_trib] + transfer_cost + cost)
        
    res = min(dp[n][0] + 1, dp[n][1])
    print(res)
    return res


if __name__ == '__main__':
    main()
