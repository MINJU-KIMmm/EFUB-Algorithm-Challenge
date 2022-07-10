//
// Created by KangMinji on 2022-07-10.
//

#include <iostream>
#include <map>
using namespace std;

int main() {
    int n, t;
    string type, outfit;

    cin >> n;
    while(n--){
        cin >> t;

        // 옷의 종류, 숫자를 저장
        map<string, int> m;
        while (t--){
            cin >> outfit >> type;
            m[type]++;
        }

        // 연산
        int ans = 1;
        for (auto iter = m.begin(); iter != m.end(); iter++)
            ans *= (iter->second + 1);

        // 알몸인 경우 제외
        cout << ans - 1 << "\n";
    }
}