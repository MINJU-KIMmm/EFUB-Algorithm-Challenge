#include <iostream>
using namespace std;

int main() {
	string table[8] = { "c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=" };
	string input; cin >> input;
	int answer = 0;

	for (int i = 0; i < input.length(); i++) {
		for (int j = 0; j < 8; j++) {
			if (input.find(table[j], i) == i) {
				answer++;
				i += table[j].length() - 1;
				break;
			}
			if (j == 7) answer++;
		}
	}

	cout << answer;
	return 0;
}