//
// Created by KangMinji on 2022-10-05.
//

#include <iostream>
#include <queue>
using namespace std;

int main() {
    int n, x;

    // 입출력 시간
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // 입력
    cin >> n;
    priority_queue<int, vector<int>, greater<>> pq; // 최소힙

    for (int i=0; i<n*n; i++) {
        cin >> x;

        pq.push(x);

        if (pq.size() > n) { // 최소 힙의 크기가 n을 넘어가면 가장 작은 값(root) 삭제
            pq.pop();
        }
    }

    // 3) root 출력
    cout << pq.top() << "\n";
}