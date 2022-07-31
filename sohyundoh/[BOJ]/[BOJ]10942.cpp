#include <iostream>
#include <vector>
using namespace std;

int main() {
	//iostream과 stdio 버퍼 동기화시켜서 입력 빨리받아오자
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	//==============================================
	int n;
	cin >> n;
	vector<int> nums(n + 1, 0);
	for (int i = 1; i <= n; i++) cin >> nums[i];
	//dp에 nums에서 s,e에따라 펠린드롬 여부 기록.
	vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0)); //0이면 팰린드롬이 아니다.
	for (int i = 1; i <= n; i++) {
		dp[i][i] = 1;
		if (i < n && nums[i] == nums[i + 1]) dp[i][i + 1] = 1;
	}
	int start, end; //시작위치와 끝위치
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

	//m개의 명령에 따라 dp에서 팰린드롬 여부 찾아 출력
	int m, s, e;
	cin >> m;
	for (int i = 0; i < m; i++) {
		cin >> s >> e;
		cout << dp[s][e] << "\n";
	}
	return 0;
}