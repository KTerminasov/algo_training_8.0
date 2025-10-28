def main():
    import bisect

    n = int(input())
    a = list(map(int, input().split()))

    m = int(input())
    b = list(map(int, input().split()))

    sorted_b = sorted(b)
    prefix_b = [0] * (m + 1)
    for j in range(m):
        prefix_b[j + 1] = sorted_b[j] + prefix_b[j]
    total_b = prefix_b[m]
    
    s1 = 0
    for i in range(n):
        pos = bisect.bisect_right(sorted_b, a[i])
        left_sum = prefix_b[pos]
        right_sum = total_b - left_sum
        abs_sum = a[i] * pos - left_sum + right_sum - a[i] * (m - pos)
        
        s1 += (i + 1) * abs_sum
    
    sorted_a = sorted(a)
    prefix_a = [0] * (n + 1)
    for i in range(n):
        prefix_a[i + 1] = sorted_a[i] + prefix_a[i]
    total_a = prefix_a[n]

    s2 = 0
    for j in range(m):
        pos = bisect.bisect_right(sorted_a, b[j])
        left_sum = prefix_a[pos]
        right_sum = total_a - left_sum
        abs_sum = b[j] * pos - left_sum + right_sum - b[j] * (n - pos)
        s2 += (j + 1) * abs_sum
    
    res = s1 - s2
    print(res)


if __name__ == '__main__':
    main()
