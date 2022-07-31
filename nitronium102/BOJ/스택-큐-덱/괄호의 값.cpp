//
// Created by KangMinji on 2022-07-31.
//

#include <iostream>
#include <stack>
#include <map>

using namespace std;

/* [분배법칙 이용]
 * (()[[]]) = 2*(2+3*(3)) = 2*2 + 2*3*3
 * ( : 2배
 * (( : 4배
 * (([ : 4 더해주고 뒤에 것은 2배(2로 나누기)
 * (()[ : 6배
 * (()[[ : 18배
 * (()[[] : 18 더해주고 뒤에 것은 6배(3으로 나누기)
 * (()[[]] : 값이 나온 것이 아님! []처럼 바로 앞 문자가 여는 괄호일 때만 값이 나온다
 *           뒤에 것들은 2배(3으로 나누기)
 * (()[[]]) : 값이 나온 것이 아님! 뒤에 것들은 1배(2로 나누기)
 */
int calc(string s) {
    stack<char> st;
    map<char, int> num;
    map<char, char> bracket;

    // 괄호 쌍과 값 저장
    num['('] = 2;
    num['['] = 3;
    bracket[')'] = '(';
    bracket[']'] = '[';

    int answer = 0;
    int tmp = 1;
    for (int i = 0; i < s.length(); i++) {
        char c = s[i];
        switch (c) {
            case '(':
            case '[': // 여는 괄호 : 일단 곱셈
                st.push(c);
                tmp *= num[c];
                break;

            case ')':
            case ']': // 닫는 괄호 : tmp 값 나누기
                if (st.empty() || st.top() != bracket[c]) {
                    return 0;
                }
                if (s[i - 1] == bracket[c]) // 바로 앞 문자가 여는 괄호인 경우 : 더해준다
                    answer += tmp;
                tmp /= num[bracket[c]];
                st.pop();
                break;
        }
    }
    if (st.empty()) // 올바른 괄호인 경우
        return answer;
    return 0;
}

int main() {
    string s;
    cin >> s;

    cout << calc(s);
}