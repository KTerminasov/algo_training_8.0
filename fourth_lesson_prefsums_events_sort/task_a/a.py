def main():
    import heapq

    def to_mins(time):
        h, m = map(int, time.split(':'))
        return h * 60 + m
    
    trips = []
    n = int(input())
    for i in range(n):
        dep, arr = input().split('-')
        trips.append((to_mins(dep), to_mins(arr), 'to'))
    m = int(input())
    for i in range(m):
        dep, arr = input().split('-')
        trips.append((to_mins(dep), to_mins(arr), 'back'))      

    trips.sort()
    a_buses = []
    b_buses = []
    min_buses = 0

    for dep, arr, type in trips:
        
        if type == 'to':
            if a_buses and a_buses[0] <= dep:
                heapq.heappop(a_buses)
            else:
                min_buses += 1
            
            heapq.heappush(b_buses, arr)
        else:
            if b_buses and b_buses[0] <= dep:
                heapq.heappop(b_buses)
            else:
                min_buses += 1
            
            heapq.heappush(a_buses, arr)
    
    print(min_buses)
        

if __name__ == '__main__':
    main()