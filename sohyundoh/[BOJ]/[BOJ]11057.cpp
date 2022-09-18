#include <iostream>
#include <vector>

using namespace std;

const int MOD = 10007;

int increasingNum(int n) { // ������ �� ����
    // dp[i][j] : i��° �ڸ��� j�� �� �� �ִ� ����� ��
    vector<vector<int>> dp(n, vector<int>(10, 0));
    for (int i = 0; i < 10; i++) dp[n - 1][i] = 1; // n-1��° �ڸ��� i�� �� �� �ִ� ����� ��

    for (int i = n - 2; i >= 0; i--) { // i : �ڸ�
        for (int j = 0; j < 10; j++) { // j : i��° �ڸ���
            for (int k = j; k < 10; k++)
                dp[i][j] += dp[i + 1][k];
            dp[i][j] %= MOD;
        }
    }

    int ans = 0;
    for (int i = 0; i < 10; i++) ans += dp[0][i];
    return ans % MOD;
}

int main() {
    int n;
    cin >> n;

    cout << increasingNum(n);
    return 0;
}
