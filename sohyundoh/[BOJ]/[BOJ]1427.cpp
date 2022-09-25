#include <iostream>

int main() {
    // 1 <= n <= 1,000,000,000
    int n;
    std::cin >> n;

    int count[10] = { 0 };

    while (n > 0) {
        ++count[n % 10];
        n /= 10;
    }

    for (int i = 9; i >= 0; --i) {
        if (count[i] != 0) {
            for (int j = 0; j < count[i]; ++j) {
                std::cout << i;
            }
        }
    }
    std::cout << '\n';
}