#include <iostream>
#include <cmath>

int main() {
	int x1, x2, y1, y2, t;
	int r1, r2;
	int xDiff, yDiff; // x��ǥ�� ����, y��ǥ�� ����
	int d; // �Ÿ�d, ����� ���� ���� ���� �Ÿ��� �������� ����Ѵ�

	std::cin >> t;
	for (int i = 0; i < t; i++) {
		std::cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
		xDiff = x1 - x2;
		yDiff = y1 - y2;
		d = pow(xDiff, 2) + pow(yDiff, 2); // �Ÿ�

		if (d == 0) {
			if (r1 == r2) std::cout << -1 << "\n";
			else std::cout << 0 << "\n";
		}
		/* ���ɿ��� ���. ���� ���������� ���ٸ� ��ġ�� ���� ���Ѵ�,
		�׷��� �ʴٸ� ��ġ�� ���� ���� */
		else if (pow(r1 - r2, 2) > d) std::cout << 0 << "\n"; // �� ���� ���ο� �ִ�
		else if (pow(r1 - r2, 2) == d) std::cout << 1 << "\n";  // ����
		else if ((pow(r1 - r2, 2) < d) && (pow(r1 + r2, 2) > d)) std::cout << 2 << "\n"; // �� ���� ����
		else if (pow(r1 + r2, 2) == d) std::cout << 1 << "\n"; //����
		else if (pow(r1 + r2, 2) < d) std::cout << 0 << "\n"; // �� ���� �ܺο� �ִ�
	}
	return 0;
}