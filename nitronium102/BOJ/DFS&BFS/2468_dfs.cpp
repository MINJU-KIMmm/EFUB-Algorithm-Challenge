//
// Created by KangMinji on 2022-11-20.
//

#include <iostream>
#include <vector>
using namespace std;

int n;
vector<vector<int>> board;
vector<vector<bool>> visited;
int dx[] = {0, 0, -1, 1};
int dy[] = {-1, 1, 0, 0};

void dfs(int x, int y, int height){
    // 초기 방문 표시
    visited[x][y] = true;

    for (int i=0; i<4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (nx < 0 || nx >= n || ny < 0 || ny >=n ){
            continue;
        }
        if (!visited[nx][ny] && board[nx][ny] > height){
            dfs(nx, ny, height);
        }
    }
}

int countArea(int max_height) {
    int max_cnt = 1; // 안전영역 최대 개수

    for (int height = 1; height<max_height; height++){
        int cnt = 0;
        visited.assign(n, vector<bool>(n, false));

        for (int i=0; i<n; i++){
            for (int j=0; j<n; j++){
                // 방문하지 않았고, 물에 잠기지 않았다면 -> 영역 count
                if (!visited[i][j] && board[i][j] > height){
                    cnt++;
                    dfs(i, j, height);
                }
            }
        }
        max_cnt = max(cnt, max_cnt);
    }
    return max_cnt;
}

int main() {
    // 입력
    cin >> n;
    board.assign(n, vector<int>(n, 0));
    int max_height = 0;

    for(int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            cin >> board[i][j];
            max_height = max(max_height, board[i][j]);
        }
    }

    // 연산 & 출력
    cout << countArea(max_height) << "\n";
}