#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int need_tape(vector<int> hole, int L) {
	int tape_num = 0;

	while (!hole.empty()) {
		double start = hole.front() - 0.5;
		double range = start + L; // 테이프 범위
		while (!hole.empty()) {
			if (hole.front() < range)
				hole.erase(hole.begin());
			else {
				tape_num++;
				break;
			}
		}
		if (hole.empty())
			tape_num++;
	}
	return tape_num;
}


int main(void) {
	int N, L;

	cin >> N >> L;

	vector<int> hole;
	for (int i = 0; i < N; i++) {
		int spot;
		cin >> spot;
		hole.push_back(spot);
	}
	sort(hole.begin(), hole.end());
	cout << need_tape(hole, L);

}