def main():
    n, m, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    
    diff = [0] * (n + 2)
    routes = []
    for _ in range(m):
        l, r = map(int, input().split())
        routes.append((l, r))
        diff[l] += 1
        if r + 1 <= n:
            diff[r + 1] -= 1
            
    w = [0] * n
    current = 0
    for i in range(1, n + 1):
        current += diff[i]
        w[i - 1] = current
        
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + a_list[i - 1]
        
    total_discomfort = 0
    for l, r in routes:
        total_discomfort += prefix[r] - prefix[l - 1]
        
    segments = []
    for i in range(n):
        segments.append((w[i], a_list[i]))
        
    segments.sort(reverse=True)
    
    total_gain = 0
    remaining = k
    for weight, a_val in segments:
        if remaining <= 0:
            break
        take = min(remaining, a_val)
        total_gain += take * weight
        remaining -= take
        
    result = total_discomfort - total_gain
    print(result)


if __name__ == "__main__":
    main()