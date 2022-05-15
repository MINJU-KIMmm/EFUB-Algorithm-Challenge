#include <iostream>
#include <algorithm>
using namespace std;
int main() {
	int N;
	cin >> N;
	int tc[100];
	int strike[100];
	int ball[100];
	int cnt = 0;
	int h, t, o, th, tt, to;
	bool flag[900] = { false, };
	for (int i = 0; i < N; i++) {
		int test_strike = 0, test_ball = 0;
		cin >> tc[i] >> strike[i] >> ball[i];
		h = tc[i] / 100;
		t = (tc[i] % 100) / 10;
		o = tc[i] - 100 * h - 10 * t;
		for (int j = 0; j < 900; j++) {
			th = (j + 100) / 100;
			tt = ((j + 100) % 100) / 10;
			to = (j + 100) % 10;
			if (th == tt || th == to || tt == to || tt == 0 || to == 0) {
				flag[j] = false;
				continue;
			}
			if (th == h) test_strike++;
			else if (th == o) test_ball++;
			if (tt == t) test_strike++;
			else if (tt == h) test_ball++;
			else if (tt == o) test_ball++;
			if (to == o) test_strike++;
			else if (to == h) test_ball++;
			else if (to == t) test_ball++;
			if (test_ball == ball[i] && test_strike == strike[i]) {
			}
			else {
				flag[j] = false;
			}
		}
	}
	for (int i = 0; i < 900; i++) {
		if (flag[i]) cnt++;
	}
	cout << cnt;
}