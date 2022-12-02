#include <iostream>
#include <queue>
using namespace std;
typedef pair<int, int> ci;

/*
배추 구역 하나당 배추흰지렁이 1마리
인접이므로 bfs 사용
*/
void bfs(int x, int y, int n, int m, vector<vector<bool>> &board){
    int dx[4] = {0, 0, -1, 1};
    int dy[4] = {1, -1, 0, 0};
    queue<ci> q;

    // 첫 지점 표시
    q.push({x, y});
    board[x][y] = false;

    // 인접 지역 탐색 수행
    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m){
                continue;
            }
            if (board[nx][ny]) {
                board[nx][ny] = false;
                q.push({nx, ny});
            }
        }
    }

}

int main() {
    int t, m, n, k, x, y;

    // 입력
    cin >> t;
    while(t--){
        cin >> m >> n >> k;
        vector<vector<bool>> board(n, vector<bool>(m, false));
        while(k--){
            cin >> x >> y;
            board[y][x] = true;
        }

        // 연산
        int cnt = 0; // 구역의 개수
        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++){
                if (board[i][j]){ // 새로운 구역 발견
                    cnt++; // 구역의 개수 증가
                    bfs(i, j, n, m, board); // 인접 구역 방문 표시
                }
            }
        }
        cout << cnt << "\n";
    }
}