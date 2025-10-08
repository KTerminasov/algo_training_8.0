def main():
    s = input()
    
    words = set()
    for i in range(int(input())):
        words.add(input())

    dp = [None] * (len(s) + 1)
    dp[0] = ''
    for i in range(1, len(s) + 1):
        for j in range(max(0, i-20), i):
            if dp[j] is not None and s[j:i] in words:
                dp[i] = dp[j] + f'{s[j:i]} '

    print(dp[-1])
    return dp[-1]


if __name__ == '__main__':
    main()
