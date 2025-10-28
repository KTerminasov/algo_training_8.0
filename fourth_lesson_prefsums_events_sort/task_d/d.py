def main():
    n = int(input())
    a = list(map(int, input().split()))

    pref = [0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + a[i - 1]

    suf = [0] * (n + 2)
    for i in range(n, 0, -1):
        suf[i] = a[i - 1] + suf[i + 1]

    best_diff = float('inf')
    best_l = 0
    best_r = 0

    for l in range(1, n):
        low = l + 1
        high = n
        while low <= high:
            mid = (low + high) // 2
            if suf[mid] > pref[l]:
                low = mid + 1
            else:
                high = mid - 1
                
        candidates = []
        if l + 1 <= high <= n:
            candidates.append(high)
        if l + 1 <= low <= n:
            candidates.append(low)
            
        for r in candidates:
            diff = abs(pref[l] - suf[r])
            if diff < best_diff:
                best_diff = diff
                best_l = l
                best_r = r

    print(f"{best_diff} {best_l} {best_r}")
    return f"{best_diff} {best_l} {best_r}"


if __name__ == '__main__':
    main()