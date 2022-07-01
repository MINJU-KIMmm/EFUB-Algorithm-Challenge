//
// Created by KangMinji on 2022-06-28.
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
typedef pair<int, int> ci;

// 다른 지원자에 비해 서류 심사와 면접 시험 결과가 모두 떨어지면 선발 X
int main(){
    int T, N;
    cin >> T;

    vector<ci> people;
    for (int i=0; i<T; i++) {
        cin >> N;
        people.assign(N, {0, 0});
        for (int j = 0; j < N; j++) {
            cin >> people[j].first >> people[j].second;
        }

        // 서류심사 순서대로 정렬(오름차순)
        sort(people.begin(), people.end());

        // 면접 심사 순서 확인
        int result = 1; // 기본적으로 서류 1등은 합격 보장
        int first_order = people[0].second;
        for (int i = 1; i < N; i++){
            if (first_order > people[i].second) { // = 표시 필요X(동석차 X)
                first_order = people[i].second;
                result++;
            }
        }

        cout << result << "\n";
    }
}