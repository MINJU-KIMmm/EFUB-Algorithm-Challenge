#include <iostream>
#include <vector>
using namespace std;

int main() {
	//iostream�� stdio ���� ����ȭ���Ѽ� �Է� �����޾ƿ���
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	//==============================================
	int n;
	cin >> n;
	vector<int> nums(n + 1, 0);
	for (int i = 1; i <= n; i++) cin >> nums[i];
	//dp�� nums���� s,e������ �縰��� ���� ���.
	vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0)); //0�̸� �Ӹ������ �ƴϴ�.
	for (int i = 1; i <= n; i++) {
		dp[i][i] = 1;
		if (i < n && nums[i] == nums[i + 1]) dp[i][i + 1] = 1;
	}
	int start, end; //������ġ�� ����ġ
	for (int i = 1; i <= n; i++) {
		start = i - 1; end = i + 1;
		while (start >= 1 && end <= n) {
			if (dp[start + 1][end - 1] == 1 && nums[start] == nums[end]) dp[start][end] = 1;
			start--;
			end++;
		}
	}
	for (int i = 1; i < n; i++) {
		start = i - 1; end = i + 2;
		while (start >= 1 && end <= n) {
			if (dp[start + 1][end - 1] == 1 && nums[start] == nums[end]) dp[start][end] = 1;
			start--;
			end++;
		}
	}

	//m���� ��ɿ� ���� dp���� �Ӹ���� ���� ã�� ���
	int m, s, e;
	cin >> m;
	for (int i = 0; i < m; i++) {
		cin >> s >> e;
		cout << dp[s][e] << "\n";
	}
	return 0;
}