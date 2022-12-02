//
// Created by KangMinji on 2022-11-20.
//

#include <iostream>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

int dfs(int n, vector<vector<int>> &adj_list){
    int cnt = 0;

    vector<bool> visited(n+1, false);
    stack<int> q;

    // 수를 세는 방법
    // 1. 스택에 넣으면서 count
    // 2. 스택에서 빼면서 count
    // 3. 다 끝나고 방문배열 검사

    // 시작 정점
    q.push(1);
    visited[1] = true;

    // 탐색 시작
    while(!q.empty()){
        int curr = q.top();
        q.pop();

        for (auto next : adj_list[curr]){
            if (visited[next]){
                continue;
            }
            visited[next] = true;
            q.push(next);
            cnt++; // 1번 선택
        }
    }
    return cnt;
}

int bfs(int n, vector<vector<int>> &adj_list){
    int cnt = 0;

    vector<bool> visited(n+1, false);
    queue<int> q;

    // 수를 세는 방법
    // 1. 큐에 넣으면서 count
    // 2. 큐에서 빼면서 count
    // 3. 다 끝나고 방문배열 검사

    // 시작 정점
    q.push(1);
    visited[1] = true;

    // 탐색 시작
    while(!q.empty()){
        int curr = q.front();
        q.pop();

        for (auto next : adj_list[curr]){
            if (visited[next]){
                continue;
            }
            visited[next] = true;
            q.push(next);
            cnt++; // 1번 선택
        }
    }
    return cnt;
}

int main() {
    int n, m, a, b;

    // 입력
    cin >> n >> m;

    // 인접 리스트(연결된 정점 확인)
    vector<vector<int>> adj_list(n+1, vector<int>());

    while(m--) {
        cin >> a >> b;
        adj_list[a].push_back(b);
        adj_list[b].push_back(a);
    }

    cout << bfs(n, adj_list);
}