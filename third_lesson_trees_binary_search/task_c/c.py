def main():
    n, w, h = map(int, input().split())

    dims = [tuple(map(int, input().split())) for _ in range(n)]

    def check(k):
        total_height = 0
        i = 0

        while i < n:
            w_i, h_i = dims[i]
            w_cur = k * w_i
            if w_cur > w:
                return False
            
            i += 1
            
            while i < n and dims[i][1] == h_i and w_cur + k * dims[i][0] <= w:
                w_cur += k * dims[i][0]
                i += 1

            total_height += k * h_i

        return total_height <= h

    left, right = 0, min(w, h) + 1
    for _ in range(100):
        k = (left + right) / 2

        if check(k):
            left = k
        else:
            right = k

    res = str(left)

    print(res)
    return res


if __name__ == '__main__':
    main()