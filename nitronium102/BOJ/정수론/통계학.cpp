//
// Created by KangMinji on 2022-07-24.
//

#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

typedef pair<int, int> ci;

bool cmp(const ci &a, const ci &b) {
    // 1. 개수에 대해 오름차순
    // 2. 값에 대해 내림차순
    if (a.second != b.second)
        return a.second > b.second;
    return a.first < b.first;
}

int findMode(int n, vector<int> &num) {
    vector<ci> count; // first : 값, second : 개수

    int cur_idx = 0;
    count.push_back({num[0], 1}); // 인덱스 에러 방지용

    // 이미 정렬된 벡터에서 정수의 개수를 count -> 연속되는 개수 count
    for (int i = 1; i < n; i++) {
        if (num[i] == num[i - 1]) // 연속인 경우
            count[cur_idx].second++;
        else {
            count.push_back({num[i], 1}); // 새로운 값 삽입
            cur_idx++;
        }
    }

    // 모두 1개씩 들어있는 경우
    if (cur_idx == 0)
        return num[0];

    // 최빈값 계산
    sort(count.begin(), count.end(), cmp);

    // 여러 개인 경우
    if (count[0].second == count[1].second)
        return count[1].first;
    return count[0].first;
}

int main() {
    int n;
    int sum = 0;
    cin >> n;

    vector<int> num(n);
    for (int i = 0; i < n; i++) {
        cin >> num[i];
        sum += num[i];
    }

    sort(num.begin(), num.end());

    if (round((double)sum / n) == -0)
        cout << "0\n";
    else
        cout << round((double)sum / n) << '\n';
    cout << num[n / 2] << "\n"; // 중앙값
    cout << findMode(n, num) << "\n"; // 최빈값
    cout << num[n - 1] - num[0] << "\n"; // 범위
}