def main():
    n = int(input())

    is_simple = [True] * (n + 1)
    is_simple[0] = False
    is_simple[1] = False

    i = 2
    while i <= n ** 0.5:
        if is_simple[i] is True:
            j = i ** 2
            while j <= n:
                is_simple[j] = False
                j += i
        i += 1

    dp = [0] * (n + 1)
    dp[0] = 2

    for i in range(1, n + 1):
        dp[i] = 2
        for j in (1, 2, 3):
            if i - j >= 0:
                k = i - j
                if not is_simple[k] and dp[k] == 2:
                    dp[i] = 1
                    break

    print(dp[n])
    return str(dp[n])    


if __name__ == '__main__':
    main()
