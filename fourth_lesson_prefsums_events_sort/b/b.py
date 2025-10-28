def main():
    n = int(input())
    
    powers = []
    taxes = []
    for _ in range(n):
        power, tax = map(int, input().split())
        powers.append(power)
        taxes.append(tax)
    
    m = int(input())
    cars_powers = []
    for _ in range(m):
        cars_powers.append(int(input()))
    
    res = []
    for car_power in cars_powers:
        if car_power <= powers[0]:
            res.append('0')
        else:
            left = 0
            right = len(powers) - 1
            
            while left < right:
                m = (left + right + 1) // 2
                if powers[m] < car_power:
                    left = m
                else:
                    right = m - 1
            res.append(str(car_power * taxes[left]))

    print('\n'.join(res))


if __name__ == '__main__':
    main()