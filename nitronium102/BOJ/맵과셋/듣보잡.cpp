//
// Created by KangMinji on 2022-07-10.
//

#include <iostream>
#include <set>

using namespace std;

int main() {
    int n, m;
    string input;
    set<string> s, answer;

    // 입력
    cin >> n >> m;

    while (n--) {
        cin >> input;
        s.insert(input);
    }

    for (int i = 0; i < m; i++) {
        cin >> input;
        if (s.find(input) != s.end())
            answer.insert(input);
    }

    // 출력
    cout << answer.size() << "\n";
    for (auto pos = answer.begin(); pos != answer.end(); pos++)
        cout << *pos << "\n";
}