#include <iostream>
#include <vector>

using namespace std;

bool rows[9][10] = { 0, };
bool cols[9][10] = { 0, };
bool areas[9][10] = { 0, };
vector<pair<int, int>> blank_cord;

//좌표를 영역으로 바꿔주는 함수
int find_area(int x, int y) {
    return 3 * (x / 3) + (y / 3);
}

bool backtracking(int k, int l, vector<vector<int>>* answer) {
    if (k == l) return true; //마지막까지 다 채웠으면 리턴
    auto [x, y] = blank_cord[k];
    int a = find_area(x, y);

    //1~9까지 검사
    for (int num = 1; num < 10; num++) {
        //가로, 세로, 영역 체크해서 해당 수를 넣어도 괜찮으면 진행
        if (!rows[x][num] && !cols[y][num] && !areas[a][num]) {
            rows[x][num] = 1;
            cols[y][num] = 1;
            areas[a][num] = 1;

            (*answer)[x][y] = num;

            //다음에도 잘 채워지면 true를 리턴
            if (backtracking(k + 1, l, answer)) return true;
            //재귀로 진행하다가 안들어가서 막히는경우 발생
            else {
                rows[x][num] = 0; //다 없던일로 하기
                cols[y][num] = 0;
                areas[a][num] = 0;
            }
        }
    }
    return false;
}

vector<vector<int>> solution(vector<vector<int>> sudoku) {
    vector<vector<int>> answer(9, vector<int>(9, 0));
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (sudoku[i][j] == 0) blank_cord.push_back({ i, j });
            else {
                rows[i][sudoku[i][j]] = 1;
                cols[j][sudoku[i][j]] = 1;
                areas[find_area(i, j)][sudoku[i][j]] = 1;
                answer[i][j] = sudoku[i][j];
            }
        }
    }
    int l = blank_cord.size();
    backtracking(0, l, &answer);
    return answer;
}


int main() {
    vector<vector<int>> sudoku(9, vector<int>(9));
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) cin >> sudoku[i][j];
    }
    auto output = solution(sudoku);
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) cout << output[i][j] << ' ';
        cout << '\n';
    }
    return 0;
}