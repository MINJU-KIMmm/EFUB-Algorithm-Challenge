//
// Created by KangMinji on 2022-07-10.
//

#include <iostream>
#include <stack>
using namespace std;

stack<int> calcPlus(string &a, string &b){
    stack<int> st;

    // 일의 자릿수
    int la = a.length() - 1;
    int lb = b.length() - 1;

    // 올림 여부
    bool carry = false;

    // 공통 부분 덧셈 연산
    while (la >= 0 && lb >= 0){
        int num = (a[la--] - '0') + (b[lb--] - '0');

        if (carry) // 이전 자릿수에서 올림된 경우
            num +=1;
        carry = num / 10; // 이번 자릿수에서 올림 여부 확인

        st.push(num % 10);
    }

    // a에서 남은 숫자 반영
    while (la >= 0){
        int num = a[la--] - '0';
        if (carry) // 이전 자릿수에서 올림된 경우
            num +=1;
        carry = num / 10; // 이번 자릿수에서 올림 여부 확인
        st.push(num % 10);
    }

    // b에서 남은 숫자 반영
    while (lb >= 0){
        int num = b[lb--] - '0';
        if (carry) // 이전 자릿수에서 올림된 경우
            num +=1;
        carry = num / 10; // 이번 자릿수에서 올림 여부 확인
        st.push(num % 10);
    }

    // 마지막 올림 확인
    if (carry)
        st.push(1);

    return st;
}

int main() {
    string a, b;
    cin >> a >> b;

    // 연산
    stack<int> st = calcPlus(a, b);

    while (!st.empty()){
        cout << st.top();
        st.pop();
    }
    cout << "\n";

    return 0;
}