//
// Created by KangMinji on 2022-11-20.
//

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<vector<bool>> adj_matrix;
vector<bool> visited_recur; // 재귀함수에서 사용할 방문체크
vector<int> order_recur;

void dfsRecur(int n, int curr) {
    // 종료조건
    if (visited_recur[curr]){
        return;
    }

    visited_recur[curr] = true;
    order_recur.push_back(curr);
    for (int next=1; next<=n; next++){
        if (adj_matrix[curr][next]){
            dfsRecur(n, next);
        }
    }
}

vector<int> bfs(int n, int v, vector<vector<bool>> &adj_matrix){
    vector<bool> visited(n+1, false); // 방문 체크
    queue<int> q;
    vector<int> order; // 정답 기록

    // 1) 시작 정점 넣기
    q.push(v);
    visited[v] = true;

    // 2) 탐색 수행
    while(!q.empty()){
        // 2-1) pop
        int curr = q.front();
        order.push_back(curr); // 순서 기록
        q.pop();

        // 2-2) 정점 번호가 작은 것부터 방문
        for (int next=1; next<=n; next++){
            // 간선이 없거나 이미 방문했다면
            if (!adj_matrix[curr][next] || visited[next]){
                continue;
            }
            // 방문 표기
            visited[next] = true;
            q.push(next);
        }
    }
    return order;
}

int main() {
    int n, m, v, a, b;

    // 입력
    cin >> n >> m >> v;

    // 인접 행렬 구현
    adj_matrix.assign(n+1, vector<bool>(n+1, false));
    visited_recur.assign(n+1, false);

    while(m--){
        cin >> a >> b;
        // 양방향 간선
        adj_matrix[a][b] = true;
        adj_matrix[b][a] = true;
    }

    // 연산
    dfsRecur(n, v);
    for (auto i : order_recur){
        cout << i << " ";
    }
    cout << "\n";
    auto ans = bfs(n, v, adj_matrix);
    for (auto i : ans){
        cout << i << " ";
    }

}