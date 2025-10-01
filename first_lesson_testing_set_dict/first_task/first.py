def main():
    n = int(input())

    sum_vas = 0
    min_vas = 1000

    sum_mash = 0
    max_mash = 0

    a = [int(i) for i in input().split()]
    for i in range(n):
        if i % 2 == 0:
            sum_vas += a[i]
            if a[i] < min_vas:
                min_vas = a[i]
        else:
            sum_mash += a[i]
            if a[i] > max_mash:
                max_mash = a[i]

    res = sum_vas - sum_mash
    if min_vas < max_mash:
        res = res - 2*min_vas + 2*max_mash

    return res


if __name__ == '__main__':
    print(main())
