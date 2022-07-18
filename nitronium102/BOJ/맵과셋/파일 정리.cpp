//
// Created by KangMinji on 2022-07-17.
//

#include <iostream>
#include <map>
using namespace std;

int main() {
    int n;
    string filename, ext;
    map<string, int> extension; // 확장자별 개수 저장

    // 입력
    cin >> n;
    while(n--){
        cin >> filename;
        // .뒤에 확장자명
        ext = filename.substr(filename.find(".") +1, filename.length());
        extension[ext] += 1;
    }

    for (auto iter : extension){
        cout << iter.first << " " << iter.second << "\n";
    }
}