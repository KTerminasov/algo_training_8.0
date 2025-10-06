def main():
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    found = False
    
    for r in range(n):
        for c in range(m):
            if grid[r][c] == '.':
                continue
            sym = grid[r][c]
            for dr, dc in directions:
                count = 1
                for step in range(1, 5):
                    nr = r + step * dr
                    nc = c + step * dc
                    if not (0 <= nr < n and 0 <= nc < m) or grid[nr][nc] != sym:
                        break
                    count += 1
                if count == 5:
                    found = True
                    break
            if found:
                break
        if found:
            break
    
    print("Yes" if found else "No")


if __name__ == '__main__':
    main()