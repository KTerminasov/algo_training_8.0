def main():
    n, sec = map(int, input().split())

    mod = n % 10

    if sec == 0 or mod == 0:
        # print(n)
        return n
    elif mod == 5:
        # print(n+5)
        return n+5
    elif mod % 2 == 1:
        n += mod
        sec -= 1
        mod = n % 10
    
    # У нас получается цикл остатков {2, 4, 8, 6} длины 4 и суммой 20
    n += 20 * (sec // 4)  # Добавляем полные вхождения цикла

    for _ in range(sec % 4):
        n += n % 10  # Добавляем оставшиеся остатки из неполного цикла

    #print(n)
    return n   


if __name__ == '__main__':
    print(main())
