#include <iostream>
#include <algorithm>
using namespace std;
int card[300]; // ī�尪�� �Է¹��� �迭
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
				if (i == j || j == k || i == k) { //���� ī�带 ���� ���� ����
					continue;
				}
				int sum = card[i] + card[j] + card[k]; //ī�� ���� ������ �� ��� �ð����⵵: O(n^3)
				if (sum > max && sum <= tn) { //�Է¹��� ������ ������ ���� ū �� ã��
					max = sum;
					break;
				}
			}
		}
	}
	cout << max;
}