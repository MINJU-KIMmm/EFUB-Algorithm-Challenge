#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int n;

int main() {
	//iostream�� stdio ���� ����ȭ���Ѽ� �Է� �����޾ƿ���
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	//==============================================
	cin >> n;
	vector<long long> liquids(n, 0);
	for (int i = 0; i < n; i++) {
		cin >> liquids[i];
	}
	sort(liquids.begin(), liquids.end());

	//a,b����� ������������ ã��, ������ c�� lower_bound�� �������.
	long long a, b, c;
	long long chosen_a, chosen_b, chosen_c;
	long long min_abs = 3000000010;
	for (int i = 0; i < liquids.size() - 2; i++) {
		a = liquids[i];
		for (int j = i + 1; j < liquids.size() - 1; j++) {
			b = liquids[j];
			//lower_bound
			int l, r;
			l = j + 1; //low
			r = liquids.size() - 1;
			int idx_c = lower_bound(liquids.begin() + l, liquids.begin() + r, -a - b) - liquids.begin();
			//l~r���̿� ������
			if (idx_c > liquids.size() - 1) {
				c = liquids[liquids.size() - 1];
			}
			//������ idx_c�� idx_c-1�� �� ������ ����
			else if (idx_c > l) {
				if (abs(a + b + liquids[idx_c]) < abs(a + b + liquids[idx_c - 1])) {
					c = liquids[idx_c];
				}
				else {
					c = liquids[idx_c - 1];
				}
			}
			//idx_c�� l�϶�
			else {
				c = liquids[idx_c];
			}
			if (min_abs > abs(a + b + c)) {
				min_abs = abs(a + b + c);
				chosen_a = a;
				chosen_b = b;
				chosen_c = c;
			}
		}
	}
	cout << chosen_a << " " << chosen_b << " " << chosen_c;
	return 0;
}