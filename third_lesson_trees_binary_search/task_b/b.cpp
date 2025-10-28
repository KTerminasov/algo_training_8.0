#include <bits/stdc++.h>

using namespace std;

const int INF = 100001;
int min_dist = INF;
vector<vector<int>> adj;

int dfs(int u, int p) {
    vector<int> heights;
    bool is_leaf = true;
    for (int v : adj[u]) {
        if (v == p) continue;
        is_leaf = false;
        int h = dfs(v, u);
        if (h != -1) {
            heights.push_back(h);
        }
    }
    if (is_leaf) {
        return 0;
    }
    if (heights.size() >= 2) {
        int min1 = INT_MAX, min2 = INT_MAX;
        for (int h : heights) {
            if (h < min1) {
                min2 = min1;
                min1 = h;
            } else if (h < min2) {
                min2 = h;
            }
        }
        min_dist = min(min_dist, min1 + min2 + 2);
    }
    if (heights.empty()) {
        return -1;
    }
    int min_h = INT_MAX;
    for (int h : heights) {
        min_h = min(min_h, h);
    }
    return min_h + 1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    adj.resize(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    if (n == 2) {
        cout << 1 << endl;
        return 0;
    }
    int root = -1;
    for (int i = 1; i <= n; i++) {
        if (adj[i].size() >= 2) {
            root = i;
            break;
        }
    }
    if (root == -1) {
        cout << INF << endl;
        return 0;
    }
    dfs(root, -1);
    cout << min_dist << endl;
    return 0;
}