def main():
    import heapq

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if sum(a) > sum(b):
        res = -1
        print(res)
        return str(res)
    
    def can_distribute(k):
        heap = []
        j = 0

        for i in range(n):
            while j < n and j - k <= i:
                if a[j] > 0:
                    heapq.heappush(heap, (j + k, a[j], j))
                j += 1
            
            canditates = b[i]

            while canditates > 0 and heap:
                right, count, original = heap[0]

                if right < i:
                    return False
                
                take_cand = min(canditates, count)
                canditates -= take_cand

                if count == take_cand:
                    heapq.heappop(heap)
                else:
                    heap[0] = (right, count - take_cand, original)
                    heapq.heapify(heap)

        return len(heap) == 0

    left, right = 0, n + 1

    while left < right:
        m = (left + right) // 2

        if can_distribute(m):
            right = m
        else:
            left += 1

    res = right if right != n + 1 else -1
    print(res)
    return str(res)
         

if __name__ == '__main__':
    main()
