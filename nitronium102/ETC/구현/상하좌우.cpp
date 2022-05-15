//
// Created by KangMinji on 2022-05-04.
//

#include <iostream>
using namespace std;

// ���� ��ġ �ʱ�ȭ
int x=1, y=1;

// L, R, U, D �̵� ����
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};
char type[4] = {'L', 'R', 'U', 'D'};

int main(){
    int n;
    string plan;

    cin >> n;
    cin.ignore(); // ���� ����
    getline(cin, plan); // ���۸� ����� ������ �� ���� �Է� ����

    int nx=0, ny=0;
    // �̵� ��ǥ ���
    for (int i=0; i<plan.size(); i++) {
        char dir = plan[i];
        for (int j = 0; j < 4; j++) {
            if (type[j] == dir) {
                nx = x + dx[j];
                ny = y + dy[j];
            }
        }
        // ���� ������ ����� ��� ����
        if (nx < 1 || ny < 1 || nx > n || ny > n){
            cout << "������";
            continue;
        }
        // �̵� ����
        x = nx;
        y = ny;
    }
    cout << x << ' ' << y << "\n";
}