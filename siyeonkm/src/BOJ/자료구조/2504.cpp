#include <iostream>
#include <vector>
#include <stack>
#include <map>

using namespace std;

int calc(string s) {
    stack<char> st;
    map<char, int> num; //괄호 값
    map<char, char> bracket; //괄호 쌍

    //괄호 쌍과 값 저장
    bracket[')'] = '(';
    bracket[']'] = '[';
    num['('] = 2;
    num['['] = 3;

    int ans = 0, temp = 1;
    for (int i = 0; i < s.length(); i++) {
        switch (s[i]) {
            case '(': case '[': //여는 괄호일 경우
                st.push(s[i]);
                temp *= num[s[i]];
                break;
            case ')': case ']': //닫는 괄호일 경우
                if (st.empty() || st.top() != bracket[s[i]]) {
                    return 0;
                }
                if (s[i - 1] == bracket[s[i]]) {
                    ans += temp;
                }
                temp /= num[bracket[s[i]]]; //이미 값을 더한 경우이므로 나누기
                st.pop();
                break;
        }
    }
    if (st.empty()) { //올바른 괄호라면
        return ans;
    }
    return 0;
}

int main() {
    string s;

    //입력
    cin >> s;
    //연산 & 출력
    cout << calc(s);
    return 0;
}