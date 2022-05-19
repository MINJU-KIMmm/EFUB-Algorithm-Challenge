#include <iostream>
#include <queue>

using namespace std;
const int SIZE = 100000;

//그냥 특정 2점 사이의 최단거리 문제임
int bfs(int n, int k) {
    vector<int> check(SIZE + 1, 0);
    queue<int> q; //bfs는 queue
    int answer = 0;

    check[n] = 1; //시작 노드
    q.push(n);

    while (!q.empty()) {
        int x = q.front();
        q.pop();

        if (x == k) { //찾은경우
            answer = check[x] - 1;
            break;
        }

        vector<int> child = {x - 1, x + 1, x * 2}; //자식 노드

        for (int i = 0; i < 3; i++) { //자식 노드 queue에 넣기
            if (child[i] >= 0 && child[i] <= SIZE && !check[child[i]]) { //범위 내에 있고, 첫 방문이라면
                check[child[i]] = check[x] + 1;
                q.push(child[i]);
            }
        }
    }
    return answer;
}

int main() {
    int n, k;
    cin >> n >> k;
    cout << bfs(n, k) << '\n';
}