#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
int main() { //1부터 N까지 Queue에 저장한 다음 K-1번 앞에 있는 걸 뒤에 붙이고 pop한다.
	int N, K;
	cin >> N >> K;
	queue<int> q;
	for (int i = 0; i < N; i++) {
		q.push(i + 1);
	}
	cout << "<";
	while (!q.empty()) {
		for (int i = 0; i < K - 1; i++) {
			q.push(q.front());//front 요소를 push
			q.pop();//push한 요소를 front에서 pop
		}
		cout << q.front();
		q.pop();
		if (!q.empty()) {
			cout << ", ";
		}
	}
	cout << ">";
}