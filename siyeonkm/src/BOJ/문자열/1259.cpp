#include <iostream>
#include <string>

using namespace std;

int main() {
	string input;
	bool yes = true;

	while (true) {
		cin >> input;
		if (input == "0") break;

		for (int i = 0; i < input.size() / 2; i++) {
			if (input[i] != input[input.size() - (i + 1)]) {
				yes = false;
				break;
			}
		}

		if (yes) cout << "yes" << "\n";
		else {
			cout << "no" << "\n";
			yes = true;
		}
	}
}