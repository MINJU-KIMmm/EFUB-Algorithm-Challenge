#include <iostream>
using namespace std;
int main() {
    long long a, b, c;
    cin >> a >> b >> c;
    if (b >= c) {
        cout << -1 << endl;
        return 0;
    }
    long long BreakEvenPoint = (int)(a / (c - b));
    cout << BreakEvenPoint + 1 << endl;


    return 0;
}