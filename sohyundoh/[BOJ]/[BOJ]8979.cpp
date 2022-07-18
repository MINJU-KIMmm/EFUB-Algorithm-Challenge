#include <iostream>
using namespace std;

int main() {
	int N, K;
	cin >> N >> K;
	int Score[1000][3] = { {0,0,0}, };
	for (int i = 0; i < N; i++) {
		int C;
		cin >> C;
		for (int k = 0; k < 3; k++) {
			cin >> Score[C][k]; //메달 수 저장
		}
	}
	for (int i = 0; i < N; i++) {

	}
}