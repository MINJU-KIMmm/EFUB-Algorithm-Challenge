//
// Created by KangMinji on 2022-07-17.
//

#include <iostream>
#include <unordered_set>
using namespace std;

int main() {
    // 시간 초과 방지
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, n, m, num;

    // 입력
    cin >> t;
    while (t--) {
        unordered_set<int> note;
        cin >> n;
        while (n--) {
            cin >> num;
            note.insert(num);
        }

        cin >> m;
        while (m--) {
            cin >> num;
            if (note.find(num) == note.end())
                cout << "0\n";
            else
                cout << "1\n";
        }
    }
}
