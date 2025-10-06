def main():
    x, y = map(int, input().split())
    f, g = map(int, input().split())
    a = abs(x - f)
    b = abs(y - g)
    if a == 0 and b == 0:
        print(0)
    elif a == 0:
        print(3 * (b - 1))
    elif b == 0:
        print(3 * (a - 1))
    else:
        print(3 * (a + b) - 5)

if __name__ == '__main__':
    main()