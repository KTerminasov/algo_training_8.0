def main():
    n = int(input())
    field = ['   ']
    field += [input() for i in range(n)]

    dp = [3 * [0] for i in range(n + 1)]
    res = 0
    no_way = [False, False, False]

    for i in range(1, n + 1):

        no_way[1] = True

        if field[i-1][1] != 'W':
            no_way[0] = False
            no_way[2] = False

        if field[i] == 'WWW':
            no_way = [True, True, True]

        # Для средних клеток
        if field[i][1] != 'W':
            dp[i][1] = max(dp[i-1])

            if field[i][1] == 'C':
                dp[i][1] += 1

            no_way[1] = False

        for j in (0, 2):  # Для крайних клеток
            if field[i][j] == field[i-1][1] == field[i][1] == 'W' or \
                field[i-1][j] == field[i-1][1] == 'W':
                no_way[j] = True
            elif field[i][j] != 'W' and no_way[j] is False:
                dp[i][j] = max(dp[i-1][j], dp[i-1][1])

                if field[i][j] == 'C':
                    dp[i][j] += 1
    
                # no_way = False        

        if False not in no_way:
            res = max(dp[i-1])
            break

    res = max(res, max(dp[n]))
    print(res)
    return res


if __name__ == '__main__':
    main()
