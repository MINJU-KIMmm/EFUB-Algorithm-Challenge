#include <iostream>
#include <deque>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int T; cin >> T;
	while (T--) {
		string p; cin >> p;
		int n; cin >> n;
		string arr; cin >> arr;
		deque<string> dq;
		bool isReversed = false;
		bool isError = false;

		string num;
		for (int i = 1; i < arr.length(); i++) {
			if (num != "" && (arr[i] == ',' || arr[i] == ']')) {
				dq.push_back(num);
				num = "";
				continue;
			}
			num += arr[i];
		}

		for (int i = 0; i < p.length(); i++) {
			if (p[i] == 'R') isReversed = !isReversed;
			else {
				if (dq.empty()) {
					isError = true;
					break;
				}
				if (!isReversed) dq.pop_front();
				else dq.pop_back();
			}
		}

		if (isError) {
			cout << "error\n";
			continue;
		}

		cout << '[';
		if (isReversed) {
			for (auto i = dq.rbegin(); i < dq.rend(); i++) {
				cout << *i;
				if (i != dq.rend() - 1) cout << ',';
			}
		}
		else {
			for (auto i = dq.begin(); i < dq.end(); i++) {
				cout << *i;
				if (i != dq.end() - 1) cout << ',';
			}
		}
		cout << "]\n";
	}
	return 0;
}