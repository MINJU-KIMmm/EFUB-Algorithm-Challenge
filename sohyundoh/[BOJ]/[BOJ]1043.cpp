#include <bits/stdc++.h>

#define OwO ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

using namespace std;

bool know[51];
int par[51];
vector<int> party[51];

int find(int u) {
    return par[u] == u ? u : par[u] = find(par[u]);
}

// ������ �ƴ� ����� �θ� �ǰԲ� merge
void merge(int u, int v) {
    u = find(u);
    v = find(v);
    if (u == v) return;
    if (know[u]) {
        par[v] = u;
    }
    else if (know[v]) {
        par[u] = v;
    }
    else {
        par[u] = v;
    }
}

int main() {
    OwO

        int n, m, k;
    cin >> n >> m >> k;
    // ������ �ƴ� ����� ���ٸ� ���� ����
    if (!k) {
        cout << m;
        return 0;
    }

    for (int i = 1; i <= n; ++i) par[i] = i;

    for (int i = 0; i < k; ++i) {
        int u;
        cin >> u;
        know[u] = 1;
    }

    // �� ��Ƽ���� ������� merge ���ְ�
    for (int i = 0; i < m; ++i) {
        int p, u;
        cin >> p >> u;
        party[i].push_back(u);
        for (int j = 0; j < p - 1; ++j) {
            int v;
            cin >> v;
            party[i].push_back(v);
            merge(u, v);
        }
    }

    // ��� ��Ƽ���� ����ĥ �� �ִٰ� �����ϰ� �����ؼ�
    int ans = m;
    // �� ��Ƽ���� ������ �ƴ� ����� ������ ���ֱ�
    for (int i = 0; i < m; ++i) {
        for (auto& j : party[i]) {
            if (know[find(j)]) {
                --ans;
                break;
            }
        }
    }
    cout << ans;

    return 0;
}