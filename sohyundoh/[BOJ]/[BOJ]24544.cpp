#include <iostream>

using namespace std;


int main(void) {
	int N;
	int A[1000];
	int B[1000];
	int All_interest = 0, View_interest = 0;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> A[i];
		All_interest += A[i];
	}
	for (int j = 0; j < N; j++) {
		cin >> B[j];
		if (B[j] == 1) {
			A[j] = 0;
		}
		else if (B[j] == 0) {
			B[j] = 1;
		}
		View_interest += B[j] * A[j];
	}
	cout << All_interest << '\n' << View_interest;
	return 0;
}