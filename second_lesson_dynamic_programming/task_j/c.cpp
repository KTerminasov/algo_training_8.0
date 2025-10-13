#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

const ll INF = 1000000000LL;

const ll BIG = 1000000000000000000LL;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, l;
    cin >> n >> l;

    vector<vector<int>> stores(n, vector<int>(4));
    int max_opt = 1;
    for (int i = 0; i < n; i++) {
        cin >> stores[i][0] >> stores[i][1] >> stores[i][2] >> stores[i][3];
        max_opt += stores[i][3];
    }

    vector<vector<ll>> dp(n + 1, vector<ll>(max_opt, INF));
    dp[0][0] = 0;

    auto cost_func = [&](int i, int j) -> ll {
        if (j == 0) return 0;
        if (j > stores[i][3]) return INF;
        if (j < stores[i][1]) return (ll)j * stores[i][0];
        return (ll)j * stores[i][2];
    };

    for (int i = 1; i <= n; i++) {
        int P = stores[i - 1][0];
        int R = stores[i - 1][1];
        int Q = stores[i - 1][2];
        int F = stores[i - 1][3];

        for (int jj = 0; jj < max_opt; jj++) {
            dp[i][jj] = dp[i - 1][jj];
        }

        auto update_range = [&](int low, int high, int C) {
            if (low > high) return;
            deque<int> dq;
            for (int j = low; j < max_opt; j++) {
                int m_new = j - low;
                if (m_new >= 0 && dp[i - 1][m_new] < INF) {
                    ll f_new = dp[i - 1][m_new] - (ll)m_new * C;
                    while (!dq.empty() && (dp[i - 1][dq.back()] - (ll)dq.back() * C) >= f_new) {
                        dq.pop_back();
                    }
                    dq.push_back(m_new);
                }
                int left = max(0, j - high);
                while (!dq.empty() && dq.front() < left) {
                    dq.pop_front();
                }
                if (!dq.empty()) {
                    int m_min = dq.front();
                    ll min_f = dp[i - 1][m_min] - (ll)m_min * C;
                    ll new_val = min_f + (ll)j * C;
                    if (new_val < dp[i][j]) {
                        dp[i][j] = new_val;
                    }
                }
            }
        };

        int low1 = 1;
        int high1 = min(R - 1, F);
        if (low1 <= high1) {
            update_range(low1, high1, P);
        }

        int low2 = R;
        int high2 = F;
        if (low2 <= high2) {
            update_range(low2, high2, Q);
        }
    }

    ll min_cost = INF;
    int best_total = -1;
    for (int j = l; j < max_opt; j++) {
        if (dp[n][j] < min_cost) {
            min_cost = dp[n][j];
            best_total = j;
        }
    }

    if (min_cost >= INF) {
        cout << -1 << endl;
        return 0;
    }

    vector<int> amounts(n);
    int j = best_total;
    for (int i = n; i >= 1; i--) {
        int F = stores[i - 1][3];
        bool found = false;
        for (int a = 0; a <= F; a++) {
            int prev_j = j - a;
            if (prev_j < 0) continue;
            ll c = cost_func(i - 1, a);
            if (c >= INF) continue;
            if (dp[i - 1][prev_j] + c == dp[i][j]) {
                amounts[i - 1] = a;
                j = prev_j;
                found = true;
                break;
            }
        }
        assert(found);
    }

    cout << min_cost << endl;
    for (int i = 0; i < n; i++) {
        if (i > 0) cout << " ";
        cout << amounts[i];
    }
    cout << endl;

    return 0;
}