#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 //다시 풀어보기
int main(void) {
	int N, M;
	cin >> N;
	vector<int> A;
	for (int i = 0; i < N; i++) {
		int a;
		cin >> a;
		A.push_back(a);
	}
	cin >> M;
	vector<int> X;
	for (int i = 0; i < M; i++) {
		int x;
		cin >> x;
		X.push_back(x);
	}
	for (int k = 0; k < M; k++) {
		if (*find(A.begin(), A.end(), X[k]) == X[k]) cout << 1 << '\n';
		else cout << 0 << '\n';
	}
}