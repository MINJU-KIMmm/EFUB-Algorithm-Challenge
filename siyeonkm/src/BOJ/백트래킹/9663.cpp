#include <iostream>
#include <vector>

using namespace std;

int n;
int answer;
vector<bool> line; //열
vector<bool> left_line; //좌하향 대각선
vector<bool> right_line; //우하향 대각선

void nQueen(int cnt) {
	if (cnt == n) {
		answer = answer+1;
		return;
	}

    //우하향 대각선에 속한 애들은 다 행-열값이 똑같음
    //좌하향의 경우에는 다 행+열이 같음
    //근데 행-열은 음수일 수 있으니까 n을 더하는것
	for (int i = 0; i < n; i++) {
		if (!line[i] && !left_line[cnt+i] && !right_line[cnt-i+n]) {
			line[i] = true;
			left_line[cnt + i] = true;
			right_line[cnt - i + n] = true;
			nQueen(cnt+1);

			line[i] = false;
			left_line[cnt + i] = false;
			right_line[cnt - i + n] = false;
		}
	}
	return;
}

int main() {
	cin >> n;

	line.assign(n, false);
	left_line.assign(n*2, false); //cnt+i가 최대 n+n일 수 있으니까
	right_line.assign(n*2, false); //cnt-i+n이 최대 n-0+n일 수 있으니까

	answer = 0;
	nQueen(0);

	cout << answer;

}