//
// Created by KangMinji on 2022-07-17.
//

#include <iostream>
#include <set>
using namespace std;

int main() {
    string s;

    cin >> s;

    set<string> subStr;
    /* 1) [0] [1] [2] [3] [4]
     * 2) [0-1] [1-2] [2-3] [3-4]
     * 3) [0-1-2] [1-2-3] [2-3-4]
     * 4) [0-1-2-3] [1-2-3-4]
     * 5) [0-1-2-3-4]
     * => 0으로 시작하는 것 / 1로 시작하는 것 / 2로 시작하는 것 / ...
     */
    for (int i=0; i<s.length(); i++){
        string tmp = "";
        for (int j=i; j<s.length(); j++){
            tmp += s[j];
            subStr.insert(tmp);
        }
    }

    cout << subStr.size();
}