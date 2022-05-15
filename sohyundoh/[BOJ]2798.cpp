#include <iostream>
#include <algorithm>
using namespace std;
int card[300]; // 카드값을 입력받을 배열
int main() {
	int n, tn;
	cin >> n >> tn;
	int max = 0;
	for (int i = 0; i < n; i++) {
		cin >> card[i];
	}
	for (int j = 0; j < n; j++) {
		for (int k = 0; k < n; k++) {
			for (int i = 0; i < n; i++) {
				if (i == j || j == k || i == k) { //같은 카드를 뽑을 수는 없음
					continue;
				}
				int sum = card[i] + card[j] + card[k]; //카드 값을 일일이 다 계산 시간복잡도: O(n^3)
				if (sum > max && sum <= tn) { //입력받은 값보다 작은데 가장 큰 값 찾기
					max = sum;
					break;
				}
			}
		}
	}
	cout << max;
}