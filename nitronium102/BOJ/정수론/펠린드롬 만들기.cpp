//
// Created by KangMinji on 2022-07-24.
//

#include <iostream>

using namespace std;

int alphabet[26] = {0,};

/*
 *  대칭문자열 + 중간 문자(0~1글자) + 대칭문자열
 *  1. 각 알파벳이 몇 개인지 저장
 *  2. 사전 순으로 앞선 펠린드롬 수 생성 -> 대칭 문자열에 하나씩 할당
 *  3. 만약 알파벳의 숫자가 홀수인 경우, 중간 문자에 할당. 만약 이미 중간 문자가 있다면 팰린드롬 불가 출력
 */
string makePelindrome() {
    string part1 = "", part2 = "", part3 = "";
    for (int i = 0; i < 26; i++) {
        if (alphabet[i] % 2 == 1) {
            if (part2.size() == 1)
                return "I'm Sorry Hansoo";
            part2 = (char) (i + 'A');
        }
        for (int j = 0; j < alphabet[i] / 2; j++) {
            part1 += (char) (i + 'A');
            part3 = (char) (i + 'A') + part3; // 대칭으로 더해져야 하기 때문에 +=를 쓰면 안 된다!
        }
    }
    return part1 + part2 + part3;
}

int main() {
    string name;
    cin >> name;

    // 1번 : 알파벳 개수 저장
    for (int i = 0; i < name.length(); i++)
        alphabet[name[i] - 'A']++;

    // 2번 : 팰린드롬 수 생성
    cout << makePelindrome();
}