//
// Created by KangMinji on 2022-06-26.
//

#include <iostream>
#include <vector>
using namespace std;

bool isGroup(string word){
    char c = '.';
    vector<bool> alphabet(26, false);

    for (int i=0; i<word.size(); i++){
        // 1) 연속해서 나타난 문자인 경우
       if (word[i] == c)
            continue;
       // 2) 이전과 다른 문자
       if (alphabet[word[i] - 'a'])
           return false;
       // 벡터 업데이트
       alphabet[word[i]-'a'] = true;
       c = word[i];
    }
    return true;
}

int main(){
    int n;
    int result = 0;
    string word;

    // 입력
    cin >> n;

    while (n--) {
        cin >> word;
        if (isGroup(word))
            result++;
    }

    // 출력
    cout << result;
}
