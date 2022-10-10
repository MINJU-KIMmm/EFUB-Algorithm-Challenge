#include <iostream>
#include <string>
using namespace std;

int main(void) {
	int alpha[26];
	for (int j = 0; j < 26; j++) {
		alpha[j] = -1;
	}
	string a;
	cin >> a;
	for (int i = 0; i < a.length(); i++) {
		if (alpha[(int)a[i] - (int)'a'] != -1) continue;
		alpha[(int)a[i] - (int)'a'] = i;
	}
	for (int k = 0; k < 26; k++) {
		cout << alpha[k] << ' ';
	}
}