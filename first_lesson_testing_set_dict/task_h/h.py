def main():
    n, m = map(int, input().split())
    s = input()

    len_of_part = n // m
    parts = {}
    for i in range(m):
        part = s[i*len_of_part:(i+1)*len_of_part]
        if part not in parts:
            parts[part] = []
        parts[part].append(i + 1)

    curr_pos = 1
    res = [0] * m
    for i in range(m):
        part = input()
        pos = parts[part].pop(0)
        res[pos-1] = curr_pos
        curr_pos += 1

    res = ' '.join(map(str, res))
    print(res)
    return res


if __name__ == '__main__':
    main()
