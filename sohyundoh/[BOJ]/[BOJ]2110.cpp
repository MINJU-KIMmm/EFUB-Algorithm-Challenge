#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
long long x[200000];
void cal(long long x[], int n, int c) {
	vector<long long> v;
	for (int j = 0; j < n; j++) {
		v.push_back(x[j]);
	}
	sort(v.begin(), v.end()); //�Է¹��� �迭�� ���� ��� ����
	long long start = 1, end = v[n - 1] - v[0]; //1�� , �Ÿ��� ���� ū ���̰� ���� ���� ����.
	int temp = 0;//������ ���� �Ÿ� �����ִ� ����
	while (start <= end) {
		long long home = v[0]; //���� ���� ��ǥ�� ���� �� ������ ����
		long long mid = (start + end) / 2; //1�� �Ÿ��� ���� �� ���� ���� ���� ������ ����
		int cnt = 1;//�������� ������ �����ִ� ����
		for (int k = 0; k < n; ++k) {
			if (v[k] - home >= mid) {//���� ���� ��ǥ�� ���� �������� �Ÿ��� mid ���� ũ�ٸ� 
				++cnt;//cnt�� Ű����
				home = v[k];//�׸��� home �ٲٱ� 
			}
			if (cnt >= c) { //cnt ���� ������ �������� ���ų� ���ٸ�
				temp = mid;//������ ���� �Ÿ��� mid�� ����
				start = mid + 1;//���� ���̱�
			}
			else {
				end = mid - 1;//���� ���߱�
			}
		}
	}
	cout << temp;
}
int main(void) {
	int n, c;
	cin >> n >> c;
	for (int i = 0; i < n; i++) {
		cin >> x[i];
	}
	cal(x, n, c);
}
