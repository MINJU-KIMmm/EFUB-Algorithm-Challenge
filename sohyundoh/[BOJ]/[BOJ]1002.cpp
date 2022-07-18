#include <iostream>
#include <cmath>

int main() {
	int x1, x2, y1, y2, t;
	int r1, r2;
	int xDiff, yDiff; // x좌표의 차이, y좌표의 차이
	int d; // 거리d, 계산의 편리를 위해 실제 거리의 제곱값을 사용한다

	std::cin >> t;
	for (int i = 0; i < t; i++) {
		std::cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
		xDiff = x1 - x2;
		yDiff = y1 - y2;
		d = pow(xDiff, 2) + pow(yDiff, 2); // 거리

		if (d == 0) {
			if (r1 == r2) std::cout << -1 << "\n";
			else std::cout << 0 << "\n";
		}
		/* 동심원인 경우. 만약 반지름까지 같다면 겹치는 점은 무한대,
		그렇지 않다면 겹치는 점은 없다 */
		else if (pow(r1 - r2, 2) > d) std::cout << 0 << "\n"; // 한 원이 내부에 있다
		else if (pow(r1 - r2, 2) == d) std::cout << 1 << "\n";  // 내접
		else if ((pow(r1 - r2, 2) < d) && (pow(r1 + r2, 2) > d)) std::cout << 2 << "\n"; // 두 원이 교접
		else if (pow(r1 + r2, 2) == d) std::cout << 1 << "\n"; //외접
		else if (pow(r1 + r2, 2) < d) std::cout << 0 << "\n"; // 두 원이 외부에 있다
	}
	return 0;
}