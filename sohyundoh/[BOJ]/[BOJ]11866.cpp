#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
int main() { //1���� N���� Queue�� ������ ���� K-1�� �տ� �ִ� �� �ڿ� ���̰� pop�Ѵ�.
	int N, K;
	cin >> N >> K;
	queue<int> q;
	for (int i = 0; i < N; i++) {
		q.push(i + 1);
	}
	cout << "<";
	while (!q.empty()) {
		for (int i = 0; i < K - 1; i++) {
			q.push(q.front());//front ��Ҹ� push
			q.pop();//push�� ��Ҹ� front���� pop
		}
		cout << q.front();
		q.pop();
		if (!q.empty()) {
			cout << ", ";
		}
	}
	cout << ">";
}