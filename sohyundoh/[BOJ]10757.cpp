#include <iostream>
#include <algorithm>
using namespace std;
//숫자가 너무 커서 정수형으로 표현하면 오버플로우가 일어날 수 있음. 그래서 문자열로 받아서 자리수 각각마다 더해주기 
//자리가 올라갈 수 있음 ex)13자리 => 14자리 reverse함수 사용해서 받은 값을 거꾸로 저장하기...
int main() {
	string a, b;
	cin >> a >> b;
	int a_size = a.length(), b_size = b.length();
	reverse(a.begin(), a.end());
	reverse(b.begin(), b.end());
	int round;
	long long result[10000];
	if (a_size > b_size) {
		result[0] = ((int)(a[0] - '0' + b[0] - '0')) % 10;
		round = ((int)(a[0] - '0' + b[0] - '0')) / 10;
		for (int i = 1; i < a_size + 1; i++) {
			if (i <= b_size) {
				result[i] = ((int)(a[i] - '0' + b[i] - '0') + round) % 10;
				round = ((int)(a[i] - '0' + b[i] - '0') + round) / 10;
			}
			else {
				result[i] = ((int)(a[i] - '0') + round) % 10;
				round = ((int)(a[i] - '0') + round) / 10;
			}
		}
		if (result[a_size + 1] > 0) {
			reverse(result, result + a_size + 1);
			for (int i = 0; i < (a_size + 1); i++) {
				cout << result[i];
			}
		}
		else {
			reverse(result, result + a_size);
			for (int i = 0; i < (a_size); i++) {
				cout << result[i];
			}
		}

	}
	else {
		result[0] = ((int)(a[0] - '0' + b[0] - '0')) % 10;
		round = ((int)(a[0] - '0' + b[0] - '0')) / 10;
		for (int i = 1; i < b_size + 1; i++) {
			if (i <= a_size) {
				result[i] = ((int)((a[i] - '0') + (b[i] - '0')) + round) % 10;
				round = ((int)((a[i] - '0') + (b[i] - '0')) + round) / 10;
			}
			else {
				result[i + 1] = ((int)(b[i] - '0') + round) % 10;
				round = ((int)(b[i] - '0') + round) / 10;
			};
		}
		if (result[b_size + 1] > 0) {
			reverse(result, result + b_size + 1);
			for (int i = 0; i < (b_size + 1); i++) {
				cout << result[i];
			}
		}
		else {
			reverse(result, result + b_size);
			for (int i = 0; i < (b_size); i++) {
				cout << result[i];
			}
		}
	}

	//result의 크기가 10000이기 때문에.. 그대로 출력하면 안됨...

}