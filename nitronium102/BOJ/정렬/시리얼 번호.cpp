//
// Created by KangMinji on 2022-06-28.
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int countSum(const string &s){
    int sum = 0;
    for (int i=0; i<s.size(); i++){
        if (isdigit(s[i]))
            sum += s[i] - '0'; // char->int로 변환 필요
    }
    return sum;
}

bool cmp(const string &s1, const string &s2){
    // 1. 길이가 짧은 것이 먼저 온다
    if (s1.size() != s2.size())
        return s1.size() < s2.size();
    // 2. 서로 길이가 같다면 자리수의 합이 작은 것이 먼저 들어온다
    if (countSum(s1) != countSum(s2))
        return countSum(s1) < countSum(s2);
    // 3. 사전순 비교
    return s1 < s2;
}

int main(){
    int n;
    vector<string> serial_num;

    // 입력
    cin >> n;
    serial_num.assign(n, "");
    for (int i=0; i<n; i++) {
        cin >> serial_num[i];
    }

    // 연산
    sort(serial_num.begin(), serial_num.end(), cmp);

    // 출력
    for (int i=0; i<n; i++)
        cout << serial_num[i] << "\n";

}