#include <cstdio>
#include <queue>

using namespace std;
queue<int> q;
int main() {
	int n;

	long ans = 1, num = 1;
	int some;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
		q.push(i);

	while (q.size() != 1) {
		ans = num * num * num;
		ans = ans % q.size();

		if (ans == 0) {
			ans = q.size();
		}
		for (int i = 0; i < ans - 1; i++) {
			some = q.front();
			q.pop();
			q.push(some);
		}
		num++;
		q.pop();
	}
	printf("%d", q.front());
}