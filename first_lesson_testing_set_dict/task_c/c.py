def main():
    s = input()

    freqs = {}
    for char in set(s):
        freqs[char] = s.count(char)

    len_s = len(s)

    all_variants = len_s * (len_s - 1) // 2
    repeated_variants = sum(freq * (freq - 1) // 2 for freq in freqs.values())
    res = 1 + all_variants - repeated_variants

    print(res)
    return str(res)


if __name__ == '__main__':
    main()

