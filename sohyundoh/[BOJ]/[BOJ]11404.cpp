#include <iostream>
#include <vector>

using namespace std;

const int INF = 1e7;
vector<vector<int>> graph;

void floyd_warshall(int n) {
    for (int k = 1; k <= n; k++) { // k ���ø� ��������
        for (int i = 1; i <= n; i++) { // ������ : i ����
            for (int j = 1; j <= n; j++) { // ������ : j ����
                int dist = graph[i][k] + graph[k][j];
                graph[i][j] = min(graph[i][j], dist);
            }
        }
    }
}
int main() {
    int n, m, a, b, c;
    cin >> n >> m;

    graph.assign(n + 1, vector<int>(n + 1, INF));
    for (int i = 1; i <= n; i++)
        graph[i][i] = 0;

    while (m--) { // ���� ����
        cin >> a >> b >> c;
        // (a ���ÿ� b ���ø� �����ϴ� �뼱�� �ϳ��� �ƴ� �� ����)
        graph[a][b] = min(graph[a][b], c);
    }

    floyd_warshall(n);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (graph[i][j] == INF) cout << 0 << ' ';
            else cout << graph[i][j] << ' ';
        }
        cout << '\n';
    }
    return 0;
}
[��ó] [���� / C++] 11404�� �÷��̵� | �ۼ��� ����������