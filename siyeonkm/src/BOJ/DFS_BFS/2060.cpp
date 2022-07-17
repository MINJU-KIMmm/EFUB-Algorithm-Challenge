#include <iostream>
#include <vector>
#include <queue>
#include <stack>

using namespace std;

int dfs(int n, vector<vector<int>> &adj_list){
    int count = 0;
    stack<int> s;
    vector<bool> visited(n+1, false);

    s.push(1);
    visited[1] = true;

    while (!s.empty()){
        int curr = s.top();
        s.pop();

        // curr에 연결되어 있는 모든 인접 정점(컴퓨터)에 대해
        for (auto next: adj_list[curr]) {
            if (visited[next]) {
                continue;
            }
            visited[next] = true;
            s.push(next); // 스택에 삽입 -> 1번으로 할거면 여기서 카운트
            count++;
        }
    }
    return count;
}

int bfs(int n, vector<vector<int>> &adj_list){
    int count = 0;
    queue<int> q;
    vector<bool> visited(n+1, false);

    q.push(1);
    visited[1] = true;

    while (!q.empty()){
        int curr = q.front();
        q.pop();

        // curr에 연결되어 있는 모든 인접 정점(컴퓨터)에 대해
        for (auto next: adj_list[curr]) {
            if (visited[next]) {
                continue;
            }
            visited[next] = true;
            q.push(next);
            count++;
        }
    }
    return count;
}

int main() {
    int n, m, a, b;
    cin >> n >> m;

    vector<vector<int>> adj_list(n+1, vector<int>());

    for(int i=0; i<m; i++) {
        cin >> a >> b;
        adj_list[a].push_back(b);
        adj_list[b].push_back(a);
    }

    cout << dfs(n, adj_list);
}