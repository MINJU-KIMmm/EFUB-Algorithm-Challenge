//
// Created by KangMinji on 2022-05-08.
//

/*
 * 1) 수평으로 두 칸 -> 수직으로 한 칸
 * 2) 수직으로 두 칸 -> 수평으로 한 칸
 */

#include <iostream>
using namespace std;

int dx[8] = {-1, 1, -1, 1, -2, -2, 2, 2};
int dy[8] = {2, 2, -2, -2, 1, -1, 1, -1};

int main(){
    string input;
    int column, row;

    /* char과 int로도 받을 수 있음
    char c;
    int r;

    cin >> c >> r;
    */
    
    cin >> input;
    column = input[0] - 'a' + 1;
    row = input[1] - '0';

    int cnt = 0;
    for (int i=0; i<8; i++){
        int nr = row + dx[i];
        int nc = column + dy[i];
        if (nr >=1 && nr <=8 && nc >=1 && nr <= 8){
            cnt++;
        }
    }
    cout << cnt << "\n";
}