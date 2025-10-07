def main():
    n = int(input())

    dp = [0] * (n + 1)
    dp[0] = 0
    if n == 1:
        print(1)
        return 1
    dp[1] = 1
    if n == 2:
        print(2)
        return 2
    dp[2] = 2
    if n == 3:
        print(4)
        return 4
    dp[3] = 4

    for i in range(4, n + 1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[n])
    return dp[n]


if __name__ == '__main__':
    main()