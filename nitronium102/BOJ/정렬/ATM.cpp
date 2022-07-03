//
// Created by KangMinji on 2022-07-01.
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int n;

    // 입력
    cin >> n;
    vector<int> time(n, 0);
    for (int i=0; i<n; i++)
        cin >> time[i];

    // 연산
    sort(time.begin(), time.end());

    // 출력 (1)
    int result = 0, sum;
    for (int i=0; i<n; i++){
        sum = 0;
        for (int j=0; j<=i; j++)
            sum += time[j];
        result += sum;
    }

    // 출력 (2) : 시간복잡도 개선
    // (n-i)을 빈도로 생각
    int result = 0;
    for (int i=0; i<n; i++)
        result += (time[i] * (n-i));

    cout << result;
}
