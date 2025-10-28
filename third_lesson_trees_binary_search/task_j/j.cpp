#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

std::string main_function() {
    int n;
    std::cin >> n;
    
    std::vector<int> a(n), b(n);
    long long sum_a = 0, sum_b = 0;
    
    // Ввод массива a
    for (int i = 0; i < n; ++i) {
        std::cin >> a[i];
        sum_a += a[i];
    }
    
    // Ввод массива b
    for (int i = 0; i < n; ++i) {
        std::cin >> b[i];
        sum_b += b[i];
    }
    
    // Проверка суммы
    if (sum_a > sum_b) {
        std::cout << -1 << std::endl;
        return "-1";
    }
    
    // Функция can_distribute
    auto can_distribute = [&](int k) -> bool {
        std::priority_queue<std::tuple<int, int, int>, 
                           std::vector<std::tuple<int, int, int>>, 
                           std::greater<>> heap;
        int j = 0;
        
        for (int i = 0; i < n; ++i) {
            while (j < n && j - k <= i) {
                if (a[j] > 0) {
                    heap.push({j + k, a[j], j});
                }
                ++j;
            }
            
            int candidates = b[i];
            
            while (candidates > 0 && !heap.empty()) {
                auto [right, count, original] = heap.top();
                
                if (right < i) {
                    return false;
                }
                
                int take_cand = std::min(candidates, count);
                candidates -= take_cand;
                
                if (count == take_cand) {
                    heap.pop();
                } else {
                    heap.pop();
                    heap.push({right, count - take_cand, original});
                }
            }
        }
        
        return heap.empty();
    };
    
    // Бинарный поиск
    int left = 0, right = n + 1;
    
    while (left < right) {
        int m = (left + right) / 2;
        
        if (can_distribute(m)) {
            right = m;
        } else {
            left = m + 1;
        }
    }
    
    int res = (right != n + 1) ? right : -1;
    std::cout << res << std::endl;
    return std::to_string(res);
}

int main() {
    main_function();
    return 0;
}