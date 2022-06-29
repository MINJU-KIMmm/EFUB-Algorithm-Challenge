//
// Created by KangMinji on 2022-06-28.
//

#include <iostream>
#include <vector>
using namespace std;

void makeStar(int x, int y, int width, vector<vector<char>> &star){
    // 종료조건
    if (width == 1){
        star[x][y] = '*';
        return;
    }

    // 가운데 작은 별 생성 - index 이동 : x, y 인덱스는 +2, width는 -4
    makeStar(x+2, y+2, width-4, star);

    // 현재 별 채우기
    for (int i=x; i<x+width; i++)
        star[i][y] = star[x][i] = star[x + width - 1][i] = star[i][y+width-1] = '*';
}

int main(){
    int n;
    cin >> n;

    int width = 4*n - 3;
    vector<vector<char>> star(width, vector<char>(width, ' '));

    makeStar(0, 0, width, star);

    for (int i=0; i<width; i++){
        for (int j=0; j<width; j++)
            cout << star[i][j];
        cout << "\n";
    }

}