#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    double A, B, V;
    cin >> A >> B >> V;
    double gap = A - B;
    double target = V - A;
    if (target == 0)
    {
        cout << "1";
        return 0;
    }
    cout << (int)(ceil(target / gap)) + 1;
    return (0);
}