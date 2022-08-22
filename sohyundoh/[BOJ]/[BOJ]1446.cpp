#include <stdio.h>
#include <vector>
#include <queue>
using namespace std;
typedef pair<int, int> pii;

int d[10001], INF = -1000000000, vis[10001];
vector<pii> e[10001];
priority_queue<pii> pq;

int main() {
	int N, D;
	scanf("%d%d", &N, &D);

	while (N--) {
		int a, b, leng;
		scanf("%d%d%d", &a, &b, &leng);

		e[a].push_back({ -leng,b });
	}

	for (int i = 0; i < D; i++) {
		e[i].push_back({ -1,i + 1 });
	}

	for (int i = 1; i <= D; i++) {
		d[i] = INF;
	}

	pq.push({ 0,0 });

	while (!pq.empty()) {
		pii p = pq.top();
		pq.pop();
		if (vis[p.second]) continue;
		vis[p.second] = 1;

		if (p.first < d[p.second]) continue;
		for (pii np : e[p.second]) {
			if (d[np.second] < d[p.second] + np.first) {
				d[np.second] = d[p.second] + np.first;
				pq.push({ d[np.second],np.second });
			}
		}
	}
	printf("%d", -d[D]);
}