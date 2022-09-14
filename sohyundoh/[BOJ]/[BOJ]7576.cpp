#include <iostream>
#include <vector>
#include <queue>
using namespace std;

typedef struct {
    int x;     int y;    int day;
}tomato;

vector<int> dx = { -1,0,0,1 };
vector<int> dy = { 0,1,-1,0 };
vector<vector<int>> map;
vector<vector<int>> visited;

queue<tomato> q;
int m, n; //n이 행, m이 열
int x, y, day, xx, yy;
int rst;

int isArea(int a, int b) {
    if (a < n && a >= 0 && b < m && b >= 0) return 1;
    else
        return 0;
}

void print_tomato() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << map[i][j] << " ";
        }
        cout << endl;
    }
}

void bfs() {
    while (!q.empty()) {
        x = q.front().x; //행
        y = q.front().y; //열
        day = q.front().day; //day

        q.pop();

        visited[x][y] = 1;
        rst = day;


        for (int i = 0; i < 4; i++) {
            xx = x + dx[i];
            yy = y + dy[i];

            if (isArea(xx, yy)) {
                if (!visited[xx][yy] && map[xx][yy] == 0) {
                    map[xx][yy] = 1;
                    visited[xx][yy] = 1;
                    q.push({ xx, yy, day + 1 });
                    //cout<<q.size()<<" "<<" "<<xx<<yy<< i<<endl;
                }
            }

            //cout<<i<<" i 값"<<endl;
            //cout<<q.size()<<" "<< i<<endl;
        }

        //cout<<q.size()<<endl;


    }
    //cout<<"******"<<endl;
    //print_tomato();
}





int main() {
    cin >> m >> n;
    //주어진 (m,n) 벡터 생성 후 -1로 초기화 >> 나중에 토마토 익지 못했을 때 어떻게?
    map.resize(n, vector<int>(m, -1));
    visited.resize(n, vector<int>(m, 0));

    //주어진 map 입력하기
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> map[i][j];
            if (map[i][j] == 1)
                q.push({ i, j, 0 });
        }
    }

    bfs();

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (map[i][j] == 0) {
                cout << -1 << endl;
                return 0;
            }
        }
    }

    cout << rst << endl;

    return 0;




}