#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>

using namespace std;

vector<vector<bool>> adj_matrix; //인접행렬
vector<vector<int>> adj_list; //인접리스트

vector<bool> visited_re;

//DFS (재귀함수)
//노드가 작은 순으로 탐색해야 하는 문제이므로 재귀함수가 더 효율적이라고함
void dfsRe(int v) {
    if (visited_re[v])
        return;

    visited_re[v] = true; //방문했는지 확인
    cout << v << ' ';

    for (int i = 0; i < adj_list[v].size(); i++)
        dfsRe(adj_list[v][i]); //재귀적으로 계속 호출
}

//DFS
vector<int> dfs(int n, int v) {
    stack<int> st;
    vector<bool> visited(n + 1, false); //방문 노드 체크
    vector<int> result; //탐색순으로 노드 저장

    //첫부분 처리
    st.push(v);
    visited[v] = true;
    result.push_back(v);

    //탐색 시작
    while (!st.empty()) {
        int node = st.top(); //현재 탐색하려는 노드
        bool check = false; //연결 노드 존재 여부

        for (int i = 1; i <= n; i++) {
            if (adj_matrix[node][i] && !visited[i]) { //연결이 되어 있고, 처음 방문이라면
                check = true;
                visited[i] = true;
                st.push(i); //앞으로 탐색해야 할 노드이므로 스택에 삽입
                result.push_back(i); //탐색 노드 바로 삽입
                break; //이 문제에선 작은 노드부터 방문해야 하므로 바로 break
            }
        }
        if (!check)
            st.pop();
    }

    return result;
}

//BFS
vector<int> bfs(int n, int v) {
    queue<int> q;
    vector<bool> visited(n + 1, false); //방문 노드 체크
    vector<int> result; //탐색 순으로 정점 저장

    //첫부분 처리
    q.push(v);
    visited[v] = true;

    while (!q.empty()) {
        int node = q.front(); //현재 탐색하려는 노드
        q.pop();
        result.push_back(node);
        for (int i = 1; i <= n; i++) {
            if (adj_matrix[node][i] && !visited[i]) { //연결이 되어 있고, 처음 방문이라면
                visited[i] = true; //방문 체크
                q.push(i); //앞으로 탐색해야할 노드이므로 큐에 삽입
            }
        }
    }
    return result;
}

int main() {
    int n, m, v, a, b; //node, edge, 시작node, 간선 정보들
    vector<vector<int>> result(2, vector<int>()); //결과 저장 배열

    //입력
    cin >> n >> m >> v;
    adj_matrix.assign(n + 1, vector<bool>(n + 1, false));
    adj_list.assign(n + 1, vector<int>());
    while (m--) {
        cin >> a >> b;
        adj_matrix[a][b] = adj_matrix[b][a] = true;
        adj_list[a].push_back(b);
        adj_list[b].push_back(a);
    }

    //인접리스트 구현 시, 노드 번호가 작은 것부터 방문하기 위해 정렬해야 함
    for (int i = 1; i <= n; i++)
        sort(adj_list[i].begin(), adj_list[i].end());

    visited_re.assign(n + 1, false);
    dfsRe(v);
    result[1] = bfs(n, v);

    //출력
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < result[i].size(); j++) {
            cout << result[i][j] << ' ';
        }
        cout << '\n';
    }
    return 0;
}