#include <iostream>
#include <algorithm>
using namespace std;
float solution(int x, int y, int k) {
	float expect;
	int mid1 = (x + y) / 2 - 1, mid2 = (x + y) / 2 + 1;
	int a = max(x, mid1);
	int b = min(y, mid2);
	int ask = a;
	for (a; a < b; a++) {
		if (a > k) {

		}
	}

	return expect;
}
int main(void) {
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		int x, y, k;
		cin >> x >> y >> k;
		cout << solution(x, y, k);
	}
	return 0;
}





