def main():
    a, b, c, v0, v1, v2 = map(int, input().split())

    routes = []
    # дом -> супермаркет -> пвз -> дом
    routes.append(a/v0 + c/v1 + b/v2)
    # дом -> супермаркет -> пвз -> супермаркет -> дом
    routes.append(a/v0 + c/v0 + c/v1 + a/v2)
    # дом -> супермаркет -> дом -> пвз -> дом (через пвз сначала аналогично)
    routes.append(a/v0 + a/v1 + b/v0 + b/v1)
    # дом -> супермаркет -> дом -> супермаркет -> пвз -> супермаркет -> дом
    routes.append(a/v0 + a/v1 + a/v0 + c/v0 + c/v1 + a/v1)
    # дом -> пвз -> супермаркет -> дом
    routes.append(b/v0 + c/v1 + a/v2)
    # дом -> пвз -> супермаркет -> пвз -> дом
    routes.append(b/v0 + c/v0 + c/v1 + b/v2)
    # дом -> пвз -> дом -> пвз -> супермаркет -> пвз -> дом
    routes.append(b/v0 + b/v1 + b/v0 + c/v0 + c/v1 + b/v1)

    res = f'{min(routes):.15f}'
    print(res)
    return res


if __name__ == '__main__':
    main()
