#include <iostream>
#include <vector>

using namespace std;

int n, m;
vector<int> num;

void backtracking(int cnt, int prev) {
	if (cnt == m) {
		for (int i = 0; i < cnt; i++) {
			cout << num[i] << ' ';
		}
		cout << "\n";
		return;
	}

	for (int i = prev+1; i <= n; i++) {
		num[cnt] = i;
		backtracking(cnt + 1, i);
	}
}

int main() {
	cin >> n >> m;
	num.assign(m, 0);

	backtracking(0, 0);

}