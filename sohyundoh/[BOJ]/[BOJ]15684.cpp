
#include <iostream>
#include <vector>
using namespace std;

int n, m, h;
bool flag;
int answer;
vector<vector<bool>> ladder_state(31, vector<bool>(10, false));
void dfs(int start_r, int goal_cnt, int ladder_cnt) {
	if (goal_cnt == ladder_cnt) {
		for (int c = 1; c <= n; c++) {
			int now_col = c;
			for (int r = 1; r <= h; r++) {
				if (now_col < n && ladder_state[r][now_col] == true) {
					now_col++;
				}
				else if (now_col > 1 && ladder_state[r][now_col - 1] == true) {
					now_col--;
				}
			}
			if (c != now_col) {
				break;
			}
			else if (c == n && c == now_col) {
				flag = true;
			}
		}
	}
	else {
		for (int i = start_r; i <= h; i++) {
			for (int j = 1; j < n; j++) {
				if (ladder_state[i][j] == true || j > 1 && ladder_state[i][j - 1] == true || j < n - 1 && ladder_state[i][j + 1] == true)
					continue;

				ladder_state[i][j] = true;
				dfs(i, goal_cnt, ladder_cnt + 1);
				if (flag)
					return;
				ladder_state[i][j] = false;
			}
		}
	}
	return;
}

int main() {
	cin >> n >> m >> h;
	int row, col;
	for (int i = 0; i < m; i++) {
		cin >> row >> col;
		ladder_state[row][col] = true;
	}
	flag = false;
	for (answer = 0; answer <= 3; answer++) {
		dfs(1, answer, 0);
		if (flag) {
			cout << answer;
			return 0;
		}
	}
	cout << -1;
	return 0;
}