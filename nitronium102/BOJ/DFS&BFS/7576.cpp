//
// Created by KangMinji on 2022-11-20.
//

#include <iostream>
#include <queue>

using namespace std;
typedef pair<int, int> ci;

// 상하좌우
int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

/* 최소 일수 - bfs */
int bfs(int n, int m, int cnt, vector<vector<int>> &box, queue<ci> &q) {
    int time = 0;

    // 방문 배열 필요없음! box 사용하기

    while (!q.empty()) {
        int r = q.front().first;
        int c = q.front().second;

        q.pop();
        time = box[r][c]; // 🔥 그냥 ans로 하면 토마토 익을 때마다 추가돼서 값 크게 난옴

        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];

            if (nr >= 0 && nr < n && nc >= 0 && nc < m && box[nr][nc] == 0) {
                q.push({nr, nc});
                box[nr][nc] = time+1; // 방문 체크
                cnt--; // 토마토가 새로 익음
            }
        }
    }
    return (cnt == 0) ? time-1 : -1;
}

int main() {
    int n, m; // 행, 열

    // 입력
    cin >> m >> n;
    vector<vector<int>> box(n, vector<int>(m, 0));
    queue<ci> q;

    int cnt = 0; // 익지 않은 토마토의 개수
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> box[i][j];
            // 이미 익은 토마토의 좌표를 넣음 -> 시작 정점
            if (box[i][j] == 1) {
                q.push({i, j});
            } else if (box[i][j] == 0) {
                cnt++;
            }
        }
    }

    cout << bfs(n, m, cnt, box, q);
}