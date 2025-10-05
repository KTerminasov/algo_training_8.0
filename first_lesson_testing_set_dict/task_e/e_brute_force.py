def main():
    n, sec = map(int, input().split())

    while sec > 0:
        mod = n % 10

        if mod == 0:
            break

        n += mod
        sec -= 1
        print(n)

    print(n)


if __name__ == '__main__':
    main()