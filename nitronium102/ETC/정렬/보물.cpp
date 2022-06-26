//
// Created by KangMinji on 2022-06-26.
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int n;
    // 입력
    cin >> n;

    vector<int> A(n);
    vector<int> B(n);

    for (int i=0; i<n; i++)
        cin >> A[i];

    for (int i=0; i<n; i++)
        cin >> B[i];

    // S의 최솟값 : A의 최솟값 * B의 최솟값 + A의 두 번째 최솟값 * B의 두 번째 최솟값 + ...
    // B의 수를 재배열하지 말라고는 했지만, 어차피 A 재배열하면 둘 다 재배열한 거랑 똑같아짐
    // 최솟값 계산 : 한 배열은 오름차순, 한 배열은 내림차순으로 배열해야 함
    sort(A.begin(), A.end());
    sort(B.begin(), B.end(), greater<>());

    int sum = 0;
    for (int i=0; i<n; i++)
        sum += A[i]*B[i];

    // 출력
    cout << sum;
}