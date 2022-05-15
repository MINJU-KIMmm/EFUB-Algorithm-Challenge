//
// Created by KangMinji on 2022-05-04.
//

#include <iostream>
using namespace std;

// 시작 위치 초기화
int x=1, y=1;

// L, R, U, D 이동 방향
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};
char type[4] = {'L', 'R', 'U', 'D'};

int main(){
    int n;
    string plan;

    cin >> n;
    cin.ignore(); // 버퍼 비우기
    getline(cin, plan); // 버퍼를 비워준 다음에 한 라인 입력 가능

    int nx=0, ny=0;
    // 이동 좌표 계산
    for (int i=0; i<plan.size(); i++) {
        char dir = plan[i];
        for (int j = 0; j < 4; j++) {
            if (type[j] == dir) {
                nx = x + dx[j];
                ny = y + dy[j];
            }
        }
        // 범위 밖으로 벗어나는 경우 무시
        if (nx < 1 || ny < 1 || nx > n || ny > n){
            cout << "잡혔다";
            continue;
        }
        // 이동 수행
        x = nx;
        y = ny;
    }
    cout << x << ' ' << y << "\n";
}