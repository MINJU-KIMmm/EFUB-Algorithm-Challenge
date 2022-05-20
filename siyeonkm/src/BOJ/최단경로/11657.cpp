#include <iostream>
#include <vector>
#include <tuple>

using namespace std;
typedef long long ll;
typedef tuple<int, int, int> ti;
const int INF = 1e6 * 5;

vector<ll> bellmanFord(int n, int m, int start, vector<ti> &edges) {
    //int 범위를 벗어남. 언더플로우때문에!
    vector<ll> dist(n + 1, INF);
    dist[start] = 0;

    for (int i = 1; i <= n; i++) {
        bool flag = true; //탈출용
        for (int j = 0; j < m; j++) {
            int s = get<0>(edges[j]);
            int d = get<1>(edges[j]);
            int w = get<2>(edges[j]);

            if (dist[s] == INF) //시작점하고 이어지지않은 node임 최단거리 측정불가!
                continue;
            ll next_weight = w + dist[s];
            if (dist[d] > next_weight) { //짧은 경로 발견
                if (i == n) //음의 사이클 발생했다는 이야기임
                    return {INF + 1};
                dist[d] = next_weight;
                flag = false;
            }
        }
        if (flag) //true라는거는 갱신이 더이상 불가능하다는 소리
            break;
    }
    return dist;
}

int main() {
    int n, m, a, b, c;
    cin >> n >> m;
    vector<ti> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> a >> b >> c;
        edges[i] = {a, b, c};
    }

    vector<ll> ans = bellmanFord(n, m, 1, edges);

    if (ans[0] == INF + 1) {
        cout << -1;
        return 0;
    }
    for (int i = 2; i <= n; i++)
        cout << ((ans[i] == INF) ? -1 : ans[i]) << '\n';
}