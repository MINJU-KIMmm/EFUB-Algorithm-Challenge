#include <iostream>
using namespace std;

int main()
{
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	int N;
	cin >> N;

	int* cnt = new int[N + 1]();
	for (int i = 2; i <= N; i++)
	{
		//2나 3으로 나누어 떨어지지 않는 경우를 가정
		cnt[i] = cnt[i - 1] + 1;

		//3으로 나누어 떨어질 경우 위의 경우와 비교
		if (i % 3 == 0)
			cnt[i] = min(cnt[i / 3] + 1, cnt[i]);

		//2로 나누어 떨어질 경우 위의 2가지 경우와 비교
		if (i % 2 == 0)
			cnt[i] = min(cnt[i / 2] + 1, cnt[i]);
	}

	cout << cnt[N];

	return 0;
}