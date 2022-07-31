#include <iostream>

using namespace std;

int main() {

	int hour, min;

	cin >> hour >> min;

	if (hour == 0) {
		if (min >= 45 && min <= 59) {
			cout << hour << " " << (min - 45) << endl;
		}
		else if (min >= 0 && min < 45) {
			hour = 23;
			min = min - 45 + 60;
			cout << hour << " " << min << endl;
		}
	}
	else if (hour >= 1 && hour <= 23) {
		if (min >= 45 && min <= 59) {
			cout << hour << " " << (min - 45) << endl;
		}
		else if (min >= 0 && min < 45) {
			min = min - 45 + 60;
			cout << (hour - 1) << " " << min << endl;
		}
	}

	return 0;
}