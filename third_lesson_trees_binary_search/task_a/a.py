def main():
    a, b, s = list(map(int, input().split()))

    def lbinsearch(left, right):
        def check(m):            
            return (m - a) * (m - b) >= s

        while left < right:
            m = (left + right) // 2

            if check(m):
                right = m
            else:
                left = m + 1
        
        return left if (left - a) * (left - b) == s else -1      

    res = lbinsearch(max(a, b)+1, 10**9)
    print(res)
    return res


if __name__ == '__main__':
    main()
