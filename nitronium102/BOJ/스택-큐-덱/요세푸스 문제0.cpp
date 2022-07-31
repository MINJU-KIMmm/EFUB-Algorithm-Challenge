//
// Created by KangMinji on 2022-07-31.
//

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<int> playGame(int k, queue<int> &q){
    vector<int> result; // 요세푸스 순열
    int cnt = 0; // 몇 번째 사람인지 표시
    int x;
    while(!q.empty()){
        x = q.front();
        q.pop();
        cnt++;
        if (cnt == k){ // 사람 제거 -> result 순열에 추가
            result.push_back(x);
            cnt = 0;
            continue;
        }
        q.push(x);
    }
    return result;
}

int main() {
    int n, k;
    queue<int> q;

    // 입력
    cin >> n >> k;
    for (int i=1; i<=n; i++)
        q.push(i);

    // 연산
    vector<int> result = playGame(k, q);

    // 출력
    cout << "<";
    for (int i=0; i<result.size()-1; i++)
        cout << result[i] << ", ";
    cout << result[result.size()-1] << ">";
}