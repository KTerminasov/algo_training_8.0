from bisect import bisect


def main():
    n = int(input())

    segments = [list(map(float, input().split())) for i in range(n)]
    segments = sorted(segments, key=lambda x: x[1])
    ends = [i[1] for i in segments]

    dp = [0] * (n + 1)

    for i in range(1, n+1):
        j = bisect(ends, segments[i-1][0], 0, i)
        dp[i] = max(dp[i-1], segments[i-1][2] + dp[j])

    print(dp[n])
    return dp[n]


if __name__ == '__main__':
    main()