//
// Created by KangMinji on 2022-11-20.
//

#include <iostream>
#include <queue>
using namespace std;
typedef pair<int, int> ci;

void bfs(int x, int y, int height, int n,
         vector<vector<int>> &board, vector<vector<bool>> &visited){

    int dx[] = {0, 0, -1, 1};
    int dy[] = {1, -1, 0, 0};
    queue<ci> q;

    // 시작 지점 넣기
    q.push({x, y});
    visited[x][y] = true;

    // 탐색 시작
    while(!q.empty()){
        int a = q.front().first;
        int b = q.front().second;
        q.pop();

        for (int i=0; i<4; i++){
            int nx = a + dx[i];
            int ny = b + dy[i];
            if (nx < 0 || nx >= n || ny < 0 || ny >= n){
                continue;
            }
            if (!visited[nx][ny] && board[nx][ny] > height){
                visited[nx][ny] = true;
                q.push({nx, ny});
            }
        }
    }
}

int countArea(int n, int max_height, vector<vector<int>> &board){
    int max_cnt = 1; // 안전지역 최대 개수

    for (int height=1; height<max_height; height++){
        vector<vector<bool>> visited(n, vector<bool>(n, false));

        int cnt = 0; // 안전 지역 개수
        for (int i=0; i<n; i++){
            for (int j=0; j<n; j++){
                // 방문한 적 없고, 물에 잠기지 않았으면
                if (!visited[i][j] && board[i][j] > height){
                    bfs(i, j, height, n, board, visited);
                    cnt++;
                }
            }
        }
        max_cnt = max(max_cnt, cnt);
    }
    return max_cnt;
}

// 일정한 높이 이하의 "모든" 지점은 물에 잠긴다
// 강수량을 체크하면서 [안전구역 최대 개수]릁 탐구해야 함
int main() {
    int n;

    // 입력
    cin >> n;
    vector<vector<int>> board(n, vector<int>(n, 0));
    int max_height = 0;
    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            cin >> board[i][j];
            max_height = max(board[i][j], max_height);
        }
    }
    cout << countArea(n, max_height, board) << "\n";
}