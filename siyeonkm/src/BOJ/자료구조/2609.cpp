#include <iostream>

using namespace std;

int main() {
    int a, b;
    int c, d;
    cin >> a >> b;
    c = a; d = b;
    while(b) {
        int tmp = a%b;
        a = b;
        b = tmp;
    }
    cout << a << "\n";
    cout << a*(c/a)*(d/a) << "\n";
}