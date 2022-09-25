//
// Created by KangMinji on 2022-07-17.
//

#include <iostream>
#include <map>

using namespace std;

/*
 * 개강총회 전 : 개강 총회 시작 시간 이하
 * 개강총회 후 ~ 스트리밍 끝 : 개강총회 종료 시간 이상 ~ 스트리밍 종료 시간 이하
 */
int main() {
    string s, e, q, time, nickname;

    map<string, bool> m;
    int cnt = 0;

    cin >> s >> e >> q;
    while (cin >> time >> nickname) { // 입력이 있는 동안 반복
        if (time <= s)
            m[nickname] = true;
        else if (time >= e && time <= q) {
            if (m[nickname]) {
                cnt++;
                m[nickname] = false; // 중복 count 방지
            }
        }
    }
    cout << cnt << "\n";
}