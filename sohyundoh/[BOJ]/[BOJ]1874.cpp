#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int main() {
	cin.tie(NULL); cout.tie(NULL); ios::sync_with_stdio(false);

	vector<char> ans;
	stack<int> save;
	int cnt = 1;

	int n; cin >> n;
	int tmp;
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		while (cnt <= tmp) {
			save.push(cnt);
			cnt++;
			ans.push_back('+');
		}
		if (save.top() == tmp) {
			save.pop();
			ans.push_back('-');
		}
		else {
			cout << "NO";
			return 0;
		}
	}

	for (int i = 0; i < ans.size(); i++) cout << ans[i] << "\n";

	return 0;
}