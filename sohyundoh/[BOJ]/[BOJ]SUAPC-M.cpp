#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

int combination(int n, int r)
{
	if (n == r || r == 0)
		return 1;
	else if (r == 1)
		return n;
	else
		return combination(n - 1, r - 1) + combination(n - 1, r);
}
int main(void) {

	int N;
	cin >> N;
	int printnum = 1;
	vector<int> a(N), b(N);
	for (int i = 0; i < N; i++) {
		cin >> a[i] >> b[i];
	}
	for (int i = 0; i < N; i++) {
		int answer = 0;
		if (a[i] > b[i]) {
			for (int j = 1; j <= b[i]; j++) {
				answer += combination(b[i], j) * combination(a[i], j);
			}
		}
		else {
			for (int k = 1; k <= a[i]; k++) {
				answer += combination(b[i], k) * combination(a[i], k);
			}
		}
	}

	cout << printnum % int(pow(10, 9) + 7);
	return 0;
}