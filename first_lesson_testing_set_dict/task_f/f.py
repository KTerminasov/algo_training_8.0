import sys

def main():
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    
    base_row = [0] * n
    num_q_row = [0] * n
    base_col = [0] * m
    num_q_col = [0] * m
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '+':
                base_row[i] += 1
                base_col[j] += 1
            elif grid[i][j] == '-':
                base_row[i] -= 1
                base_col[j] -= 1
            else:
                num_q_row[i] += 1
                num_q_col[j] += 1
    
    max_diff = -sys.maxsize - 1
    
    for c in range(m):
        min_sum_c = base_col[c] - num_q_col[c]
        max_r = -sys.maxsize - 1
        for r in range(n):
            adjust = 2 if grid[r][c] == '?' else 0
            this_row_max = base_row[r] + num_q_row[r] - adjust
            if this_row_max > max_r:
                max_r = this_row_max
        
        other_max = sys.maxsize
        has_other = False
        for jj in range(m):
            if jj == c:
                continue
            has_other = True
            this_max = base_col[jj] + num_q_col[jj]
            if this_max < other_max:
                other_max = this_max
        if not has_other:
            other_max = sys.maxsize
        
        actual_min = min(min_sum_c, other_max)
        diff = max_r - actual_min
        if diff > max_diff:
            max_diff = diff
    
    print(max_diff)
    return str(max_diff)


if __name__ == '__main__':
    main()