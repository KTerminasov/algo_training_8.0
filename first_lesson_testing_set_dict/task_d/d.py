def main():
    n,k = map(int, input().split())

    count_themes = {}
    res = []

    for i in input().split():
        if i in count_themes:
            count_themes[i] += 1
        else:
            count_themes[i] = 1
            res.append(i)
    
    len_res = len(res)

    if len_res > k:
        res = res[:k]
    else:
        for i in count_themes.keys():
            count_themes[i] -= 1  # Так как по одной задаче уже взяли
            if count_themes[i] < k - len_res:
                res += [i] * count_themes[i]
                len_res += count_themes[i]
            else:
                res += [i] * (k - len_res)
                break

    res = ' '.join(map(str, res))
    print(res)
    return res


if __name__ == '__main__':
    main()