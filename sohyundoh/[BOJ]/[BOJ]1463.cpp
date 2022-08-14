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
		//2�� 3���� ������ �������� �ʴ� ��츦 ����
		cnt[i] = cnt[i - 1] + 1;

		//3���� ������ ������ ��� ���� ���� ��
		if (i % 3 == 0)
			cnt[i] = min(cnt[i / 3] + 1, cnt[i]);

		//2�� ������ ������ ��� ���� 2���� ���� ��
		if (i % 2 == 0)
			cnt[i] = min(cnt[i / 2] + 1, cnt[i]);
	}

	cout << cnt[N];

	return 0;
}