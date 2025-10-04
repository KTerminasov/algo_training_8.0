def main():
    n = int(input())
    sec = int(input())

    for _ in range(sec):
        n += n % 10

    print(n)


if __name__ == '__main__':
    main()
