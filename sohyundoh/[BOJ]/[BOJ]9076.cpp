#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N[5] = { 0, };
		int MAX[2] = { 0,0 }, MIN[2] = { 11,11 };
		int res = 0;
		int p, q;
		for (int k = 0; k < 5; k++) {
			cin >> N[k];
			if (MAX[0] < N[k]) {
				MAX[0] = N[k];
				p = k;
				continue;
			}
			if (MIN[0] > N[k]) {
				MIN[0] = N[k];
				q = k;
			}
		}
		N[p] = 0;
		N[q] = 0;
		for (int j = 0; j < 5; j++) {
			if (j == p || j == q) {
				continue;
			}
			if (MAX[1] < N[j]) {
				MAX[1] = N[j];
			}
			if (MIN[1] > N[j]) {
				MIN[1] = N[j];
			}
			res += N[j];
		}
		if (MAX[1] - MIN[1] >= 4) {
			cout << "KIN" << "\n";
		}
		else {
			cout << res << "\n";
		}

	}
}