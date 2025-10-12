def main():
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]

    dp = [0] * (n + 1)
    
    for i in range(k, n + 1):   
        strength = sum(a[i-k:i]) * min(a[i-k:i])
        dp[i] = max(dp[i-1], dp[i - k] + strength)            
    
    starts = []
    i = n
    while i > 0:
        if dp[i] == dp[i - 1]:
            i -= 1
        else:
            start = (i - k) + 1
            starts.append(start)
            i -= k
    
    res = ' '.join(map(str, starts[::-1]))

    print(f'{len(starts)}\n{res}')
    return f'{len(starts)}\n{res}'


if __name__ == '__main__':
    main()
