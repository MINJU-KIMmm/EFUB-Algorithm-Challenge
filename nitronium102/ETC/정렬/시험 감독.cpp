//
// Created by KangMinji on 2022-06-26.
//

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, b, c;
    long long num = 0;
    cin >> n;
    vector<int> student(n);

    // 입력
    for (int i=0; i<n; i++)
        cin >> student[i];
    cin >> b >> c;

    // 연산
    for (int i=0; i<n; i++){
        int cnt = student[i];
        // 총감독관
        cnt -= b;
        num++;

        // 총감독관만으로도 충분한 경우
        if (cnt <= 0)
            continue;

        // 부감독관
        num += (cnt / c);
        if (cnt % c != 0)
            num++;
    }

    // 출력
    cout << num;
}