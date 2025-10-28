def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())

    prefs = [0] * (n + m + 1)
    # Расчет префиксных сумм
    for i in range(1, n + 1):
        prefs[i] = prefs[i-1] + (1 if a[i-1] >= x else 0)

    start = 1
    end = n
    res = []

    for _ in range(m):
        data = input().split()
        event = data[0]

        if event == '1':
            val = int(data[1])
            end += 1
            prefs[end] = prefs[end-1] + (1 if val >= x else 0)
        elif event == '2':
            start += 1
        else:
            k = int(data[1])
            res.append(str(prefs[start + k - 1] - prefs[start - 1]))
    
    print('\n'.join(res))


if __name__ == '__main__':
    main()